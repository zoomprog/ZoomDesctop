import sys
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.WindowsCleaning import Ui_WindowsCleaning
from Settings import Ui_Settings
from Functions.FuncClearDate.SearchTemporaryFiles import search_get_temp_files_size, search_clean_temp_files
from Functions.FuncClearDate.ClearTemporaryFiles import clean_temp_files, clean_directory, get_temp_files_size

class WindowsCleaning(QDialog, Ui_WindowsCleaning):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        search_clean_temp_files()
        self.update_label()

        self.pushClearTemporaryFiles.clicked.connect(self.on_clear_temp_files_clicked)

    def update_label(self):
        self.labelClearTemporaryFiles.setText(f"{search_get_temp_files_size():.2f} MB")
        self.labelClearTemporaryFiles.setStyleSheet("color: red;")

    def on_clear_temp_files_clicked(self):
        clean_temp_files()
        self.update_label()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_set = WindowsCleaning()
    base_set.show()
    sys.exit(app.exec())
