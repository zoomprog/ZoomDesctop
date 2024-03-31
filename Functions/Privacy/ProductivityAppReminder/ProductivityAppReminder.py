import re
import subprocess

def check_StartupAppTask():
    command = 'schtasks /Query /TN "Microsoft\Windows\Application Experience\StartupAppTask"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'StartupAppTask\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def enable_StartupAppTask():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Application Experience\StartupAppTask', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Application Experience\ProgramDataUpdater: {e}")


def disable_StartupAppTask():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Application Experience\StartupAppTask', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Application Experience\ProgramDataUpdater'': {e}")