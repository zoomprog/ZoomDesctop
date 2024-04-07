import re
import subprocess


def SearchNETFrameworkNGENv4030319():
    command = 'schtasks /Query /TN "Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'.NET Framework NGEN v4.0.30319\s+.*\s+(Ready|Running|Disabled)', output)
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


def NETFrameworkNGENv4030319On():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")


def NETFrameworkNGENv4030319Off():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchNETFrameworkNGENv403031964():
    command = 'schtasks /Query /TN "Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'.NET Framework NGEN v4.0.30319 64\s+.*\s+(Ready|Running|Disabled)', output)
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


def NETFrameworkNGENv403031964On():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")


def NETFrameworkNGENv403031964off():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchNETFrameworkNGENv403031964Critical():
    command = 'schtasks /Query /TN "Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64 Critical"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'.NET Framework NGEN v4.0.30319 64 Critic\s+.*\s+(Ready|Running|Disabled)', output)
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


def NETFrameworkNGENv403031964CriticalOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64 Critical', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")


def NETFrameworkNGENv403031964Criticaloff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64 Critical', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу '\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64 Critical': {e}")

def SearchNETFrameworkNGENv4030319Critical():
    command = 'schtasks /Query /TN "Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 Critical"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'.NET Framework NGEN v4.0.30319 Critical\s+.*\s+(Ready|Running|Disabled)', output)
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


def NETFrameworkNGENv4030319CriticalOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 Critical', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")


def NETFrameworkNGENv4030319Criticaloff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 Critical', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")