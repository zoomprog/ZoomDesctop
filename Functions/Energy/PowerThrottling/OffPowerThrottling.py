import winreg

def disable_power_throttling_policy():
    key_path = r"SOFTWARE\Policies\Microsoft\Power\PowerThrottling"
    value_name = "PowerThrottlingOff"

    try:
        # Open the registry key, create if it doesn't exist
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        # Set the value to 1 to disable the policy
        winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 1)
        print("Turn off Power Throttling policy disabled successfully.")
        # Close the registry key
        winreg.CloseKey(key)
    except Exception as e:
        print("An error occurred:", str(e))

