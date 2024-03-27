import winreg as reg


def get_win32_priority_separation_Search():
    try:
        # Определение пути к ключу реестра
        key_path = r"SYSTEM\CurrentControlSet\Control\PriorityControl"
        # Открытие ключа реестра с правами на чтение
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_READ)

        # Считывание значения параметра Win32PrioritySeparation
        value, reg_type = reg.QueryValueEx(registry_key, "Win32PrioritySeparation")

        # Закрытие ключа реестра
        reg.CloseKey(registry_key)

        # Вывод значения параметра
        return value
    except WindowsError as e:
        print(f"Ошибка при чтении реестра: {e}")
        return None


