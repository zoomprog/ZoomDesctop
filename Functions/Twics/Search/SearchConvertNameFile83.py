import winreg as reg


def ConvertNameFile83_Update():
    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\FileSystem"
        # Открываем ключ реестра для чтения и записи
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_READ | reg.KEY_WRITE)

        try:
            # Пытаемся прочитать значение. Если оно существует, возвращаем его.
            value, reg_type = reg.QueryValueEx(registry_key, "NtfsDisable8dot3NameCreation")
            return value
        except FileNotFoundError:
            # Если значение не найдено, создаем его со значением 0
            reg.SetValueEx(registry_key, "NtfsDisable8dot3NameCreation", 0, reg.REG_DWORD, 0)
            print("Значение создано со значением 0")

        # Не забываем закрыть ключ реестра
        reg.CloseKey(registry_key)

    except WindowsError as e:
        print(f"Ошибка при работе с реестром: {e}")

