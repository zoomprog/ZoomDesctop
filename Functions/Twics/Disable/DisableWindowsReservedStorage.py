import winreg


def disable_reserved_storage():
    try:
        # Открываем ключ реестра, где находится настройка зарезервированного хранилища
        # В этом примере используется путь к ключу для Windows 10 версии 1903 и выше
        # ВНИМАНИЕ: Путь может отличаться в зависимости от версии Windows
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\ReserveManager"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)

        # Устанавливаем значение ключа ShippedWithReserves в 0 для отключения зарезервированного хранилища
        winreg.SetValueEx(key, "ShippedWithReserves", 0, winreg.REG_DWORD, 0)

        # Закрываем ключ реестра
        winreg.CloseKey(key)
        print("Зарезервированное хранилище успешно отключено.")
    except Exception as e:
        print(f"Ошибка при отключении зарезервированного хранилища: {e}")

