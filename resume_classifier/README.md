# AI Resume Classifier

A sophisticated web application that uses AI to analyze and rank resumes against job descriptions. Built with Flask, OpenAI GPT, and modern web technologies.

## 🚀 Features

- **AI-Powered Analysis**: Uses OpenAI GPT to intelligently analyze resume compatibility
- **Multi-Format Support**: Handles PDF, DOC, and DOCX files
- **Batch Processing**: Process up to 101 resumes simultaneously
- **Smart Ranking**: Combines AI analysis with TF-IDF similarity scoring
- **Beautiful UI**: Modern, responsive design with drag-and-drop functionality
- **Database Storage**: SQLite database for storing job descriptions and analysis results
- **Detailed Reports**: Comprehensive analysis with strengths, concerns, and assessments

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **AI/ML**: OpenAI GPT-3.5-turbo, scikit-learn
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Bootstrap 5, Font Awesome, JavaScript
- **File Processing**: PyPDF2, python-docx
- **Styling**: Custom CSS with modern gradients and animations

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for AI analysis

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Navigate to the project directory
cd resume_classifier

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the project root:

```bash
# Copy the example file
cp env_example.txt .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_actual_openai_api_key_here
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
```

### 3. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📖 Usage

### 1. Home Page
- View application overview and features
- Navigate to upload or view history

### 2. Upload Resumes
- Enter job title, description, and requirements
- Drag and drop or select multiple resume files (PDF/DOC/DOCX)
- Submit for AI analysis

### 3. View Results
- See ranked candidates with compatibility scores
- View detailed AI analysis for each resume
- Access strengths, concerns, and assessments

### 4. History
- View all previous job descriptions and analyses
- Access past results and statistics

## 🎯 How It Works

### AI Analysis Process

1. **Text Extraction**: Extracts text from uploaded resume files
2. **AI Analysis**: Uses OpenAI GPT to analyze resume against job description
3. **Similarity Scoring**: Calculates TF-IDF similarity between resume and job description
4. **Score Combination**: Combines AI analysis score with similarity score
5. **Ranking**: Ranks candidates by final compatibility score

### Scoring System

- **Excellent (80-100%)**: Highly qualified candidates
- **Good (60-79%)**: Well-qualified candidates  
- **Average (40-59%)**: Moderately qualified candidates
- **Poor (0-39%)**: Less qualified candidates

## 📁 Project Structure

```
resume_classifier/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with styling
│   ├── index.html        # Home page
│   ├── upload.html       # Upload form
│   ├── results.html      # Analysis results
│   └── history.html      # Analysis history
├── uploads/              # Uploaded files (auto-created)
├── resume_classifier.db  # SQLite database (auto-created)
├── env_example.txt       # Environment variables example
└── README.md            # This file
```

## 🔧 Configuration

### File Upload Limits
- Maximum files: 101
- Maximum file size: 16MB per file
- Supported formats: PDF, DOC, DOCX

### AI Analysis Settings
- Model: GPT-3.5-turbo
- Max tokens: 500
- Temperature: 0.3 (for consistent results)

## 🚨 Important Notes

1. **API Key**: You need a valid OpenAI API key for AI analysis
2. **Internet Connection**: Required for OpenAI API calls
3. **File Storage**: Uploaded files are stored locally
4. **Database**: SQLite database is created automatically

## 🐛 Troubleshooting

### Common Issues

1. **"Error in AI analysis"**
   - Check your OpenAI API key
   - Ensure internet connection
   - Verify API key has sufficient credits

2. **"Could not read PDF/DOCX"**
   - Ensure file is not corrupted
   - Check file format is supported
   - Try with different file

3. **"Maximum files exceeded"**
   - Reduce number of files to 101 or less
   - Process in smaller batches

## 🔒 Security Considerations

- API keys are stored in environment variables
- File uploads are validated and sanitized
- SQL injection protection via SQLAlchemy
- XSS protection via template escaping

## 📈 Future Enhancements

- [ ] Export results to PDF/Excel
- [ ] Email notifications
- [ ] Advanced filtering options
- [ ] Custom scoring algorithms
- [ ] Integration with ATS systems
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Bootstrap for the UI framework
- Font Awesome for icons
- Flask community for the web framework 