import re
import subprocess
import winreg


# Disabled

def AcceptedPrivacyPolicyOn():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Personalization\Settings", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AcceptedPrivacyPolicy", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def AcceptedPrivacyPolicyOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Personalization\Settings", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "AcceptedPrivacyPolicy", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchAcceptedPrivacyPolicy():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Personalization\Settings", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "AcceptedPrivacyPolicy")
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