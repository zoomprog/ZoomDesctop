import os

def get_thumbnail_cache_size():
    # Путь к кэшу эскизов в Windows
    local_app_data = os.getenv('LocalAppData')
    if local_app_data is None:
        print("Переменная окружения 'LocalAppData' не определена.")
        return 0

    thumbnail_cache_path = os.path.join(local_app_data, 'Microsoft\\Windows\\Explorer')

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(thumbnail_cache_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)

    return total_size

