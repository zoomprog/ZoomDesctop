import os

def get_total_size_in_mb(directories):
    total_size_bytes = 0

    for directory in directories:
        expanded_directory = os.path.expandvars(directory)
        if os.path.exists(expanded_directory):
            for filename in os.listdir(expanded_directory):
                if filename.endswith(".log"):
                    file_path = os.path.join(expanded_directory, filename)
                    total_size_bytes += os.path.getsize(file_path)

    total_size_mb = total_size_bytes / (1024 * 1024)  # Convert bytes to megabytes
    return total_size_mb

# Замените список директорий на необходимые вам




