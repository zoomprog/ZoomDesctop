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


# from Functions.FuncClearDate.SearchAntivirusWindows import calculate_total_size
# from Functions.FuncClearDate.ClearAntivirusWindows import delete_calculate_total_size


class WindowsCleaning(QDialog, Ui_WindowsCleaning):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        search_clean_temp_files()
        self.update_label()

        self.pushClearTemporaryFiles.clicked.connect(self.on_clear_temp_files_clicked)
        self.pushClearthumbnailcache.clicked.connect(self.on_clear_thumbnail_cache_clicked)
        self.position_of_the_windows_cleaning_widget_buttons()
        self.position_of_the_windows_cleaning_widget_label()

    def update_label(self):
        self.labelClearTemporaryFiles.setText(f"{search_get_temp_files_size():.2f} MB")
        self.labelClearthumbnailcache.setText(f"{get_thumbnail_cache_size() / (1024 * 1024):.2f} MB")
        directories_to_check = [
            'X:\\Windows\\panther\\',
            '%WINDIR%\\Panther',
            '%WINDIR%\\Inf\\Setupapi.log',
            '%WINDIR%\\System32\\Sysprep\\Panther'
        ]
        self.labelClearinstallationlogfiles.setText(f"{get_total_size_in_mb(directories_to_check):.2f} MB")
        self.pushClearinstallationlogfiles.clicked.connect(self.on_clear_installation_log)

    def on_clear_temp_files_clicked(self):
        clean_temp_files()
        self.update_label()

    def on_clear_thumbnail_cache_clicked(self):
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

    def position_of_the_windows_cleaning_widget_buttons(self):
        self.pushClearTemporaryFiles.move(850, 7)
        self.pushClearthumbnailcache.move(850, 7)
        self.pushClearinstallationlogfiles.move(850, 7)
        self.pushClearDownloadedprogramfiles.move(850, 7)
        self.pushClearDeliveryOptimizationFiles.move(850, 7)
        self.pushClearDirectXShaderCache.move(850, 7)
        self.pushClearFileSysremError.move(850, 7)
        self.pushClearChkDsk.move(850, 7)

    def position_of_the_windows_cleaning_widget_label(self):
        self.labelClearTemporaryFiles.move(750, 7)
        self.labelClearthumbnailcache.move(750, 7)
        self.labelClearinstallationlogfiles.move(750, 7)
        self.labelClearDownloadedprogramfiles.move(750, 7)
        self.labelClearDeliveryOptimizationFiles.move(750, 7)
        self.labelClearDirectXShaderCache.move(750, 7)
        self.labelClearFileSysremError.move(750, 7)
        self.labelClearChkDsk.move(750, 7)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_set = WindowsCleaning()
    base_set.show()
    sys.exit(app.exec())
