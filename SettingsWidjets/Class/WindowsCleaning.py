import sys

from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.WindowsCleaning import Ui_WindowsCleaning
from Settings import Ui_Settings

class WindowsCleaning(QDialog, Ui_WindowsCleaning):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_set = WindowsCleaning()
    base_set.show()
    sys.exit(app.exec())