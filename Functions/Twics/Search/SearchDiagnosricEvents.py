import subprocess


def check_logs_status(logs):
    """Проверяет статусы переданных журналов событий с использованием PowerShell."""

    def check_log_status_ps(log_name):
        """Проверяет, включен или отключен журнал событий с использованием PowerShell."""
        try:
            # Команда PowerShell для получения статуса журнала
            ps_command = f"Get-WinEvent -ListLog {log_name} | Select-Object -ExpandProperty IsEnabled"
            # Выполнение команды PowerShell через subprocess
            result = subprocess.check_output(["powershell", "-Command", ps_command], text=True).strip()
            # Определение статуса журнала на основе вывода команды
            if result == "True":
                return "Enabled"
            elif result == "False":
                return "Disabled"
            else:
                return "Unknown status"
        except subprocess.CalledProcessError as e:
            return f"Error checking status: {e}"

    statuses = [check_log_status_ps(log) for log in logs]
    return statuses
