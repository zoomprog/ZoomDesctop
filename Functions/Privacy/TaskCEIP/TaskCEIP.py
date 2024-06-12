import re
import subprocess


# Proxy
def check_Proxy():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Autochk\Proxy"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Proxy\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False


def enable_Proxy():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Autochk\Proxy', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Application Experience\ProgramDataUpdater: {e}")


def disable_Proxy():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Autochk\Proxy', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Application Experience\ProgramDataUpdater'': {e}")


import win32com.client


# BthSQM
def create_bthsqm_task():
    # Получаем доступ к планировщику задач
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')

    # Определяем информацию о задаче
    task_definition = scheduler.NewTask(0)  # Создаем новую задачу
    task_definition.RegistrationInfo.Description = 'BthSQM'
    task_definition.RegistrationInfo.Author = 'AuthorName'

    # Создаем триггер для запуска задачи (например, при старте системы)
    trigger = task_definition.Triggers.Create(8)  # 8 - это EVENT_TRIGGER
    trigger.Id = 'BthSQMTrigger'
    trigger.Enabled = True  # Включаем триггер

    # Создаем действие для задачи (например, запуск программы)
    action = task_definition.Actions.Create(0)  # 0 - это ACTION_EXEC
    action.Path = 'path_to_executable'  # Укажите путь к исполняемому файлу

    # Устанавливаем настройки задачи
    task_definition.Settings.Enabled = True  # Включаем задачу
    task_definition.Settings.StopIfGoingOnBatteries = False

    # Регистрируем задачу в планировщике
    task_folder = scheduler.GetFolder('\\Microsoft\\Windows\\Customer Experience Improvement Program')
    task_folder.RegisterTaskDefinition(
        'BthSQM',  # Имя задачи
        task_definition,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # Используем текущего пользователя
        None,  # Нет пароля
        3,  # TASK_LOGON_INTERACTIVE_TOKEN
        ''  # Нет дополнительных параметров
    )
    print('Задача BthSQM успешно создана.')


def check_BthSQM():
    pass
    # command = 'schtasks /Query /TN "\Microsoft\Windows\Customer Experience Improvement Program\BthSQM"'
    #
    # try:
    #     output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    # except subprocess.CalledProcessError as e:
    #     create_bthsqm_task()
    #     return False
    #
    # # Использование регулярного выражения для поиска строки с задачей и её статусом
    # match = re.search(r'BthSQM\s+.*\s+(Ready|Running|Disabled)', output)
    # if match:
    #     # Получение статуса задачи из найденной строки
    #     status = match.group(1)
    #     if status == "Disabled":
    #         return 'Disabled'
    #     else:
    #         return 'Enabled'
    # else:
    #     print("Задача не найдена.")
    #     return False


def enable_BthSQM():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\BthSQM', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Customer Experience Improvement Program\BthSQM {e}")


def disable_BthSQM():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\BthSQM', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Customer Experience Improvement Program\BthSQM'': {e}")


# Consolidator
def check_Consolidator():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Consolidator\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False


def enable_Consolidator():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\Consolidator', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Application Experience\ProgramDataUpdater: {e}")


def disable_Consolidator():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\Consolidator', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Application Experience\ProgramDataUpdater'': {e}")


# KernelCeipTask

def create_kernel_ceip_task():
    # Получаем доступ к планировщику задач
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')

    # Определяем информацию о задаче
    task_definition = scheduler.NewTask(0)  # Создаем новую задачу
    task_definition.RegistrationInfo.Description = 'KernelCeipTask'
    task_definition.RegistrationInfo.Author = 'AuthorName'

    # Создаем триггер для запуска задачи
    trigger = task_definition.Triggers.Create(8)  # 8 - это EVENT_TRIGGER
    trigger.Id = 'KernelCeipTaskTrigger'
    trigger.Enabled = True  # Включаем триггер

    # Создаем действие для задачи (например, запуск программы)
    action = task_definition.Actions.Create(0)  # 0 - это ACTION_EXEC
    action.Path = 'path_to_executable'  # Укажите путь к исполняемому файлу

    # Устанавливаем настройки задачи
    task_definition.Settings.Enabled = True  # Включаем задачу
    task_definition.Settings.StopIfGoingOnBatteries = False

    # Регистрируем задачу в указанной папке планировщика
    task_folder = scheduler.GetFolder('\\Microsoft\\Windows\\Customer Experience Improvement Program')
    task_folder.RegisterTaskDefinition(
        'KernelCeipTask',  # Имя задачи
        task_definition,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # Используем текущего пользователя
        None,  # Нет пароля
        3,  # TASK_LOGON_INTERACTIVE_TOKEN
        ''  # Нет дополнительных параметров
    )
    print('Задача KernelCeipTask успешно создана.')

def check_KernelCeipTask():
    pass
    # command = 'schtasks /Query /TN "\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask"'
    #
    # try:
    #     output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    # except subprocess.CalledProcessError as e:
    #     create_kernel_ceip_task()
    #     return False
    #
    # # Использование регулярного выражения для поиска строки с задачей и её статусом
    # match = re.search(r'KernelCeipTask\s+.*\s+(Ready|Running|Disabled)', output)
    # if match:
    #     # Получение статуса задачи из найденной строки
    #     status = match.group(1)
    #     if status == "Disabled":
    #         return 'Disabled'
    #     else:
    #         return 'Enabled'
    # else:
    #     print("Задача не найдена.")
    #     return False

def enable_KernelCeipTask():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask: {e}")


def disable_KernelCeipTask():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask'': {e}")

# UsbCeip
def create_usbceip_task():
    # Получаем доступ к планировщику задач
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')

    # Определяем информацию о задаче
    task_definition = scheduler.NewTask(0)  # Создаем новую задачу
    task_definition.RegistrationInfo.Description = 'UsbCeip'
    task_definition.RegistrationInfo.Author = 'AuthorName'

    # Создаем триггер для запуска задачи
    trigger = task_definition.Triggers.Create(8)  # 8 - это EVENT_TRIGGER
    trigger.Id = 'UsbCeipTrigger'
    trigger.Enabled = True  # Включаем триггер

    # Создаем действие для задачи (например, запуск программы)
    action = task_definition.Actions.Create(0)  # 0 - это ACTION_EXEC
    action.Path = 'path_to_executable'  # Укажите путь к исполняемому файлу

    # Устанавливаем настройки задачи
    task_definition.Settings.Enabled = True  # Включаем задачу
    task_definition.Settings.StopIfGoingOnBatteries = False

    # Регистрируем задачу в указанной папке планировщика
    task_folder = scheduler.GetFolder('\\Microsoft\\Windows\\Customer Experience Improvement Program')
    task_folder.RegisterTaskDefinition(
        'UsbCeip',  # Имя задачи
        task_definition,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # Используем текущего пользователя
        None,  # Нет пароля
        3,  # TASK_LOGON_INTERACTIVE_TOKEN
        ''  # Нет дополнительных параметров
    )
    print('Задача UsbCeip успешно создана.')


def check_UsbCeip():
    pass
    # command = 'schtasks /Query /TN "\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask"'
    #
    # try:
    #     output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    # except subprocess.CalledProcessError as e:
    #     create_usbceip_task()
    #     return False
    #
    # # Использование регулярного выражения для поиска строки с задачей и её статусом
    # match = re.search(r'KernelCeipTask\s+.*\s+(Ready|Running|Disabled)', output)
    # if match:
    #     # Получение статуса задачи из найденной строки
    #     status = match.group(1)
    #     if status == "Disabled":
    #         return 'Disabled'
    #     else:
    #         return 'Enabled'
    # else:
    #     print("Задача не найдена.")
    #     return False

def enable_UsbCeip():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask: {e}")


def disable_UsbCeip():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask'': {e}")