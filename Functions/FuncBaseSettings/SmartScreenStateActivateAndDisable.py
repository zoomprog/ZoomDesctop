from main import *
import winreg

def SmartScreenActivate(self):
    # Открываем ключ реестра
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer"
    key_name = "SmartScreenEnabled"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
    # Устанавливаем новое значение
    new_value = "On"  # Здесь можно указать новое значение, например, "on"
    winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, new_value)
    # Закрываем ключ реестра
    winreg.CloseKey(key)
    print("Значение SmartScreenEnabled успешно изменено.")

def SmartScreenDisable(self):
    # Открываем ключ реестра
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer"
    key_name = "SmartScreenEnabled"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
    # Устанавливаем новое значение
    new_value = "Off"  # Здесь можно указать новое значение, например, "on"
    winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, new_value)
    # Закрываем ключ реестра
    winreg.CloseKey(key)
    print("Значение SmartScreenEnabled успешно изменено.")