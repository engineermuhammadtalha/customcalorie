@echo off
echo ====================================
echo    Starting CustomCalorie Server...
echo ====================================
cd /d %~dp0
call .venv\Scripts\activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause
