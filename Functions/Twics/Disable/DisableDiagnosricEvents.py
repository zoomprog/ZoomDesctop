import subprocess

def disable_event_viewer_logs(log_names):
    for log_name in log_names:
        try:
            # Команда PowerShell для изменения настройки журнала событий
            command = f"wevtutil sl {log_name} /e:False"
            # Запуск команды с правами администратора
            subprocess.run(["powershell", "-Command", command], check=True)
            print(f"Журнал {log_name} успешно отключен.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при отключении журнала {log_name}: {e}")

