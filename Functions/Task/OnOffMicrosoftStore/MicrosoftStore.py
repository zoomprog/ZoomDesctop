import re
import subprocess


def check_microsoft_store_status():
    command = r'schtasks /Query /TN "Microsoft\Windows\PushToInstall\Registration"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT, encoding='utf-8',
                                         errors='ignore')
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Registration\s+.*\s+(Ready|Running|Disabled)', output)
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


def enable_microsoft_store():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\PushToInstall\Registration', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")

def disable_microsoft_store():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\PushToInstall\Registration', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def check_microsoft_store_status2():
    command = r'schtasks /Query /TN "Microsoft\Windows\PushToInstall\LoginCheck"'
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output)  # Print raw bytes to inspect the encoding
        output = output.decode('cp1252')  # Try decoding with cp1252
    except subprocess.CalledProcessError as e:
        return False
    except UnicodeDecodeError as e:
        print(f"Unicode decode error: {e}")
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'LoginCheck\s+.*\s+(Ready|Running|Disabled)', output)
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


def enable_microsoft_store2():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\PushToInstall\LoginCheck', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")

def disable_microsoft_store2():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\PushToInstall\LoginCheck', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

