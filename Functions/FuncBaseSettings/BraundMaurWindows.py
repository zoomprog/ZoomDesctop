from main import *
import subprocess


def disableBraundMaurWindows(self):
    cmd_command = 'netsh advfirewall set allprofiles state off'
    subprocess.run(cmd_command, shell=True)

def EnableBraundMaurWindows(self):
    cmd_command = 'netsh advfirewall set allprofiles state on'
    subprocess.run(cmd_command, shell=True)

