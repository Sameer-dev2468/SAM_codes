# Weather Prediction App Launcher (PowerShell)
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Weather Prediction App Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting the Weather Prediction App..." -ForegroundColor Green
Write-Host ""
Write-Host "The app will be available at:" -ForegroundColor Yellow
Write-Host "http://localhost:5000" -ForegroundColor White
Write-Host "http://192.168.29.235:5000" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the app" -ForegroundColor Red
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if required packages are installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
try {
    python -c "import flask, pandas, numpy, sklearn, plotly" 2>$null
    Write-Host "✓ All dependencies are installed" -ForegroundColor Green
} catch {
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ ERROR: Failed to install required packages" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Start the weather app
Write-Host "Starting Flask application..." -ForegroundColor Green
Write-Host ""
python weatherpred.py

# If the app stops, wait for user input
Write-Host ""
Write-Host "The app has stopped. Press Enter to exit..." -ForegroundColor Yellow
Read-Host 