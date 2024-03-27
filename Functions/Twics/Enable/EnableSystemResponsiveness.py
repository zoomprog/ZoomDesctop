import winreg as reg


def set_registry_values(values):
    for value_info in values:
        path = value_info["path"]
        name = value_info["name"]
        value = value_info["value"]
        value_type = value_info["value_type"]
        try:
            # Open the specified registry key for writing
            registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            # Set the value
            reg.SetValueEx(registry_key, name, 0, value_type, value)
            # Close the key
            reg.CloseKey(registry_key)
            print(f"Successfully set {name} to {value}")
        except Exception as e:
            print(f"Error setting {name}: {e}")


def SystemResponsivenessEnable():
    values_to_set = [
        {
            "path": r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile",
            "name": "SystemResponsiveness",
            "value": 0,
            "value_type": reg.REG_DWORD
        },
        {
            "path": r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
            "name": "GPU Priority",
            "value": 8,
            "value_type": reg.REG_DWORD
        },
        {
            "path": r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
            "name": "Priority",
            "value": 6,
            "value_type": reg.REG_DWORD
        }
    ]

    set_registry_values(values_to_set)
