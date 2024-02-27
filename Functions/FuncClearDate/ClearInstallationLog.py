import os

import shutil

def delete_files_in_directories(directories):
    for directory in directories:
        expanded_directory = os.path.expandvars(directory)
        if os.path.exists(expanded_directory):
            try:
                # Use shutil.rmtree to delete directories and their contents recursively
                shutil.rmtree(expanded_directory)
            except Exception as e:
                print(f"Error deleting {expanded_directory}: {e}")
