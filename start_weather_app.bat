@echo off
echo ========================================
echo    Weather Prediction App Launcher
echo ========================================
echo.
echo Starting the Weather Prediction App...
echo.
echo The app will be available at:
echo http://localhost:5000
echo http://192.168.29.235:5000
echo.
echo Press Ctrl+C to stop the app
echo.
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking dependencies...
python -c "import flask, pandas, numpy, sklearn, plotly" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install required packages
        pause
        exit /b 1
    )
)

REM Start the weather app
echo Starting Flask application...
python weatherpred.py

REM If the app stops, wait for user input
echo.
echo The app has stopped. Press any key to exit...
pause >nul 