import subprocess

def PowerSaver_Preset():
    command = 'powercfg /s SCHEME_MAX'
    subprocess.run(["powershell", "-Command", command], shell=True)

