import os

def get_thumbnail_cache_size(directory_path):
    total_size = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    return total_size

# Example usage for Linux (GNOME Desktop)
thumbnail_cache_directory = os.path.expanduser("~/.cache/thumbnails")
cache_size = get_thumbnail_cache_size(thumbnail_cache_directory)
print(f"Thumbnail Cache Size: {cache_size / (1024 * 1024):.2f} MB")
