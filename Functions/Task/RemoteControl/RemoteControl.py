import re
import subprocess


def SearchRemoteAssistanceTask():
    command = 'schtasks /Query /TN "Microsoft\Windows\RemoteAssistance\RemoteAssistanceTask"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'RemoteAssistanceTask\s+.*\s+(Ready|Running|Disabled)', output)
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


def RemoteAssistanceTaskOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\RemoteAssistance\RemoteAssistanceTask', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")

def RemoteAssistanceTaskOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\RemoteAssistance\RemoteAssistanceTask', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

