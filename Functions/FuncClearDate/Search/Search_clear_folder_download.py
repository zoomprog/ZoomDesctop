import os


def get_folder_size_folder_download():
    def calculate_size(exclude_folder):
        path = f"C:/Users/{os.getlogin()}/Downloads"
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            if exclude_folder in dirnames:
                dirnames.remove(exclude_folder)
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size

    exclude_folder = "Telegram Desktop"
    path = f"C:/Users/{os.getlogin()}/Downloads"

    if os.path.exists(os.path.join(path, exclude_folder)):
        total_size_bytes = calculate_size(exclude_folder)
        total_size_kb = total_size_bytes / 1024
        total_size_mb = total_size_kb / 1024
        return total_size_mb
    else:
        print(f"Папка {exclude_folder} не существует в папке {path}.")
