import os
import shutil

def clear_directory_FileSystemError(directory_path):
    try:
        # Удаление всех файлов в директории
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Не удалось удалить {file_path}. Причина: {e}')

        print('Очистка успешно завершена.')

    except Exception as e:
        print(f'Произошла ошибка при очистке: {e}')
