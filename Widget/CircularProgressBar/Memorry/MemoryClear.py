import psutil  # Импортируем модуль psutil для работы с процессами и системной информацией
import ctypes  # Импортируем модуль ctypes для вызова функций из библиотек Windows

def clean_memory():  # Определяем функцию для очистки оперативной памяти
    """
    Очищает оперативную память, освобождая память, используемую процессами.
    """
    try:  # Начало блока обработки исключений
        process_list = psutil.process_iter()  # Получаем итератор всех текущих процессов системы
        for process in process_list:  # Перебираем все процессы в цикле
            if process.pid != psutil.Process().pid:  # Проверяем, что процесс не является текущим процессом скрипта
                # Пытаемся открыть процесс с максимальными правами для доступа
                handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, process.pid)
                if handle:  # Если удалось получить handle процесса
                    # Освобождаем память процесса
                    ctypes.windll.psapi.EmptyWorkingSet(handle)
                    # Закрываем handle процесса
                    ctypes.windll.kernel32.CloseHandle(handle)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
