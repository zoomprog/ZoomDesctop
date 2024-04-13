import psutil

# Получаем информацию об оперативной памяти
mem = psutil.virtual_memory()

# Переводим байты в гигабайты и выводим используемую память
used_memory_gb = mem.used / (1024**3)
print(f"Используемая оперативная память: {used_memory_gb:.2f} ГБ")

