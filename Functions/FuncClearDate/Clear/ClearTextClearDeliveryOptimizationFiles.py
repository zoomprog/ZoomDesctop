import os
import shutil

def clear_delivery_optimization():
    delivery_optimization_path = os.path.join(os.environ["SystemRoot"], "SoftwareDistribution", "DeliveryOptimization")

    try:
        # Проверяем, существует ли директория
        if not os.path.exists(delivery_optimization_path):
            print(f"Директория {delivery_optimization_path} не существует.")
            return

        # Перебор файлов в папке
        for file_name in os.listdir(delivery_optimization_path):
            file_path = os.path.join(delivery_optimization_path, file_name)

            # Удаление файла или директории
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Файл {file_path} удален успешно.")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Директория {file_path} удалена успешно.")
            else:
                print(f"{file_path} не является ни файлом, ни директорией. Пропущено.")

        print("Очистка завершена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

