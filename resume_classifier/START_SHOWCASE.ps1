# AI Resume Classifier - Showcase Mode
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   AI RESUME CLASSIFIER - SHOWCASE" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting the application for tomorrow's showcase..." -ForegroundColor Green
Write-Host ""

# Set environment variables
$env:OPENAI_API_KEY = "REDACTED"
$env:SECRET_KEY = "your-secret-key-here"
$env:FLASK_ENV = "development"

Write-Host "Environment variables configured." -ForegroundColor Green
Write-Host ""
Write-Host "Application will be available at:" -ForegroundColor Yellow
Write-Host "  - http://localhost:5000" -ForegroundColor White
Write-Host "  - http://127.0.0.1:5000" -ForegroundColor White
Write-Host "  - http://192.168.29.235:5000" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Red
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Start the Flask application
try {
    .\venv\Scripts\python.exe app.py
} catch {
    Write-Host "Error starting application: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}

