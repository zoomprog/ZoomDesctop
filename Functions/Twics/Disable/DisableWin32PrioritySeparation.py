import winreg as reg


def set_win32_priority_separation_Disable(value):
    try:
        # Открытие ключа реестра с необходимыми правами доступа
        key_path = r"SYSTEM\CurrentControlSet\Control\PriorityControl"
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)

        # Установка нового значения
        reg.SetValueEx(registry_key, "Win32PrioritySeparation", 0, reg.REG_DWORD, value)

        # Закрытие ключа реестра
        reg.CloseKey(registry_key)
        print(f"Значение 'Win32PrioritySeparation' успешно изменено на {value}")
    except WindowsError as e:
        print(f"Ошибка при изменении реестра: {e}")


