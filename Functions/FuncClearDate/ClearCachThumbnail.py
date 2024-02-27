import os

def delete_thumbnail_cache():
    # Путь к кэшу эскизов в Windows
    thumbnail_cache_path = os.path.join(os.getenv('LocalAppData'), 'Microsoft\\Windows\\Explorer')

    for dirpath, dirnames, filenames in os.walk(thumbnail_cache_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                os.remove(fp)
                print(f"Удален файл: {fp}")
            except Exception as e:
                print(f"Не удалось удалить файл: {fp}. Причина: {str(e)}")

delete_thumbnail_cache()
