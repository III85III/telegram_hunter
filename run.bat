@echo off
title TelegramHunter v3.0 - High-Speed Real Username Scanner [III85III]
color 0B
cd /d "%~dp0"

if not exist "venv" (
    echo [!] Virtual environment not found. Running setup.bat first...
    call setup.bat
)

call venv\Scripts\activate
python hunter.py
pause
