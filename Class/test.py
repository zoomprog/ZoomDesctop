import subprocess

output = subprocess.run(["powershell", "Get-AppxPackage Microsoft.Office.OneNote"], capture_output=True, text=True)

if output.stdout:
    print("Приложение установлено.")
else:
    print("Приложение не установлено.")