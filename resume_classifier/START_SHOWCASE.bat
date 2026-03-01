@echo off
title AI Resume Classifier - Showcase Mode
echo ========================================
echo    AI RESUME CLASSIFIER - SHOWCASE
echo ========================================
echo.
echo Starting the application for tomorrow's showcase...
echo.
cd /d "%~dp0"

REM Set environment variables
set OPENAI_API_KEY=REDACTED
set SECRET_KEY=your-secret-key-here
set FLASK_ENV=development

echo Environment variables configured.
echo.
echo Application will be available at:
echo   - http://localhost:5000
echo   - http://127.0.0.1:5000
echo   - http://192.168.29.235:5000
echo.
echo Press Ctrl+C to stop the application
echo ========================================
echo.

REM Start the Flask application
.\venv\Scripts\python.exe app.py

echo.
echo Application stopped.
pause

