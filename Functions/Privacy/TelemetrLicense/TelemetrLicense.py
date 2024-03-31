import winreg

def NoGenTicketOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Policies\Microsoft\Windows NT\CurrentVersion\Software Protection Platform", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "NoGenTicket")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")

def NoGenTicketOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Policies\Microsoft\Windows NT\CurrentVersion\Software Protection Platform", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "NoGenTicket", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")

def SearchNoGenTicket():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Policies\Microsoft\Windows NT\CurrentVersion\Software Protection Platform", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "NoGenTicket")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 1:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")