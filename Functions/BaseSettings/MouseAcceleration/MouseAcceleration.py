import winreg

def MouseSpeedOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MouseSpeed", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def MouseSpeedOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MouseSpeed", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def SearchMouseSpeed():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "MouseSpeed")
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")

def MouseThreshold1On():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MouseThreshold1", 0, winreg.REG_DWORD, 6)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def MouseThreshold1Off():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MouseThreshold1", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def SearchMouseThreshold1():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "MouseThreshold1")
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")

def MouseThreshold2On():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MouseThreshold2", 0, winreg.REG_DWORD, 10)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def MouseThreshold2Off():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MouseThreshold2", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def SearchMouseThreshold2():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "MouseThreshold2")
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")