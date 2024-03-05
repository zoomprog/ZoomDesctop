import ctypes

def clear_basket():
    try:
        # Display a message box to confirm emptying the Recycle Bin
        response = ctypes.windll.user32.MessageBoxW(None, "Вы уверены, что хотите очистить корзину?", "Подтверждение", 1)

        if response == 1:  # 1 corresponds to "Yes" button
            # Call SHEmptyRecycleBin to empty the Recycle Bin
            result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)

            if result == 0:
                print("Корзина успешно очищена.")
            else:
                raise RuntimeError(f"Failed to empty Recycle Bin. Error code: {result}")
        else:
            print("Очистка корзины отменена.")
    except Exception as e:
        # Handle exceptions
        print(f"Произошла ошибка при очистке корзины: {e}")

