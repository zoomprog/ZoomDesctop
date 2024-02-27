import os
import shutil
import tempfile

def get_temp_files_size():
    temp_dir = tempfile.gettempdir()

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(temp_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except FileNotFoundError:
                pass  # Файл был удален другим процессом

    return total_size / (1024 * 1024)  # переводим байты в мегабайты

def clean_temp_files():
    temp_size_mb = get_temp_files_size()
    print(f"Размер временных файлов: {temp_size_mb:.2f} МБ")

    answer = input("Хотите очистить временные файлы? (да/нет): ").lower()
    if answer == "да":
        temp_dir = tempfile.gettempdir()
        clean_directory(temp_dir)
        print("Очистка временных файлов завершена")
    else:
        print("Очистка отменена")

def clean_directory(directory_path):
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        try:
            if os.path.isfile(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(f"Ошибка при очистке {item_path}: {e}")
            continue  # Продолжаем с следующего файла


if __name__ == "__main__":
    clean_temp_files()
