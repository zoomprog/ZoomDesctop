import winreg

def CEIPSQMOn():
    try:
        # Open the registry key with write permissions
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\SQMClient\Windows", 0, winreg.KEY_WRITE)
        # Delete the value
        winreg.DeleteValue(key, "CEIPEnable")
        # Close the key
        winreg.CloseKey(key)
        print("Value successfully deleted.")
    except FileNotFoundError:
        print("Value not found.")
    except Exception as e:
        print(f"Error deleting value: {e}")

def CEIPSQMOff():
    try:
        # Open the registry key with write permissions
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\SQMClient\Windows", 0, winreg.KEY_WRITE)
        # Set the value
        winreg.SetValueEx(key, "CEIPEnable", 0, winreg.REG_DWORD, 0)
        # Close the key
        winreg.CloseKey(key)
        print("Value successfully set.")
    except Exception as e:
        print(f"Error setting value: {e}")

def SearchCEIPSQM():
    try:
        # Open the registry key with read permissions
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\SQMClient\Windows", 0, winreg.KEY_READ)
        # Read the value
        value, reg_type = winreg.QueryValueEx(key, "CEIPEnable")
        # Close the key
        winreg.CloseKey(key)
        if value == 0:
            return 'Disabled'
        else:
            return 'Enabled'
    except FileNotFoundError:
        print("Registry key not found.")
    except Exception as e:
        print(f"Error reading value: {e}")

