import winreg
from main import *


def disable_location_services(self):
    try:
        # Открываем раздел реестра с настройками местоположения
        reg_path = r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors"
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_WRITE)

        # Устанавливаем значение "DisableLocation" равным 1 для отключения автообновлений
        winreg.SetValueEx(reg_key, "DisableLocation", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(reg_key)
        print("Автообновления карт местонахождения отключены.")

    except Exception as e:
        print("Ошибка при отключении автообновлений карт местонахождения:", str(e))


def enable_location_services(self):
    try:
        # Открываем раздел реестра с настройками местоположения
        reg_path = r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors"
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_WRITE)

        # Устанавливаем значение "DisableLocation" равным 0 для включения автообновлений
        winreg.SetValueEx(reg_key, "DisableLocation", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(reg_key)
        print("Автообновления карт местонахождения включены.")

    except Exception as e:
        print("Ошибка при включении автообновлений карт местонахождения:", str(e))
