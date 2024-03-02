import os

def get_directory_size_FileSysremError():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(r'C:\Windows\System32\Winevt\Logs'):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    # Конвертируем байты в мегабайты
    total_size_in_mb = total_size / (1024.0 ** 2)
    return total_size_in_mb
