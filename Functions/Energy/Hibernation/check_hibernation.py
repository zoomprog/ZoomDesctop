import subprocess
import re

def check_hibernation_PC():
    try:
        result = subprocess.run(['powercfg', '/a'], capture_output=True, text=True, check=True)
        if re.search(r'Hibernation has not been enabled\.', result.stdout):
            return 'off'
        else:
            return 'on'
    except subprocess.CalledProcessError as e:
        print(f'Ошибка при выполнении команды: {e}')
