from main import *
import subprocess


def DefenderOff(self):
    print('off')
    disable_cmd = 'powershell Set-MpPreference -DisableRealtimeMonitoring $true'
    subprocess.run(disable_cmd, shell=True)
    update_cmd = 'powershell Set-MpPreference -SignatureUpdateInterval 0'
    subprocess.run(update_cmd, shell=True)


def DefenderOn(self):
    print('on')
    enable_cmd = 'powershell Set-MpPreference -DisableRealtimeMonitoring $false'
    subprocess.run(enable_cmd, shell=True)
