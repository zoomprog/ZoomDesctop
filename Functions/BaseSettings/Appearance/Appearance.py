import winreg


def TaskbarAnimationsOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "TaskbarAnimations", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def TaskbarAnimationsOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "TaskbarAnimations", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchTaskbarAnimations():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "TaskbarAnimations")
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

def IconsOnlyOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "IconsOnly", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def IconsOnlyOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "IconsOnly", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchIconsOnly():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "IconsOnly")
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

def ListviewShadowOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ListviewShadow", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def ListviewShadowOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ListviewShadow", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchListviewShadow():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "ListviewShadow")
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

def ListviewAlphaSelectOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ListviewAlphaSelect", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def ListviewAlphaSelectOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ListviewAlphaSelect", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchListviewAlphaSelect():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "ListviewAlphaSelect")
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

def MinAnimateOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop\WindowMetrics", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MinAnimate", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def MinAnimateOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop\WindowMetrics", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MinAnimate", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchMinAnimate():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop\WindowMetrics", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "MinAnimate")
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

def DragFullWindowsOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "DragFullWindows", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def DragFullWindowsOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "DragFullWindows", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchDragFullWindows():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "DragFullWindows")
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