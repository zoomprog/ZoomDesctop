import os

def delete_files_except_telegram():
    download_folder_path = f"C:/Users/{os.getlogin()}/Downloads"

    def delete_recursive(folder_path):
        try:
            files_and_folders = os.listdir(folder_path)

            for item in files_and_folders:
                item_path = os.path.join(folder_path, item)

                if os.path.isfile(item_path) and item != 'Telegram Desktop':
                    os.remove(item_path)
                    print(f"Файл {item} удален.")
                elif os.path.isdir(item_path) and item != 'Telegram Desktop':
                    delete_recursive(item_path)

        except Exception as e:
            print(f"Произошла ошибка: {e}")

    delete_recursive(download_folder_path)


