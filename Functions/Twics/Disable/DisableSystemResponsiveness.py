import winreg as reg


def reset_registry_values(values):
    for value_info in values:
        path = value_info["path"]
        name = value_info["name"]
        value = value_info.get("value", None)  # Значение None будет использоваться для удаления ключа
        value_type = value_info.get("value_type", None)
        try:
            registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            if value is not None:
                # Установить значение по умолчанию
                reg.SetValueEx(registry_key, name, 0, value_type, value)
                print(f"Successfully reset {name} to its default value")
            else:
                # Удалить ключ, если значение не предоставлено
                reg.DeleteValue(registry_key, name)
                print(f"Successfully deleted {name}")
            reg.CloseKey(registry_key)
        except Exception as e:
            print(f"Error resetting {name}: {e}")


def SystemResponsivenessDisable():
    values_to_reset = [
        {
            "path": r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile",
            "name": "SystemResponsiveness",
            "value": 20,  # Предполагаемое значение по умолчанию
            "value_type": reg.REG_DWORD
        },
        {
            "path": r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
            "name": "GPU Priority",
            # Значение не указано, ключ будет удалён
        },
        {
            "path": r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
            "name": "Priority",
            # Значение не указано, ключ будет удалён
        }
    ]

    reset_registry_values(values_to_reset)
