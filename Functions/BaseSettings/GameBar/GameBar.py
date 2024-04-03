import winreg


def AutoGameModeEnabledOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "AutoGameModeEnabled")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def AutoGameModeEnabledOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AutoGameModeEnabled", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchAutoGameModeEnabled():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "AutoGameModeEnabled")
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

def GamePanelStartupTipIndexOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "GamePanelStartupTipIndex")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def GamePanelStartupTipIndexOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "GamePanelStartupTipIndex", 0, winreg.REG_DWORD, 3)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchGamePanelStartupTipIndex():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "GamePanelStartupTipIndex")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 3:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")

def ShowStartupPanelOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "ShowStartupPanel")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def ShowStartupPanelOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "ShowStartupPanel", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchShowStartupPanel():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "ShowStartupPanel")
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

def UseNexusForGameBarEnabledOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "UseNexusForGameBarEnabled")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def UseNexusForGameBarEnabledOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "UseNexusForGameBarEnabled", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchUseNexusForGameBarEnabled():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "UseNexusForGameBarEnabled")
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

def AllowAutoGameModeOn():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AllowAutoGameMode", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def AllowAutoGameModeOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AllowAutoGameMode", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchAllowAutoGameMode():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "AllowAutoGameMode")
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

def AllowGameDVROn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "AllowGameDVR")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def AllowGameDVROff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AllowGameDVR", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchAllowGameDVR():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "AllowGameDVR")
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

def AppCaptureEnabledOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "AppCaptureEnabled")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def AppCaptureEnabledOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AppCaptureEnabled", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchAppCaptureEnabled():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "AppCaptureEnabled")
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

def ValueGameBarOn():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "value", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def ValueGameBarOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "value", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchValueGameBar():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "value")
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