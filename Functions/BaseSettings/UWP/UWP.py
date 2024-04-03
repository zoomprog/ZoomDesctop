import winreg


def GlobalUserDisabledOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "GlobalUserDisabled", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def GlobalUserDisabledOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "GlobalUserDisabled", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchGlobalUserDisabled():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "GlobalUserDisabled")
        winreg.CloseKey(key)
        if value == 1:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
        return 'Key not found'
    except OSError as e:
        print(f"Ошибка при чтении значения: {e}")
        return 'Error'


def BackgroundAppGlobalToggleOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Search", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "BackgroundAppGlobalToggle", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def BackgroundAppGlobalToggleOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Search", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "BackgroundAppGlobalToggle", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchBackgroundAppGlobalToggle():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Search", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "BackgroundAppGlobalToggle")
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
        return 'Key not found'
    except OSError as e:
        print(f"Ошибка при чтении значения: {e}")
        return 'Error'


def BackgroundAppGlobalToggleStartOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Services\embeddedmode", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 3)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def GBackgroundAppGlobalToggleStartOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Services\embeddedmode", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 4)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchBackgroundAppGlobalToggleStart():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Services\embeddedmode", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "Start")
        winreg.CloseKey(key)
        if value == 4:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
        return 'Key not found'
    except OSError as e:
        print(f"Ошибка при чтении значения: {e}")
        return 'Error'
