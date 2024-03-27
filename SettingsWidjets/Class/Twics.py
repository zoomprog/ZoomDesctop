import sys
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.Twics import Ui_Twics

from Functions.Twics.Search.SearchSystemResponsiveness import SystemResponsivenessSearch
from Functions.Twics.Disable.DisableSystemResponsiveness import SystemResponsivenessDisable
from Functions.Twics.Enable.EnableSystemResponsiveness import SystemResponsivenessEnable


class TwicsWindows(QDialog, Ui_Twics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateSystemResponsiveness()
        self.pushSystemResponsiveness.clicked.connect(self.ButtonSearchSystemResponsiveness)

    def updateSystemResponsiveness(self):
        result = SystemResponsivenessSearch()
        status = result.get("SystemResponsiveness", "Error")
        if status == "Disable":
            self.labelSystemResponsiveness.setText("Disable")
            self.labelSystemResponsiveness.setStyleSheet('color: red;')
        else:
            self.labelSystemResponsiveness.setText("Enabled")
            self.labelSystemResponsiveness.setStyleSheet('color: green;')

    def ButtonSearchSystemResponsiveness(self):
        result = SystemResponsivenessSearch()
        status = result.get("SystemResponsiveness", "Error")
        if status == "Disable":
            SystemResponsivenessEnable()
        else:
            SystemResponsivenessDisable()
        self.updateSystemResponsiveness()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = TwicsWindows()
    energy_window.show()
    sys.exit(app.exec())
