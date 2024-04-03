import winreg


def EnableFirewallOn():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "EnableFirewall", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def EnableFirewallOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "EnableFirewall", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchEnableFirewall():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "EnableFirewall")
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

def EnableFirewall2On():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "EnableFirewall", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def EnableFirewall2Off():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "EnableFirewall", 0, winreg.REG_DWORD, 0)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchEnableFirewall2():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "EnableFirewall")
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