import psutil
import winreg as reg


def check_svc_host_split_threshold_Search():
    # Определение объема оперативной памяти в килобайтах
    ram_kb = psutil.virtual_memory().total / 1024
    ram_kb = int(ram_kb)  # Преобразование в целое число

    path = r"SYSTEM\CurrentControlSet\Control"
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_READ)
        value, _ = reg.QueryValueEx(key, "SvcHostSplitThresholdInKB")
        reg.CloseKey(key)

        if value < ram_kb:
            return 'Disable'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Параметр SvcHostSplitThresholdInKB не найден.")
    except PermissionError:
        print("Необходимы права администратора для чтения реестра.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


