@echo off
cd /d "C:\Users\TRUPTI SONAVANE\Desktop\Retail supply chain control tower"

echo [%date% %time%] Starting Hourly Refresh... >> hourly_refresh.log

"C:\Users\TRUPTI SONAVANE\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\TRUPTI SONAVANE\Desktop\Retail supply chain control tower\src\hourly_refresh.py" >> hourly_refresh.log 2>&1

set "RESULT=%ERRORLEVEL%"

echo [%date% %time%] Process finished. Exit code: %RESULT% >> hourly_refresh.log

exit /b %RESULT%