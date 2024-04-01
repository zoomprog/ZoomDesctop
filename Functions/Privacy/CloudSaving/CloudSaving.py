import winreg


# Disabled

def DisableSettingSyncOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableSettingSync")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DisableSettingSyncOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableSettingSync", 0, winreg.REG_DWORD, 2)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDisableSettingSync():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableSettingSync")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 2:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")

def DisableSettingSyncUserOverrideOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableSettingSyncUserOverride")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DisableSettingSyncUserOverrideOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableSettingSyncUserOverride", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDisableSettingSyncUserOverride():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableSettingSyncUserOverride")
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

def DisableSyncOnPaidNetworkOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableSyncOnPaidNetwork")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DisableSyncOnPaidNetworkOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableSyncOnPaidNetwork", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDisableSyncOnPaidNetwork():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableSyncOnPaidNetwork")
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

def SyncPolicyOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "SyncPolicy")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def SyncPolicyOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "SyncPolicy", 0, winreg.REG_DWORD, 5)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchSyncPolicy():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "SyncPolicy")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 5:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")

def DisableApplicationSettingSyncOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableApplicationSettingSync")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DisableApplicationSettingSyncOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableApplicationSettingSync", 0, winreg.REG_DWORD, 2)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDisableApplicationSettingSync():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableApplicationSettingSync")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 2:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")

def DisableApplicationSettingSyncUserOverrideOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableApplicationSettingSyncUserOverride")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DisableApplicationSettingSyncUserOverrideOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableApplicationSettingSyncUserOverride", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDisableApplicationSettingSyncUserOverride():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableApplicationSettingSyncUserOverride")
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

def DisableAppSyncSettingSyncOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableAppSyncSettingSync")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DisableAppSyncSettingSyncOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableAppSyncSettingSync", 0, winreg.REG_DWORD, 2)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDisableAppSyncSettingSync():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableAppSyncSettingSync")
        # Закрыть ключ
        winreg.CloseKey(key)
        if value == 2:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Ключ реестра не найден.")
    except Exception as e:
        print(f"Ошибка при чтении значения: {e}")

def DisableAppSyncSettingSyncUserOverrideOn():
    try:
        # Открыть ключ реестра с правами на запись
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Удалить значение
        winreg.DeleteValue(key, "DisableAppSyncSettingSyncUserOverride")
        # Закрыть ключ
        winreg.CloseKey(key)
        print("Значение успешно удалено.")
    except FileNotFoundError:
        print("Значение не найдено.")
    except Exception as e:
        print(f"Ошибка при удалении значения: {e}")


def DisableAppSyncSettingSyncUserOverrideOff():
    try:
        # Открыть ключ реестра в режиме записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_WRITE)
        # Установить значение
        winreg.SetValueEx(key, "DisableAppSyncSettingSyncUserOverride", 0, winreg.REG_DWORD, 1)
        # Закрыть ключ
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения: {e}")


def SearchDisableAppSyncSettingSyncUserOverride():
    try:
        # Открыть ключ реестра в режиме чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\SettingSync", 0, winreg.KEY_READ)
        # Прочитать значение
        value, reg_type = winreg.QueryValueEx(key, "DisableAppSyncSettingSyncUserOverride")
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