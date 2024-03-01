import sys
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.WindowsCleaning import Ui_WindowsCleaning
from Functions.FuncClearDate.Search.SearchTemporaryFiles import search_get_temp_files_size, search_clean_temp_files

from Functions.FuncClearDate.Clear.ClearTemporaryFiles import clean_temp_files
from Functions.FuncClearDate.Search.SearchCachThumbnail import get_thumbnail_cache_size
from Functions.FuncClearDate.Clear.ClearCachThumbnail import delete_thumbnail_cache

from Functions.FuncClearDate.Search.SearchClearInstallationLog import get_total_size_in_mb
from Functions.FuncClearDate.Clear.ClearInstallationLog import delete_files_in_directories
from Functions.FuncClearDate.Search.SearchClearDownloadedprogramfiles import get_search_Downloadedprogramfiles
from Functions.FuncClearDate.Clear.ClearDownloadedprogramfiles import ClearDownloadedprogramfiles
from Functions.FuncClearDate.Search.SearchTextClearDeliveryOptimizationFiles import get_delivery_optimization_size
from Functions.FuncClearDate.Clear.ClearTextClearDeliveryOptimizationFiles import clear_delivery_optimization


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
        self.pushClearDownloadedprogramfiles.clicked.connect(self.on_clear_Downloadedprogramfiles)
        self.pushClearDeliveryOptimizationFiles.clicked.connect(self.on_clear_clear_delivery_optimization)

        self.position_of_the_windows_cleaning_widget_buttons()
        self.position_of_the_windows_cleaning_widget_label()
        self.position_of_the_windows_cleaning_widget_labelName()

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
        self.labelClearDownloadedprogramfiles.setText(f"{get_search_Downloadedprogramfiles():.2f} MB")
        self.labelClearDeliveryOptimizationFiles.setText(f"{get_delivery_optimization_size():.2f} MB")

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

    def on_clear_Downloadedprogramfiles(self):
        ClearDownloadedprogramfiles()
        self.update_label()

    def on_clear_clear_delivery_optimization(self):
        clear_delivery_optimization()
        self.update_label()

    def position_of_the_windows_cleaning_widget_buttons(self):
        button_names = [
            "pushClearTemporaryFiles",
            "pushClearthumbnailcache",
            "pushClearinstallationlogfiles",
            "pushClearDownloadedprogramfiles",
            "pushClearDeliveryOptimizationFiles",
            "pushClearDirectXShaderCache",
            "pushClearFileSysremError",
            "pushClearChkDsk"
        ]

        x_position = 850
        # Loop through button names and set their position
        for button_name in button_names:
            button = getattr(self, button_name)
            button.move(x_position, 7)

    def position_of_the_windows_cleaning_widget_label(self):
        label_names = [
            "labelClearTemporaryFiles",
            "labelClearthumbnailcache",
            "labelClearinstallationlogfiles",
            "labelClearDownloadedprogramfiles",
            "labelClearDeliveryOptimizationFiles",
            "labelClearDirectXShaderCache",
            "labelClearFileSysremError",
            "labelClearChkDsk"
        ]

        x_position = 750
        # Loop through label names and set their position
        for label_name in label_names:
            label = getattr(self, label_name)
            label.move(x_position, 7)

    def position_of_the_windows_cleaning_widget_labelName(self):
        label_Text_name = [
            "labelTextClearTemporaryFiles",
            "labelTextClearthumbnailcache",
            "labelTextClearinstallationlogfiles",
            "labelTextClearDownloadedprogramfiles",
            "labelTextClearDeliveryOptimizationFiles",
            "labelTextClearDirectXShaderCache",
            "labelTextClearFileSysremError",
            "labelTextClearChkDsk"
        ]
        x_position = 20
        for label_Text_name in label_Text_name:
            label_text = getattr(self, label_Text_name)
            label_text.move(x_position, 12)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_set = WindowsCleaning()
    base_set.show()
    sys.exit(app.exec())
