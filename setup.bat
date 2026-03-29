@echo off
echo ====================================
echo   CustomCalorie - First Time Setup
echo ====================================
cd /d %~dp0
echo Creating Python virtual environment...
py -3.11 -m venv .venv
echo Activating environment...
call .venv\Scripts\activate
echo Installing libraries...
pip install -r requirements.txt
echo ====================================
echo DONE! Now double-click start_app.bat
echo ====================================
pause
