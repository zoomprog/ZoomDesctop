import winreg


def enable_reserved_storage():
    try:
        # Определяем путь к ключу реестра
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\ReserveManager"
        # Открываем ключ реестра для записи
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)

        # Устанавливаем значение ключа ShippedWithReserves в 1 для включения зарезервированного хранилища
        winreg.SetValueEx(key, "ShippedWithReserves", 0, winreg.REG_DWORD, 1)

        # Закрываем ключ реестра
        winreg.CloseKey(key)
        print("Зарезервированное хранилище успешно включено.")
    except Exception as e:
        print(f"Ошибка при включении зарезервированного хранилища: {e}")

