from pathlib import Path

def get_folder_size(folder_path):
    folder = Path(folder_path)
    total_size = sum(f.stat().st_size for f in folder.glob('**/*') if f.is_file())
    return total_size

# Путь к папке ProgramData
program_data_path = "C:\\ProgramData\\Microsoft\\Windows Defender"
program_data_size = get_folder_size(program_data_path)

# Путь к папке System32
system32_path = "C:\\Windows\\System32"
system32_size = get_folder_size(system32_path)

# Путь к папке AppData
# Замените [Имя пользователя] на фактическое имя пользователя
appdata_path = "C:\\Users\\[Имя пользователя]\\AppData\\Local\\Microsoft\\Windows Defender"
appdata_size = get_folder_size(appdata_path)

total_size = program_data_size + system32_size + appdata_size

# Преобразование байт в мегабайты
total_size_in_mb = total_size / (1024 * 1024)


print(f"Общий размер всех файлов: {total_size_in_mb} мегабайт")