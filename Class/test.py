import subprocess

def set_hdparm_never():
    try:
        subprocess.run(['hdparm', '-S', '0', '/dev/sda'])  # Замените '/dev/sda' на путь к вашему жесткому диску
        print("Время отключения жесткого диска установлено на 'Никогда'.")
    except FileNotFoundError:
        print("Команда hdparm не найдена. Убедитесь, что она установлена на вашей системе.")

set_hdparm_never()
