
powershell -executionpolicy bypass -command "Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Set-Content -Path C:\Users\rrarr\Downloads\soft.txt"
