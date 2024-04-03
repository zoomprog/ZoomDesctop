import re
import subprocess
import winreg


def NumberOfSIUFInPeriodOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Siuf\Rules", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "NumberOfSIUFInPeriod")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def NumberOfSIUFInPeriodOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Siuf\Rules", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "NumberOfSIUFInPeriod", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchNumberOfSIUFInPeriod():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Siuf\Rules", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "NumberOfSIUFInPeriod")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")


def PeriodInNanoSecondsOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Siuf\Rules", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "PeriodInNanoSeconds")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def PeriodInNanoSecondsOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Siuf\Rules", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "PeriodInNanoSeconds", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchPeriodInNanoSeconds():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Siuf\Rules", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "PeriodInNanoSeconds")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")


def DoNotShowFeedbackNotificationsOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DoNotShowFeedbackNotifications")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DoNotShowFeedbackNotificationsOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DoNotShowFeedbackNotifications", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDoNotShowFeedbackNotifications():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DoNotShowFeedbackNotifications")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 1:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")




def DmClientOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Feedback\Siuf\DmClient', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Feedback\Siuf\DmClient: {e}")

def DmClientOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Feedback\Siuf\DmClient', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу \Microsoft\Windows\Feedback\Siuf\DmClient: {e}")

def SearchDmClient():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Feedback\Siuf\DmClient"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        # Здесь можно добавить логирование или вывод сообщения об ошибке
        return False

    match = re.search(r'DmClient\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False


def DmClientOnScenarioDownloadOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Feedback\Siuf\DmClient: {e}")

def DmClientOnScenarioDownloadOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу \Microsoft\Windows\Feedback\Siuf\DmClient: {e}")

def SearchDmClientOnScenarioDownload():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        # Здесь можно добавить логирование или вывод сообщения об ошибке
        return False

    match = re.search(r'DmClientOnScenarioDownload\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False
