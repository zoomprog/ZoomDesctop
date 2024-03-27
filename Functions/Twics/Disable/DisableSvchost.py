import winreg as reg


def svc_host_split_threshold_Disable():
    # Определение объема оперативной памяти в килобайтах
    ram_kb = 380000
    ram_kb = int(ram_kb)  # Преобразование в целое число

    path = r"SYSTEM\CurrentControlSet\Control"
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
    except PermissionError:
        raise PermissionError("Необходимы права администратора для изменения реестра")

    try:
        reg.SetValueEx(key, "SvcHostSplitThresholdInKB", 0, reg.REG_DWORD, ram_kb)
        print(f"Значение SvcHostSplitThresholdInKB успешно установлено в {ram_kb}")
    except Exception as e:
        print(f"Произошла ошибка при установке значения: {e}")
    finally:
        reg.CloseKey(key)


