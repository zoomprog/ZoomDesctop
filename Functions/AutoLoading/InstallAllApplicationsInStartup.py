import subprocess

def get_startup_programs_count_with_names():
    startup_programs_count = 0
    try:
        # Выполнение команды PowerShell для получения списка программ в автозагрузке с названиями
        command = 'powershell "Get-CimInstance Win32_StartupCommand | Where-Object { $_.Name -ne $null -and $_.Name -ne \'\' } | Measure-Object | Select-Object -ExpandProperty Count"'
        output = subprocess.check_output(command, shell=True, text=True)

        # Преобразование вывода в целое число
        startup_programs_count = int(output.strip())
    except Exception as e:
        print("Ошибка при выполнении команды PowerShell:", e)
    return startup_programs_count


