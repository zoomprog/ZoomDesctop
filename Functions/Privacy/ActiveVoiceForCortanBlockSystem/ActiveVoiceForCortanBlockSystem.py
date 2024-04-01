import winreg


def AgentActivationOnLockScreenEnabledOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Speech_OneCore\Settings\VoiceActivation\UserPreferenceForAllApps", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "AgentActivationOnLockScreenEnabled")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def AgentActivationOnLockScreenEnabledOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Speech_OneCore\Settings\VoiceActivation\UserPreferenceForAllApps", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AgentActivationOnLockScreenEnabled", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchAgentActivationOnLockScreenEnabled():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Speech_OneCore\Settings\VoiceActivation\UserPreferenceForAllApps", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "AgentActivationOnLockScreenEnabled")
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        return "Ключ реестра не найден."
    except Exception as e:
        return f"Ошибка при чтении значения: {e}"


def LetAppsActivateWithVoiceAboveLockOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\AppPrivacy", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "AgentActivationOnLockScreenEnabled")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def LetAppsActivateWithVoiceAboveLockOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\AppPrivacy", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AgentActivationOnLockScreenEnabled", 0, winreg.REG_DWORD, 2)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchLetAppsActivateWithVoiceAboveLock():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\AppPrivacy", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "AgentActivationOnLockScreenEnabled")
        winreg.CloseKey(key)
        if value == 2:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        return "Ключ реестра не найден."
    except Exception as e:
        return f"Ошибка при чтении значения: {e}"
