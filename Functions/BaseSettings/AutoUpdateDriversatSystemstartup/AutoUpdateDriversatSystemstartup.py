import winreg


def ExcludeWUDriversInQualityUpdateOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows Defender Security Center\Notifications", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "ExcludeWUDriversInQualityUpdate")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def ExcludeWUDriversInQualityUpdateOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows Defender Security Center\Notifications", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "ExcludeWUDriversInQualityUpdate", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchExcludeWUDriversInQualityUpdate():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows Defender Security Center\Notifications", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "ExcludeWUDriversInQualityUpdate")
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



def SearchOrderConfigOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "SearchOrderConfig", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def SearchOrderConfigOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "SearchOrderConfig", 0, winreg.REG_DWORD, 3)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchSearchOrderConfig():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "SearchOrderConfig")
        winreg.CloseKey(key)
        if value == 3:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
        return 'Key not found'  # Возвращаем это значение, если ключ не найден
    except OSError as e:
        print(f"Ошибка при чтении значения: {e}")
        return 'Error'  # Можно также вернуть значение, указывающее на ошибку


