import subprocess

def Balance_Preset():
    command = 'powercfg /s SCHEME_BALANCED'
    subprocess.run(["powershell", "-Command", command], shell=True)
# Запуск команды через PowerShell для установки энергоплана на баланс
