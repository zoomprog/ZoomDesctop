import winreg

from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog
import main
from main import *
from SettingsWidjets.BaseSettings import Ui_BaseSettings
from Settings import Ui_Settings
import subprocess

from Functions.BaseSettings.MouseAcceleration.MouseAcceleration import MouseSpeedOn, MouseSpeedOff, SearchMouseSpeed, MouseThreshold1On, MouseThreshold1Off, SearchMouseThreshold1, MouseThreshold2On, MouseThreshold2Off, SearchMouseThreshold2
from Functions.BaseSettings.ProtectionNotifications.ProtectionNotifications import NotificationEnable1On, NotificationEnable1Off, SearchNotificationEnable1, NotificationEnable2On, NotificationEnable2Off, SearchNotificationEnable2, DisableNotifications1On, DisableNotifications1Off, SearchDisableNotifications1
from Functions.BaseSettings.AutoUpdateDriversatSystemstartup.AutoUpdateDriversatSystemstartup import ExcludeWUDriversInQualityUpdateOn, ExcludeWUDriversInQualityUpdateOff, SearchExcludeWUDriversInQualityUpdate, SearchOrderConfigOn, SearchOrderConfigOff, SearchSearchOrderConfig
from Functions.BaseSettings.UWP.UWP import GlobalUserDisabledOn, GlobalUserDisabledOff, SearchGlobalUserDisabled, BackgroundAppGlobalToggleOn, BackgroundAppGlobalToggleOff, SearchBackgroundAppGlobalToggle, BackgroundAppGlobalToggleStartOn, GBackgroundAppGlobalToggleStartOff, SearchBackgroundAppGlobalToggleStart

from enum import Enum, auto


class SystemStatus(Enum):
    DISABLED = auto()
    ENABLED = auto()
    ERROR = auto()


# Constants for repeated strings
STATUS_DISABLED = "Disabled"
STATUS_ENABLED = "Enabled"
STATUS_ERROR = "Error"


class BaseSet(QDialog, Ui_BaseSettings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.positionButton()
        self.positionTextLabel()

        self.updateMouseAcceleration()
        self.updateProtectionNotifications()
        self.updateAutoUpdateDriversatSystemstartup()
        self.AutoUpdateDriversatSystemstartup()
        self.updateUWP()

        self.pushMouseAcceleration.clicked.connect(self.MouseAccelerationButton_clicked)
        self.pushProtectionNotifications.clicked.connect(self.ProtectionNotificationsButton_clicked)
        self.pushAutoUpdateDriversatSystemstartup.clicked.connect(self.AutoUpdateDriversatSystemstartup_clicked)
        self.pushUWP.clicked.connect(self.UWP_clicked)

    def positionTextLabel(self):
        TextLabel_list = [
            "labelMouseAcceleration",
            "labelProtectionNotifications",
            "labelAutoUpdateDriversatSystemstartup",
            "labelUWP",
            "labelAutoUpdatingAppsStore",
            "labelAppearance",
            "labelGameBar",
            "labelMultyPlanOverplay",
            "labelWindowsFirewall",
            "labelWindowsUAC"
        ]
        x_position = 600
        # Loop through button names and set their position
        for button_name in TextLabel_list:
            button = getattr(self, button_name)
            button.move(x_position, 7)

    def positionButton(self):
        frame_list = [
            "pushMouseAcceleration",
            "pushProtectionNotifications",
            "pushAutoUpdateDriversatSystemstartup",
            "pushUWP",
            "pushAutoUpdatingAppsStore",
            "pushAppearance",
            "pushGameBar",
            "pushMultyPlanOverplay",
            "pushWindowsFirewall",
            "pushWindowsUAC"

        ]
        x_position = 780
        for button_name in frame_list:
            button = getattr(self, button_name)
            button.move(x_position, 7)

    def updateMouseAcceleration(self):
        result1 = SearchMouseSpeed()
        result2 = SearchMouseThreshold1()
        result3 = SearchMouseThreshold2()
        if result1 and result2 and result3 == STATUS_DISABLED:
            self.labelMouseAcceleration.setText(STATUS_DISABLED)
            self.labelMouseAcceleration.setStyleSheet('color:green')
        else:
            self.labelMouseAcceleration.setText(STATUS_ENABLED)
            self.labelMouseAcceleration.setStyleSheet('color:red')

    def MouseAccelerationButton_clicked(self):
        result1 = SearchMouseSpeed()
        result2 = SearchMouseThreshold1()
        result3 = SearchMouseThreshold2()
        if result1 and result2 and result3 == STATUS_DISABLED:
            MouseSpeedOn()
            MouseThreshold1On()
            MouseThreshold2On()
        else:
            MouseSpeedOff()
            MouseThreshold1Off()
            MouseThreshold2Off()
        self.updateMouseAcceleration()

    def updateProtectionNotifications(self):
        result1 = SearchNotificationEnable1()
        result2 = SearchNotificationEnable2()
        result3 = SearchDisableNotifications1()
        if result1 and result2 and result3 == STATUS_DISABLED:
            self.labelProtectionNotifications.setText(STATUS_DISABLED)
            self.labelProtectionNotifications.setStyleSheet('color:green')
        else:
            self.labelProtectionNotifications.setText(STATUS_ENABLED)
            self.labelProtectionNotifications.setStyleSheet('color:red')

    def ProtectionNotificationsButton_clicked(self):
        result1 = SearchNotificationEnable1()
        result2 = SearchNotificationEnable2()
        result3 = SearchDisableNotifications1()
        if result1 and result2 and result3 == STATUS_DISABLED:
            NotificationEnable1On()
            NotificationEnable2On()
            DisableNotifications1On()
        else:
            NotificationEnable1Off()
            NotificationEnable2Off()
            DisableNotifications1Off()
        self.updateProtectionNotifications()

    def updateAutoUpdateDriversatSystemstartup(self):
        result1 = SearchExcludeWUDriversInQualityUpdate()
        result2 = SearchSearchOrderConfig()
        if result1 and result2 == STATUS_DISABLED:
            self.labelAutoUpdateDriversatSystemstartup.setText(STATUS_DISABLED)
            self.labelAutoUpdateDriversatSystemstartup.setStyleSheet('color:green')
        else:
            self.labelAutoUpdateDriversatSystemstartup.setText(STATUS_ENABLED)
            self.labelAutoUpdateDriversatSystemstartup.setStyleSheet('color:red')

    def AutoUpdateDriversatSystemstartup(self):
        result1 = SearchExcludeWUDriversInQualityUpdate()
        result2 = SearchSearchOrderConfig()
        if result1 and result2 == STATUS_DISABLED:
            self.labelAutoUpdateDriversatSystemstartup.setText(STATUS_DISABLED)
            self.labelAutoUpdateDriversatSystemstartup.setStyleSheet('color:green')
        else:
            self.labelAutoUpdateDriversatSystemstartup.setText(STATUS_ENABLED)
            self.labelAutoUpdateDriversatSystemstartup.setStyleSheet('color:red')

    def AutoUpdateDriversatSystemstartup_clicked(self):
        result1 = SearchExcludeWUDriversInQualityUpdate()
        result2 = SearchSearchOrderConfig()
        if result1 and result2 == STATUS_DISABLED:
            ExcludeWUDriversInQualityUpdateOn()
            SearchOrderConfigOn()
        else:
            ExcludeWUDriversInQualityUpdateOff()
            SearchOrderConfigOff()
        self.AutoUpdateDriversatSystemstartup()

    def updateUWP(self):
        result1 = SearchGlobalUserDisabled()
        result2 = SearchBackgroundAppGlobalToggleStart()
        result3 = SearchBackgroundAppGlobalToggle()
        if result1 == STATUS_DISABLED:
            self.labelUWP.setText(STATUS_DISABLED)
            self.labelUWP.setStyleSheet('color:green')
        else:
            self.labelUWP.setText(STATUS_ENABLED)
            self.labelUWP.setStyleSheet('color:red')

    def UWP_clicked(self):
        result1 = SearchGlobalUserDisabled()
        result2 = SearchBackgroundAppGlobalToggleStart()
        result3 = SearchBackgroundAppGlobalToggle()
        if result1 == STATUS_DISABLED:
            GlobalUserDisabledOn()
            BackgroundAppGlobalToggleStartOn()
            BackgroundAppGlobalToggleOn()
        else:
            GlobalUserDisabledOff()
            GBackgroundAppGlobalToggleStartOff()
            BackgroundAppGlobalToggleOff()
        self.updateUWP()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = BaseSet()
    energy_window.show()
    sys.exit(app.exec())
