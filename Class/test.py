import ctypes

# Определение необходимых констант и функций из user32.dll
user32 = ctypes.windll.user32
SPI_SETFOREGROUNDLOCKTIMEOUT = 0x2001
SetForegroundLockTimeout = user32.SystemParametersInfoW

# Вызов функции для отключения работы UWP приложений в фоне
# Устанавливаем значение таймаута фокуса окна в 0
success = SetForegroundLockTimeout(SPI_SETFOREGROUNDLOCKTIMEOUT, 0, 0)

if success:
    print("Успешно отключено UWP приложений в фоне.")
else:
    print("Не удалось отключить UWP приложений в фоне.")