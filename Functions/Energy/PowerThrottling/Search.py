import winreg

def check_power_throttling_policy():
    key_path = r"SOFTWARE\Policies\Microsoft\Power\PowerThrottling"
    value_name = "PowerThrottlingOff"

    try:
        # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
        # Try to read the value
        try:
            value, _ = winreg.QueryValueEx(key, value_name)
            if value == 1:
                return 'disabled'
            else:
                return 'enabled'
        except FileNotFoundError:
            print("Turn off Power Throttling policy is currently enabled.")
        # Close the registry key
        winreg.CloseKey(key)
    except FileNotFoundError:
        print("Power Throttling policy key not found. Make sure the policy is set.")

