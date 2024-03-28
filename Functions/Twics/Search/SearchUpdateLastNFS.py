import winreg as reg


def nfs_atime_status_windows_Update():
    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\FileSystem"

        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_READ)
        value, reg_type = reg.QueryValueEx(registry_key, "NtfsDisableLastAccessUpdate")
        reg.CloseKey(registry_key)

        return value

    except WindowsError as e:
        print(f"Ошибка при чтении реестра: {e}")
        return None


