@echo off
title SysInfo Pro v1.0

:: 1. Go to the folder where this batch file is (Project Root)
cd /d "%~dp0"

:: 2. Find Python (Try venv first, then global)
set PYTHON_CMD=python
if exist "venv\Scripts\python.exe" (
    set PYTHON_CMD=venv\Scripts\python.exe
)

:: 3. Auto-install psutil if missing
"%PYTHON_CMD%" -c "import psutil" 2>nul
if errorlevel 1 (
    echo.
    echo [INFO] psutil library not found. Installing automatically...
    "%PYTHON_CMD%" -m pip install -r requirements.txt
    echo.
)

:: 4. Run the App
:: We need to run main.py which is inside SystemInfo\src
if exist "SystemInfo\src\main.py" (
    "%PYTHON_CMD%" "SystemInfo\src\main.py"
) else (
    echo [ERROR] Could not find the app files!
    echo Please ensure "SystemInfo\src\main.py" exists.
    pause
    exit /b 1
)

:: 5. Keep window open if crash
if errorlevel 1 pause