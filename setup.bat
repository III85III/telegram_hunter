@echo off
title TelegramHunter - Auto Installer
color 0B
cd /d "%~dp0"

echo ==============================================================================
echo                TelegramHunter v3.0 - Setup & Installation
echo                              By III85III
echo ==============================================================================
echo.

echo [*] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not added to PATH!
    echo [!] Please install Python 3.10+ from python.org and check "Add to PATH".
    pause
    exit /b 1
)

echo [*] Creating virtual environment (venv)...
if not exist "venv" (
    python -m venv venv
)

echo [*] Installing dependencies...
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo [*] Downloading NLTK English dictionary words (+40,000 real words)...
python -c "import nltk; nltk.download('words')"

echo.
echo ==============================================================================
echo [SUCCESS] Setup completed successfully!
echo You can now run the tool using: run.bat
echo ==============================================================================
echo.
pause
