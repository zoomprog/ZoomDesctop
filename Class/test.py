import subprocess
import chardet


def get_startup_apps():
    startup_apps = []
    output = subprocess.check_output(['wmic', 'startup', 'get', 'Caption'])
    encoding = chardet.detect(output)['encoding']
    decoded_output = output.decode(encoding)
    lines = decoded_output.strip().split('\n')[1:]

    for line in lines:
        app_name = line.strip()
        if app_name:
            startup_apps.append(app_name)

    return startup_apps

print(get_startup_apps())
