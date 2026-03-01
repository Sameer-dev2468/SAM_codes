import os
import json
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import PyPDF2
from docx import Document
import openai
from dotenv import load_dotenv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume_classifier.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Database Models
class JobDescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resumes = db.relationship('Resume', backref='job_description', lazy=True)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, default=0.0)
    ranking = db.Column(db.Integer)
    analysis = db.Column(db.Text)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    job_description_id = db.Column(db.Integer, db.ForeignKey('job_description.id'), nullable=False)

# File processing functions
def extract_text_from_pdf(file_path):
    """Extract text from PDF file"""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_text_from_docx(file_path):
    """Extract text from DOCX file"""
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return ""

def extract_text_from_file(file_path, file_extension):
    """Extract text based on file extension"""
    if file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() in ['.docx', '.doc']:
        return extract_text_from_docx(file_path)
    else:
        return ""

# AI Analysis functions
def analyze_resume_with_ai(resume_content, job_description):
    """Analyze resume using OpenAI API"""
    try:
        prompt = f"""
        Analyze the following resume against the job description and provide:
        1. A compatibility score (0-100)
        2. Key strengths that match the job requirements
        3. Areas of concern or missing qualifications
        4. Overall assessment

        Job Description:
        {job_description}

        Resume Content:
        {resume_content[:3000]}  # Limit content length

        Provide your analysis in JSON format:
        {{
            "score": <compatibility_score>,
            "strengths": ["strength1", "strength2", ...],
            "concerns": ["concern1", "concern2", ...],
            "assessment": "overall_assessment_text"
        }}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert HR recruiter analyzing resumes for job compatibility."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.3
        )

        analysis_text = response.choices[0].message.content
        try:
            analysis_json = json.loads(analysis_text)
            return analysis_json
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "score": 50,
                "strengths": ["Analysis completed"],
                "concerns": ["Could not parse detailed analysis"],
                "assessment": analysis_text
            }

    except Exception as e:
        print(f"Error in AI analysis: {e}")
        return {
            "score": 0,
            "strengths": [],
            "concerns": ["Error in AI analysis"],
            "assessment": "Could not analyze resume"
        }

def calculate_similarity_score(resume_content, job_description):
    """Calculate TF-IDF similarity score"""
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([resume_content, job_description])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(similarity * 100)
    except Exception as e:
        print(f"Error calculating similarity: {e}")
        return 0.0

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get job description
        job_title = request.form.get('job_title', '').strip()
        job_description = request.form.get('job_description', '').strip()
        requirements = request.form.get('requirements', '').strip()

        if not job_title or not job_description:
            flash('Job title and description are required!', 'error')
            return redirect(url_for('upload'))

        # Create job description in database
        jd = JobDescription(
            title=job_title,
            description=job_description,
            requirements=requirements
        )
        db.session.add(jd)
        db.session.commit()

        # Handle file uploads
        files = request.files.getlist('resumes')
        
        if not files or files[0].filename == '':
            flash('Please select at least one resume file!', 'error')
            return redirect(url_for('upload'))

        if len(files) > 101:
            flash('Maximum 101 files allowed!', 'error')
            return redirect(url_for('upload'))

        uploaded_resumes = []
        
        for file in files:
            if file and file.filename:
                # Secure filename and save
                filename = secure_filename(file.filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                file.save(file_path)

                # Extract text content
                file_extension = os.path.splitext(filename)[1]
                content = extract_text_from_file(file_path, file_extension)

                if content.strip():
                    # Analyze with AI
                    ai_analysis = analyze_resume_with_ai(content, job_description)
                    
                    # Calculate similarity score
                    similarity_score = calculate_similarity_score(content, job_description)
                    
                    # Combine scores (AI analysis + similarity)
                    final_score = (ai_analysis.get('score', 0) + similarity_score) / 2

                    # Create resume record
                    resume = Resume(
                        filename=unique_filename,
                        original_filename=filename,
                        content=content,
                        score=final_score,
                        analysis=json.dumps(ai_analysis),
                        job_description_id=jd.id
                    )
                    db.session.add(resume)
                    uploaded_resumes.append(resume)

        db.session.commit()

        # Rank resumes by score
        resumes = Resume.query.filter_by(job_description_id=jd.id).order_by(Resume.score.desc()).all()
        for i, resume in enumerate(resumes, 1):
            resume.ranking = i
        db.session.commit()

        flash(f'Successfully processed {len(uploaded_resumes)} resumes!', 'success')
        return redirect(url_for('results', jd_id=jd.id))

    return render_template('upload.html')

@app.route('/results/<int:jd_id>')
def results(jd_id):
    jd = JobDescription.query.get_or_404(jd_id)
    resumes = Resume.query.filter_by(job_description_id=jd_id).order_by(Resume.ranking).all()
    
    # Parse analysis for each resume
    for resume in resumes:
        try:
            resume.parsed_analysis = json.loads(resume.analysis)
        except:
            resume.parsed_analysis = {"assessment": "Analysis not available"}

    return render_template('results.html', job_description=jd, resumes=resumes)

@app.route('/history')
def history():
    job_descriptions = JobDescription.query.order_by(JobDescription.created_at.desc()).all()
    return render_template('history.html', job_descriptions=job_descriptions)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000) 