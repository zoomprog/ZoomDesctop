import sys
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.WindowsCleaning import Ui_WindowsCleaning
from Settings import Ui_Settings
from Functions.FuncClearDate.SearchTemporaryFiles import search_get_temp_files_size, search_clean_temp_files
from Functions.FuncClearDate.ClearTemporaryFiles import clean_temp_files, clean_directory, get_temp_files_size
from Functions.FuncClearDate.SearchCachThumbnail import get_thumbnail_cache_size
from Functions.FuncClearDate.ClearCachThumbnail import delete_thumbnail_cache
from Functions.FuncClearDate.SearchClearInstallationLog import get_total_size_in_mb
from Functions.FuncClearDate.ClearInstallationLog import delete_files_in_directories


class WindowsCleaning(QDialog, Ui_WindowsCleaning):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        search_clean_temp_files()
        self.update_label()
        self.pushClearTemporaryFiles.clicked.connect(self.on_clear_temp_files_clicked)
        self.pushClearCachThumbnail.clicked.connect(self.on_clear_cach_thumbnail)
        self.pushClearInstallationLog.clicked.connect(self.on_clear_installation_log)

    def update_label(self):
        self.labelClearTemporaryFiles.setText(f"{search_get_temp_files_size():.2f} MB")
        self.labelClearTemporaryFiles.setStyleSheet("color: red;")
        self.labelClearCachThumbnail.setText(f"{get_thumbnail_cache_size() / (1024 * 1024):.2f} MB")
        self.labelClearCachThumbnail.setStyleSheet("color: red;")
        directories_to_check = [
            'X:\\Windows\\panther\\',
            '%WINDIR%\\Panther',
            '%WINDIR%\\Inf\\Setupapi.log',
            '%WINDIR%\\System32\\Sysprep\\Panther'
        ]
        self.labelClearInstallationLog.setText(f"{get_total_size_in_mb(directories_to_check):.2f} MB")
        self.labelClearInstallationLog.setStyleSheet("color: red;")

    def on_clear_temp_files_clicked(self):
        clean_temp_files()
        self.update_label()

    def on_clear_cach_thumbnail(self):
        delete_thumbnail_cache()
        self.update_label()

    def on_clear_installation_log(self):
        directories_to_delete_files = [
            'X:\\Windows\\panther\\',
            '%WINDIR%\\Panther',
            '%WINDIR%\\Inf\\Setupapi.log',
            '%WINDIR%\\System32\\Sysprep\\Panther'
        ]

        delete_files_in_directories(directories_to_delete_files)
        self.update_label()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_set = WindowsCleaning()
    base_set.show()
    sys.exit(app.exec())
