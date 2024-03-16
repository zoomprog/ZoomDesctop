import subprocess
import sys
import winreg

import chardet
import layout
from PyQt6.QtWidgets import QApplication, QDialog, QFrame, QLabel, QPushButton, QVBoxLayout
from PyQt6.uic.properties import QtGui
from PyQt6.uic.uiparser import QtCore
from functools import partial

from SettingsWidjets.AutoLoading import Ui_AutoLoading


class AutoLoadingWindows(QDialog, Ui_AutoLoading):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def get_startup_apps(self):
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

    import winreg

    def toggle_startup(self, program_name):
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        full_key_path = r"HKEY_CURRENT_USER\{}".format(key_path)

        try:
            # Check if the program is currently in startup
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
                try:
                    _, _ = winreg.QueryValueEx(key, program_name)
                    # If program exists in startup, remove it
                    winreg.DeleteValue(key, program_name)
                    print(f'{program_name} отключено успешно.')
                except FileNotFoundError:
                    # If program doesn't exist in startup, add it
                    executable_path = r"C:\Program Files\YourProgram\program.exe"  # Replace with actual path
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as write_key:
                        winreg.SetValueEx(write_key, program_name, 0, winreg.REG_SZ, executable_path)
                        print(f'{program_name} включено успешно.')
        except PermissionError:
            print("Ошибка: Недостаточно прав для доступа к реестру.")
        except Exception as e:
            print(f'Ошибка: {e}')

    def initUI(self):
        self.setGeometry(100, 100, 850, 300)  # Установите размеры окна
        label_height = 50
        programs_with_names = self.get_startup_apps()
        layout = QVBoxLayout(self.scrollAreaWidgetContents)
        count_labels = len(programs_with_names)
        min_count_labels = 9
        if count_labels > min_count_labels:
            scroll_height = count_labels * label_height  # Учитываем все метки
        else:
            scroll_height = min_count_labels * label_height
        self.scrollAreaWidgetContents.setFixedHeight(scroll_height)

        # Создание меток с названиями приложений внутри каждого фрейма
        for i, program_name in enumerate(programs_with_names):
            frame = QFrame(self.scrollAreaWidgetContents)
            frame.setGeometry(20, 20 + i * 60, 900, 50)  # Установите положение и размеры каждого фрейма
            frame.setStyleSheet("background-color: #161A1E; border-radius: 15px;")  # Установите стили фрейма

            label = QLabel(program_name, frame)  # Используем название приложения вместо "Button"
            label.setGeometry(10, 10, 400, 30)  # Установите положение и размеры метки внутри фрейма
            label.setStyleSheet("font-size:16px;")

            button = QPushButton("Кнопка", frame)
            button.setGeometry(800, 10, 100, 30)
            button.setStyleSheet(("""
    QPushButton {
        background-color: #161A1E;
        border-radius: 15px;
        color: white;
        font-size: 10px;
        padding: 10px 20px;
        border: 1px solid white;
    }
    QPushButton:hover {
        background-color: #2C3136; /* Новый цвет при наведении */
    }
"""))
            button.clicked.connect(partial(self.toggle_startup, program_name))
            layout.addWidget(frame)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = AutoLoadingWindows()
    energy_window.show()
    sys.exit(app.exec())
