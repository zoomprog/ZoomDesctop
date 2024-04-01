import winreg


def DisableWindowsLocationProviderOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableWindowsLocationProvider")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")

def DisableWindowsLocationProviderOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableWindowsLocationProvider", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")



def SearchDisableWindowsLocationProvider():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableWindowsLocationProvider")
        winreg.CloseKey(key)
        if value == 1:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        return "Ключ реестра не найден."
    except Exception as e:
        return f"Ошибка при чтении значения: {e}"


def DisableLocationScriptingOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableLocationScripting")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")

def DisableLocationScriptingOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableLocationScripting", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")



def SearchDisableLocationScripting():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableLocation")
        winreg.CloseKey(key)
        if value == 1:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        return "Ключ реестра не найден."
    except Exception as e:
        return f"Ошибка при чтении значения: {e}"


def DisableLocationOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableLocation")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")

def DisableLocationOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableLocation", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")



def SearchDisableLocation():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableLocationScripting")
        winreg.CloseKey(key)
        if value == 1:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        return "Ключ реестра не найден."
    except Exception as e:
        return f"Ошибка при чтении значения: {e}"


def SensorPermissionStateOn():
    try:
        # Corrected the registry path
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}", 0, winreg.KEY_WRITE)
        winreg.DeleteValue(key, "SensorPermissionState")
        winreg.CloseKey(key)
        return "Value successfully deleted."
    except FileNotFoundError:
        return "Value not found."
    except Exception as e:
        return f"Error deleting value: {e}"


def SensorPermissionStateOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "SensorPermissionState", 0, winreg.REG_SZ, 'Deny')
        winreg.CloseKey(key)
        return "Sensor permission set to Deny."
    except Exception as e:
        return f"Error setting value: {e}"


def SearchSensorPermissionState():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "SensorPermissionState")
        winreg.CloseKey(key)
        if value == 'Deny':
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        return "Registry key or value not found."
    except Exception as e:
        return f"Error reading value: {e}"

# Example usage


def SensorPermissionState2On():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Sensor\Overrides\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "SensorPermissionState", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def SensorPermissionState2Off():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Sensor\Overrides\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "SensorPermissionState", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")



def SearchSensorPermissionState2():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Sensor\Overrides\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "SensorPermissionState")
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        return "Ключ реестра не найден."
    except Exception as e:
        return f"Ошибка при чтении значения: {e}"


