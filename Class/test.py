import winreg

def get_registry_value(key_path, value_name):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, value_name)
        winreg.CloseKey(key)
        return value
    except FileNotFoundError:
        print(f"Registry key '{key_path}' not found.")
    except Exception as e:
        print(f"Error reading registry value '{value_name}': {e}")

# Получаем текущее значение ключа SystemResponsiveness
system_responsiveness = get_registry_value(
    r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile",
    "SystemResponsiveness"
)
if system_responsiveness is not None:
    print(f"Current value of 'SystemResponsiveness' is: {system_responsiveness}")
else:
    print("SystemResponsiveness value not found.")

# Получаем текущее значение ключа PriorityGPU
priority_gpu = get_registry_value(
    r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
    "PriorityGPU"
)
if priority_gpu is not None:
    print(f"Current value of 'PriorityGPU' is: {priority_gpu}")
else:
    print("PriorityGPU value not found.")

# Получаем текущее значение ключа Priority
priority = get_registry_value(
    r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games",
    "Priority"
)
if priority is not None:
    print(f"Current value of 'Priority' is: {priority}")
else:
    print("Priority value not found.")
