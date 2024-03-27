import winreg


def check_reserved_storage_Search():
    try:
        # Определяем путь к ключу реестра
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\ReserveManager"
        # Открываем ключ реестра для чтения
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)

        # Читаем значение ключа ShippedWithReserves
        value, _ = winreg.QueryValueEx(key, "ShippedWithReserves")

        # Закрываем ключ реестра
        winreg.CloseKey(key)

        # Проверяем значение ключа
        if value == 1:
            return 'Enabled'
        else:
            return 'Disable'
    except FileNotFoundError:
        print("Ключ реестра не найден. Возможно, зарезервированное хранилище не поддерживается этой версией Windows.")
    except Exception as e:
        print(f"Ошибка при проверке зарезервированного хранилища: {e}")

