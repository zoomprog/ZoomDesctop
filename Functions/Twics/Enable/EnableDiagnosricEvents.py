import subprocess

def enable_event_viewer_logs(log_names):
    for log_name in log_names:
        try:
            # Команда PowerShell для изменения настройки журнала событий на включение
            command = f"wevtutil sl {log_name} /e:True"
            # Использование echo y | для автоматического подтверждения, если это необходимо
            full_command = f"echo y | {command}"
            # Запуск команды с правами администратора
            subprocess.run(["powershell", "-Command", full_command], check=True)
            print(f"Журнал {log_name} успешно включен.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при включении журнала {log_name}: {e}")

