import winreg


def GlobalUserDisabledOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "GlobalUserDisabled", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def GlobalUserDisabledOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "GlobalUserDisabled", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchGlobalUserDisabled():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", 0, winreg.KEY_READ)
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

