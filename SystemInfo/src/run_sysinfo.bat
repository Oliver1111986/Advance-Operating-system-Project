@echo off
title SysInfo Pro v1.0

:: 1. Go to the folder where this batch file lives (SystemInfo\src)
cd /d "%~dp0"

:: 2. Auto-install psutil if missing
python -c "import psutil" 2>nul
if errorlevel 1 (
    echo.
    echo [INFO] psutil library not found. Installing automatically...
    :: Go up two levels to find requirements.txt
    python -m pip install -r "..\..\requirements.txt"
    echo.
)

:: 3. Run the app
:: Use venv Python if it exists, otherwise use system Python
if exist "..\..\venv\Scripts\python.exe" (
    "..\..\venv\Scripts\python.exe" main.py
) else (
    python main.py
)

:: Keep window open if there's an error
if errorlevel 1 pause