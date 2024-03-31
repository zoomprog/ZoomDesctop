import subprocess
import re
import winreg


def enable_TaskMCA_CompatibilityAppraiser():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Device Information\Device: {e}")


def disable_TaskMCA_CompatibilityAppraiser():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser'': {e}")


def check_TaskMCA_status_CompatibilityAppraiser():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e.output}")
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Microsoft Compatibility Appraiser\s+.*\s+(Ready|Running|Disabled)', output)
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

