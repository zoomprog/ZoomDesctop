import winreg

def enable_power_throttling_policy():
    key_path = r"SOFTWARE\Policies\Microsoft\Power\PowerThrottling"
    value_name = "PowerThrottlingOff"

    try:
        # Open the registry key, create if it doesn't exist
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        # Set the value to 0 to enable the policy
        winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 0)
        print("Turn off Power Throttling policy enabled successfully.")
        # Close the registry key
        winreg.CloseKey(key)
    except Exception as e:
        print("An error occurred:", str(e))

