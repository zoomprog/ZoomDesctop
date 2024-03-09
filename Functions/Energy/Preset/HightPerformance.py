import subprocess

def Hight_Performance_Preset():
    command = 'powercfg /s SCHEME_MIN'
    subprocess.run(["powershell", "-Command", command], shell=True)
# Запуск команды через PowerShell для установки энергоплана на High Performance
