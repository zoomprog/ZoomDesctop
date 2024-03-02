import os
import shutil

def clear_directx_shader_cache(login):
    directory_path = f"C:/Users/{login}/AppData/Local/Temp/D3DSCache"

    if os.path.exists(directory_path):
        try:
            # Удаляем все файлы в директории
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)

            print(f"Директория DirectX Shader Cache для пользователя {login} очищена.")
        except Exception as e:
            print(f"Произошла ошибка при очистке директории: {e}")
    else:
        print("Директория не существует.")

