@echo off
title SysInfo Pro v1.0
cd /d "%~dp0"

:: Check if Python is installed (looks in PATH)
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed on this computer.
    echo Please install Python 3.8+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

:: Auto-install psutil if missing
python -c "import psutil" 2>nul
if %errorlevel% neq 0 (
    echo [INFO] Installing psutil library...
    python -m pip install psutil
    echo.
)

:: Run the application
python SystemInfo\src\main.py

if errorlevel 1 pause