import re
import subprocess

import win32com.client

def create_ProgramDataUpdater():
    # Получаем доступ к планировщику задач
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')

    # Определяем информацию о задаче
    task_definition = scheduler.NewTask(0)  # Создаем новую задачу
    task_definition.RegistrationInfo.Description = 'ProgramDataUpdater'
    task_definition.RegistrationInfo.Author = 'AuthorName'

    # Создаем триггер для запуска задачи (например, при старте системы)
    trigger = task_definition.Triggers.Create(8)  # 8 - это EVENT_TRIGGER
    trigger.Id = 'ProgramDataUpdaterTrigger'
    trigger.Enabled = False  # Отключаем триггер

    # Создаем действие для задачи (например, запуск программы)
    action = task_definition.Actions.Create(0)  # 0 - это ACTION_EXEC
    action.Path = 'path_to_executable'  # Укажите путь к исполняемому файлу

    # Устанавливаем настройки задачи
    task_definition.Settings.Enabled = True  # Отключаем задачу
    task_definition.Settings.StopIfGoingOnBatteries = False

    # Регистрируем задачу в планировщике
    task_folder = scheduler.GetFolder('\\Microsoft\\Windows\\Application Experience')
    task_folder.RegisterTaskDefinition(
        'ProgramDataUpdater',  # Имя задачи
        task_definition,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # Используем текущего пользователя
        None,  # Нет пароля
        3,  # TASK_LOGON_INTERACTIVE_TOKEN
        ''  # Нет дополнительных параметров
    )
    print('Задача успешно создана.')

def check_ProgramDataUpdater():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Application Experience\ProgramDataUpdater"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        create_ProgramDataUpdater()
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'rogramDataUpdater\s+.*\s+(Ready|Running|Disabled)', output)
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

def enable_ProgramDataUpdater():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Application Experience\ProgramDataUpdater', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Application Experience\ProgramDataUpdater: {e}")


def disable_ProgramDataUpdater():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Application Experience\ProgramDataUpdater', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Application Experience\ProgramDataUpdater'': {e}")

