import sys
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.Twics import Ui_Twics

from Functions.Twics.Search.SearchSystemResponsiveness import SystemResponsivenessSearch
from Functions.Twics.Disable.DisableSystemResponsiveness import SystemResponsivenessDisable
from Functions.Twics.Enable.EnableSystemResponsiveness import SystemResponsivenessEnable

from Functions.Twics.Search.SearchWin32PrioritySeparation import get_win32_priority_separation_Search
from Functions.Twics.Disable.DisableWin32PrioritySeparation import set_win32_priority_separation_Disable
from Functions.Twics.Enable.EnableWin32PrioritySeparation import set_win32_priority_separation_Enable

from Functions.Twics.Search.SearchMeltdownSpectre import MeltdownSpectre_Search
from Functions.Twics.Disable.DisableMeltdownSpectre import MeltdownSpectre_Disable
from Functions.Twics.Enable.EnableMeltdownSpectre import MeltdownSpectre_Enable

from Functions.Twics.Search.SearchWindowsReservedStorage import check_reserved_storage_Search
from Functions.Twics.Disable.DisableWindowsReservedStorage import disable_reserved_storage
from Functions.Twics.Enable.EnableWindowsReservedStorage import enable_reserved_storage

from enum import Enum, auto


class SystemStatus(Enum):
    DISABLED = auto()
    ENABLED = auto()
    ERROR = auto()


# Constants for repeated strings
STATUS_DISABLED = "Disable"
STATUS_ENABLED = "Enabled"
STATUS_ERROR = "Error"


class TwicsWindows(QDialog, Ui_Twics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateSystemResponsiveness()
        self.updateWin32_priority_separation()
        self.updateMeltdownSpectre()
        self.updateWindowsReservedStorage()
        self.pushSystemResponsiveness.clicked.connect(self.ButtonSearchSystemResponsiveness)
        self.pushWin32PrioritySeparation.clicked.connect(self.ButtonSearchWin32PrioritySeparation)
        self.pushSpectreMeltdown.clicked.connect(self.ButtonSearchMeltdownSpectre)
        self.pushStorageUpdate.clicked.connect(self.ButtonSearchStorageUpdate)

    def updateSystemResponsiveness(self):
        result = SystemResponsivenessSearch()
        status = result.get("SystemResponsiveness", STATUS_ERROR)
        if status == "Disable":
            self.labelSystemResponsiveness.setText(STATUS_DISABLED)
            self.labelSystemResponsiveness.setStyleSheet('color: red;')
        else:
            self.labelSystemResponsiveness.setText(STATUS_ENABLED)
            self.labelSystemResponsiveness.setStyleSheet('color: green;')

    def ButtonSearchSystemResponsiveness(self):
        result = SystemResponsivenessSearch()
        status = result.get("SystemResponsiveness", STATUS_ERROR)
        if status == "Disable":
            SystemResponsivenessEnable()
        else:
            SystemResponsivenessDisable()
        self.updateSystemResponsiveness()

    def updateWin32_priority_separation(self):
        result = get_win32_priority_separation_Search()
        if result is not None:
            if result == 26:
                self.labelWin32PrioritySeparation.setText(STATUS_ENABLED)
                self.labelWin32PrioritySeparation.setStyleSheet('color: green;')
            elif result == 2:
                self.labelWin32PrioritySeparation.setText(STATUS_DISABLED)
                self.labelWin32PrioritySeparation.setStyleSheet('color: red;')
            else:
                print(f"{result}")
        else:
            print('Не удалось получитьзначения Win32')

    def ButtonSearchWin32PrioritySeparation(self):
        result = get_win32_priority_separation_Search()
        if result is not None:
            if result == 26:
                set_win32_priority_separation_Disable(2)
            elif result == 2:
                set_win32_priority_separation_Enable(26)
            else:
                print(f"{result}")
        else:
            print('Не удалось получитьзначения Win32')
        self.updateWin32_priority_separation()

    def updateMeltdownSpectre(self):
        result = MeltdownSpectre_Search()
        if result == STATUS_DISABLED:
            self.labelSpectreMeltdown.setText('Disable')
            self.labelSpectreMeltdown.setStyleSheet('color:red')
        else:
            self.labelSpectreMeltdown.setText('Enable')
            self.labelSpectreMeltdown.setStyleSheet('color:green')

    def ButtonSearchMeltdownSpectre(self):
        result = MeltdownSpectre_Search()
        if result == STATUS_DISABLED:
            MeltdownSpectre_Enable()
        else:
            MeltdownSpectre_Disable()
        self.updateMeltdownSpectre()

    def updateWindowsReservedStorage(self):
        result = check_reserved_storage_Search()
        print(result)
        if result == STATUS_ENABLED:
            self.labelStorageUpdate.setText(STATUS_ENABLED)
            self.labelStorageUpdate.setStyleSheet('color: red;')
        else:
            self.labelStorageUpdate.setText(STATUS_DISABLED)
            self.labelStorageUpdate.setStyleSheet('color: green;')

    def ButtonSearchStorageUpdate(self):
        result = check_reserved_storage_Search()
        if result == STATUS_ENABLED:
            disable_reserved_storage()
        else:
            enable_reserved_storage()
        self.updateWindowsReservedStorage()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = TwicsWindows()
    energy_window.show()
    sys.exit(app.exec())
