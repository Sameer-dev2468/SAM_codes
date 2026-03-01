# 🚀 AI Resume Classifier - Showcase Instructions

## Quick Start for Tomorrow's Demo

### Option 1: Double-click to start
1. **Double-click** `START_SHOWCASE.bat` 
2. Wait for "Running on http://localhost:5000" message
3. Open browser to `http://localhost:5000`

### Option 2: PowerShell (if batch doesn't work)
1. Right-click `START_SHOWCASE.ps1` → "Run with PowerShell"
2. Wait for startup message
3. Open browser to `http://localhost:5000`

## Demo Flow for Showcase

### 1. Home Page Demo
- Show the beautiful landing page
- Highlight key features:
  - ✅ AI-Powered Analysis
  - ✅ Multi-Format Support (PDF, DOC, DOCX)
  - ✅ Batch Processing (up to 101 resumes)
  - ✅ Smart Ranking System

### 2. Upload Demo
- Click "Upload Resumes" button
- Fill in job description:
  ```
  Job Title: Software Engineer
  Description: We are looking for a skilled software engineer with experience in Python, Flask, and machine learning. The ideal candidate should have strong problem-solving skills and experience with web development.
  Requirements: Python, Flask, Machine Learning, Web Development, Problem Solving
  ```
- Upload sample resumes (already in uploads folder)

### 3. Results Demo
- Show AI analysis results
- Highlight compatibility scores
- Show detailed assessments
- Demonstrate ranking system

### 4. History Demo
- Show previous analyses
- Demonstrate data persistence

## Technical Details for Q&A

- **Backend**: Python Flask
- **AI/ML**: OpenAI GPT-3.5-turbo + scikit-learn
- **Database**: SQLite with SQLAlchemy
- **Frontend**: Bootstrap 5 + Custom CSS
- **File Processing**: PyPDF2, python-docx

## Troubleshooting

If the app doesn't start:
1. Make sure Python virtual environment is activated
2. Check that all dependencies are installed
3. Verify OpenAI API key is set
4. Try running `python app.py` directly

## URLs for Demo
- **Local**: http://localhost:5000
- **Network**: http://192.168.29.235:5000

---
**Ready for Showcase! 🎯**

