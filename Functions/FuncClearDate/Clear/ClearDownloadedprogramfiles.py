import os
import shutil

def ClearDownloadedprogramfiles():
    try:
        folder_path = r'C:\Windows\Downloaded Program Files'

        # Проверяем, существует ли директория
        if not os.path.exists(folder_path):
            print(f"Директория {folder_path} не существует.")
            return

        # Перебор файлов в папке
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Удаление файла
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Файл {file_path} удален успешно.")
            else:
                print(f"{file_path} не является файлом. Пропущено.")

        print("Очистка завершена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")