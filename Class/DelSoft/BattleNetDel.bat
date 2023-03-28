@echo off
taskkill /f /im Battle.net.exe
timeout /t 5 /nobreak > nul
start /wait "" "%PROGRAMFILES(X86)%\Battle.net\Uninstall.exe"