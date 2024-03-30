import subprocess
import subprocess
import re
import winreg


def enable_task_schtasks(task_path):
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Device Information\Device', '/ENABLE'], check=True)
        print(f"Задача '{task_path}' успешно включена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Device Information\Device: {e}")


def disable_task_schtasks():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Device Information\Device', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Device Information\Device'': {e}")


def check_task_status():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Device Information\Device"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e.output}")
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Device\s+.*\s+(Ready|Running|Disabled)', output)
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


def SetEmptyDebuggerOn():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\'DeviceCensus.exe'", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, r'C:\WINDOWS\System32\taskkill.exe')
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SetEmptyDebuggerOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\'DeviceCensus.exe'", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, r'')
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchStart2():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\'DeviceCensus.exe'", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "Debugger")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == '':
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")
