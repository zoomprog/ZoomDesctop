import os

def get_search_Downloadedprogramfiles():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(os.path.join(os.environ["SystemRoot"], "Downloaded Program Files")):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size / (1024 * 1024)  # в мегабайтах