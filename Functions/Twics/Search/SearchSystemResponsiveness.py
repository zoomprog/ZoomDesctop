import winreg as reg


def check_registry_values(values):
    results = {}
    for value_info in values:
        path = value_info["path"]
        name = value_info["name"]
        default_value = value_info.get("default_value", None)
        try:
            registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_READ)
            value, _ = reg.QueryValueEx(registry_key, name)
            reg.CloseKey(registry_key)
            if default_value is not None and value == default_value:
                results[name] = "Disable"
            else:
                results[name] = "Enable"
        except FileNotFoundError:
            results[name] = "Disable" if default_value is not None else "Enable"
        except Exception as e:
            print(f"Error checking {name}: {e}")
            results[name] = "Error"
    return results


def SystemResponsivenessSearch():
    values_to_check = [
        {
            "path": r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile",
            "name": "SystemResponsiveness",
            "default_value": 20
        },
        # Другие значения, если необходимо
    ]

    return check_registry_values(values_to_check)