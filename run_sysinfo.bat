@echo off
:: ============================================================================
:: SysInfo Pro - Quick Launch Script
:: Developed by: Oliver, Princeton, and Prince
:: Tubman University - Advanced Operating Systems Project
:: ============================================================================

title SysInfo Pro v1.0

:: Navigate to src folder first
cd /d "%~dp0"

:: Use Python from venv directly (no activation needed)
if exist "%~dp0..\..\venv\Scripts\python.exe" (
    "%~dp0..\..\venv\Scripts\python.exe" main.py
) else (
    python main.py
)

:: Change to the directory where this batch file is located
cd /d "%~dp0src"

:: Check if Python is installed 
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERROR] Python is not installed or not found in PATH.
    echo Please install Python 3.8 or higher from https://python.org
    echo.
    pause
    exit /b 1
)

:: Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo.
    echo [INFO] Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo.
    echo [WARNING] Virtual environment not found.
    echo Using system Python installation.
    echo.
)

:: Check if main.py exists
if not exist "SystemInfo\src\main.py" (
    if exist "src\main.py" (
        set MAIN_PATH=src\main.py
    ) else (
        echo.
        echo [ERROR] main.py not found!
        echo Please ensure the file exists in the src folder.
        echo.
        pause
        exit /b 1
    )
) else (
    set MAIN_PATH=SystemInfo\src\main.py
)

:: Clear screen and run the application
cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                    SysInfo Pro v1.0                        ║
echo ║         System Information                                 ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo Starting application...
echo.

:: Run the Python application
python "%MAIN_PATH%"

:: Keep window open after execution (in case of errors)
if errorlevel 1 (
    echo.
    echo [ERROR] Application exited with an error.
    echo.
    pause
)