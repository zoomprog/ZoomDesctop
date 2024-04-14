import psutil


def memorry_search():
    # Получаем информацию об оперативной памяти
    mem = psutil.virtual_memory()

    # Переводим байты в гигабайты и выводим используемую память
    used_memory_gb = mem.used / (1024 ** 3)
    return used_memory_gb

