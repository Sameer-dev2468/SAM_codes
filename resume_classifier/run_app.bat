@echo off
echo Starting AI Resume Classifier...
cd /d "%~dp0"
set OPENAI_API_KEY=REDACTED
set SECRET_KEY=your-secret-key-here
echo Environment variables set.
echo Starting Flask application...
.\venv\Scripts\python.exe app.py
pause

