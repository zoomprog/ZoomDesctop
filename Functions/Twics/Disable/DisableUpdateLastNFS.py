import winreg as reg


def nfs_atime_status_windows_Disable():
    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\FileSystem"

        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
        reg.SetValueEx(registry_key,"NtfsDisableLastAccessUpdate", 0, reg.REG_DWORD, 0)
    except WindowsError as e:
        print(f"Ошибка при чтении реестра: {e}")
        return None

nfs_atime_status_windows_Disable()