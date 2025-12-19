@echo off
echo Starting Legal Document Assistant...

echo Starting Backend Server...
start "Backend" cmd /k "cd backend && python run.py"

timeout /t 3

echo Starting Frontend Server...
start "Frontend" cmd /k "npm run dev"

echo Both servers are starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Press any key to exit...
pause