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

def EnableAeroPeekOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\DWM", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "EnableAeroPeek", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def EnableAeroPeekOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\DWM", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "EnableAeroPeek", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchEnableAeroPeek():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\DWM", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "EnableAeroPeek")
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

def FontSmoothingOn():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "FontSmoothing", 0, winreg.REG_DWORD, 2)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def FontSmoothingOff():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "FontSmoothing", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchFontSmoothing():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "FontSmoothing")
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

def VisualFXSettingOn():
    # Определите путь и имя ключа реестра
    path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer"
    value_name = "ShellState"

    # Значение, которое вы хотите установить
    new_value = bytes.fromhex("240000003EA8000000000000000000000000000001000000130000000000000063000000")

    try:
        # Откройте ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_WRITE)

        # Установите значение
        winreg.SetValueEx(key, value_name, 0, winreg.REG_BINARY, new_value)

        # Закройте ключ реестра
        winreg.CloseKey(key)

        print("Значение успешно установлено.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def VisualFXSettingOff():
    # Определите путь и имя ключа реестра
    path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer"
    value_name = "ShellState"

    # Значение, которое вы хотите установить
    new_value = bytes.fromhex("240000003EA8000000000000000000000000000001000000130000000000000073000000")

    try:
        # Откройте ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_WRITE)

        # Установите значение
        winreg.SetValueEx(key, value_name, 0, winreg.REG_BINARY, new_value)

        # Закройте ключ реестра
        winreg.CloseKey(key)

        print("Значение успешно установлено.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



def SearchVisualFXSetting():
    # Определите путь и имя ключа реестра
    path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer"
    value_name = "ShellState"

    # Значение для проверки
    check_value = bytes.fromhex("240000003EA8000000000000000000000000000001000000130000000000000073000000")

    try:
        # Откройте ключ реестра с правами на чтение
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_READ)

        # Прочитайте значение
        value, _ = winreg.QueryValueEx(key, value_name)

        # Закройте ключ реестра
        winreg.CloseKey(key)

        # Сравните значение
        if value == check_value:
            return 'Disabled'
        else:
            return 'Enable'
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def VisualFXSettingOn2():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")

def VisualFXSettingOff2():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, 2)
        winreg.CloseKey(key)
    except OSError as e:
        print(f"Ошибка при установке значения: {e}")



def SearchVisualFXSetting2():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects", 0, winreg.KEY_READ)
        value, reg_type = winreg.QueryValueEx(key, "VisualFXSetting")
        winreg.CloseKey(key)
        if value == 2:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
        return 'Key not found'
    except OSError as e:
        print(f"Ошибка при чтении значения: {e}")
        return 'Error'