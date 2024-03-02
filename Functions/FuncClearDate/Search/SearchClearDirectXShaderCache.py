import os
import socket

def get_directory_size(login):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(f"C:/Users/{login}/AppData/Local/Temp/D3DSCache"):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size / (1024 * 1024)
