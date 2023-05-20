from main import *
import subprocess

def WindowsUpdateOff(self):
    print('WindowsUpdateOff')
    subprocess.call(['reg', 'add', 'HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', '/v', 'NoAutoUpdate', '/t', 'REG_DWORD', '/d', '1', '/f'])

def WindowsUpdateOn(self):
    print('WindowsUpdateOn')
    subprocess.call(['reg', 'add', 'HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', '/v', '0', '/t', 'REG_DWORD', '/d', '1', '/f'])