import subprocess

def hibernation_PC_OFF():
    powershell_command = "powercfg -h off"
    subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
    print("Гибернация отключена.")

def hibernation_PC_ON():
    powershell_command = "powercfg -h on"
    subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
    print("Гибернация включена.")
