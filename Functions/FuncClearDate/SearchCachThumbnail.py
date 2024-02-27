import os


def get_thumbnail_cache_size():
    # Путь к кэшу эскизов в Windows
    thumbnail_cache_path = os.path.join(os.getenv('LocalAppData'), 'Microsoft\\Windows\\Explorer')

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(thumbnail_cache_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)

    return total_size


# Получить размер кэша эскизов в байтах
thumbnail_cache_size_bytes = get_thumbnail_cache_size()

# Преобразовать размер в мегабайты
thumbnail_cache_size_megabytes = thumbnail_cache_size_bytes / (1024 * 1024)
