import os
import shutil
import tempfile

def search_get_temp_files_size():
    temp_dir = tempfile.gettempdir()

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(temp_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except FileNotFoundError:
                pass  # File was deleted by another process

    return total_size / (1024 * 1024)  # Convert bytes to megabytes

def search_clean_temp_files():
    temp_size_mb = search_get_temp_files_size()

