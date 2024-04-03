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
from Functions.BaseSettings.AutoUpdatingAppsStore.AutoUpdatingAppsStore import AutoDownloadOn, AutoDownloadOff, SearchAutoDownload
from Functions.BaseSettings.Appearance.Appearance import (TaskbarAnimationsOn, TaskbarAnimationsOff, SearchTaskbarAnimations, IconsOnlyOn, IconsOnlyOff, SearchIconsOnly, ListviewShadowOn, ListviewShadowOff, SearchListviewShadow, ListviewAlphaSelectOn, ListviewAlphaSelectOff, SearchListviewAlphaSelect, MinAnimateOn, MinAnimateOff, SearchMinAnimate, DragFullWindowsOn, DragFullWindowsOff,
                                                          SearchDragFullWindows, EnableAeroPeekOn, EnableAeroPeekOff, SearchEnableAeroPeek, FontSmoothingOn, FontSmoothingOff, SearchFontSmoothing, VisualFXSettingOn, VisualFXSettingOff, SearchVisualFXSetting, VisualFXSettingOn2, VisualFXSettingOff2, SearchVisualFXSetting2)
from Functions.BaseSettings.GameBar.GameBar import (AutoGameModeEnabledOn, AutoGameModeEnabledOff, SearchAutoGameModeEnabled, GamePanelStartupTipIndexOn, GamePanelStartupTipIndexOff, SearchGamePanelStartupTipIndex, ShowStartupPanelOn, ShowStartupPanelOff, SearchShowStartupPanel, UseNexusForGameBarEnabledOn, UseNexusForGameBarEnabledOff, SearchUseNexusForGameBarEnabled, AllowAutoGameModeOn,
                                                    AllowAutoGameModeOff, SearchAllowAutoGameMode, AllowGameDVROn, AllowGameDVROff, SearchAllowGameDVR, AppCaptureEnabledOff, AppCaptureEnabledOn, SearchAppCaptureEnabled, ValueGameBarOn, ValueGameBarOff, SearchValueGameBar)
from Functions.BaseSettings.MultyPlanOverplay.MultyPlanOverplay import OverlayTestModeOn, OverlayTestModeOff, SearchOverlayTestMode
from Functions.BaseSettings.WindowsFirewall.WindowsFirewall import EnableFirewallOn, EnableFirewallOff, SearchEnableFirewall, EnableFirewall2On, EnableFirewall2Off, SearchEnableFirewall2
from Functions.BaseSettings.UAC.UAC import PromptOnSecureDesktopOn, PromptOnSecureDesktopOff, SearchPromptOnSecureDesktop, ConsentPromptBehaviorAdminOn, ConsentPromptBehaviorAdminOff, SearchConsentPromptBehaviorAdmin
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
        self.updateAutoUpdatingAppsStore()
        self.updateAppearance()
        self.updateGameBar()
        self.updateMultyPlanOverplay()
        self.updateWindowsFirewall()
        self.updateWindowsUAC()

        self.pushMouseAcceleration.clicked.connect(self.MouseAccelerationButton_clicked)
        self.pushProtectionNotifications.clicked.connect(self.ProtectionNotificationsButton_clicked)
        self.pushAutoUpdateDriversatSystemstartup.clicked.connect(self.AutoUpdateDriversatSystemstartup_clicked)
        self.pushUWP.clicked.connect(self.UWP_clicked)
        self.pushAutoUpdatingAppsStore.clicked.connect(self.AutoUpdatingAppsStore_clicked)
        self.pushAppearance.clicked.connect(self.Appearance_clicked)
        self.pushGameBar.clicked.connect(self.GameBar_clicked)
        self.pushMultyPlanOverplay.clicked.connect(self.MultyPlanOverplay_clicked)
        self.pushWindowsFirewall.clicked.connect(self.WindowsFirewall_clicked)
        self.pushWindowsUAC.clicked.connect(self.WindowsUAC_clicked)

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
        if result1 and result2 and result3== STATUS_DISABLED:
            self.labelUWP.setText(STATUS_DISABLED)
            self.labelUWP.setStyleSheet('color:green')
        else:
            self.labelUWP.setText(STATUS_ENABLED)
            self.labelUWP.setStyleSheet('color:red')

    def UWP_clicked(self):
        result1 = SearchGlobalUserDisabled()
        result2 = SearchBackgroundAppGlobalToggleStart()
        result3 = SearchBackgroundAppGlobalToggle()
        if result1 and result2 and result3 == STATUS_DISABLED:
            GlobalUserDisabledOn()
            BackgroundAppGlobalToggleStartOn()
            BackgroundAppGlobalToggleOn()
        else:
            GlobalUserDisabledOff()
            GBackgroundAppGlobalToggleStartOff()
            BackgroundAppGlobalToggleOff()
        self.updateUWP()

    def updateAutoUpdatingAppsStore(self):
        result = SearchAutoDownload()
        if result == STATUS_DISABLED:
            self.labelAutoUpdatingAppsStore.setText(STATUS_DISABLED)
            self.labelAutoUpdatingAppsStore.setStyleSheet('color:green')
        else:
            self.labelAutoUpdatingAppsStore.setText(STATUS_ENABLED)
            self.labelAutoUpdatingAppsStore.setStyleSheet('color:red')

    def AutoUpdatingAppsStore_clicked(self):
        result = SearchAutoDownload()
        if result == STATUS_DISABLED:
            AutoDownloadOn()
        else:
            AutoDownloadOff()
        self.updateAutoUpdatingAppsStore()

    def updateAppearance(self):
        result1 = SearchTaskbarAnimations()
        result2 = SearchIconsOnly()
        result3 = SearchListviewShadow()
        result4 = SearchListviewAlphaSelect()
        result5 = SearchMinAnimate()
        result6 = SearchDragFullWindows()
        result7 = SearchEnableAeroPeek()
        result8 = SearchFontSmoothing()
        result9 = SearchVisualFXSetting()
        result10 = SearchVisualFXSetting2()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9 and result10 == STATUS_DISABLED:
            self.labelAppearance.setText(STATUS_DISABLED)
            self.labelAppearance.setStyleSheet('color:green')
        else:
            self.labelAppearance.setText(STATUS_ENABLED)
            self.labelAppearance.setStyleSheet('color:red')

    def Appearance_clicked(self):
        result1 = SearchTaskbarAnimations()
        result2 = SearchIconsOnly()
        result3 = SearchListviewShadow()
        result4 = SearchListviewAlphaSelect()
        result5 = SearchMinAnimate()
        result6 = SearchDragFullWindows()
        result7 = SearchEnableAeroPeek()
        result8 = SearchFontSmoothing()
        result9 = SearchVisualFXSetting()
        result10 = SearchVisualFXSetting2()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9 and result10 == STATUS_DISABLED:
            TaskbarAnimationsOn()
            IconsOnlyOn()
            ListviewShadowOn()
            ListviewAlphaSelectOn()
            MinAnimateOn()
            DragFullWindowsOn()
            EnableAeroPeekOn()
            FontSmoothingOn()
            VisualFXSettingOn()
            VisualFXSettingOn2()
        else:
            TaskbarAnimationsOff()
            IconsOnlyOff()
            ListviewShadowOff()
            ListviewAlphaSelectOff()
            MinAnimateOff()
            DragFullWindowsOff()
            EnableAeroPeekOff()
            FontSmoothingOff()
            VisualFXSettingOff()
            VisualFXSettingOff2()
        self.updateAppearance()
    def updateGameBar(self):
        result1 = SearchAutoGameModeEnabled()
        result2 = SearchGamePanelStartupTipIndex()
        result3 = SearchShowStartupPanel()
        result4 = SearchUseNexusForGameBarEnabled()
        result5 = SearchAllowAutoGameMode()
        result6 = SearchAllowGameDVR()
        result7 = SearchAppCaptureEnabled()
        result8 = SearchValueGameBar()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 == STATUS_DISABLED:
            self.labelGameBar.setText(STATUS_DISABLED)
            self.labelGameBar.setStyleSheet('color:green')
        else:
            self.labelGameBar.setText(STATUS_ENABLED)
            self.labelGameBar.setStyleSheet('color:red')

    def GameBar_clicked(self):
        result1 = SearchAutoGameModeEnabled()
        result2 = SearchGamePanelStartupTipIndex()
        result3 = SearchShowStartupPanel()
        result4 = SearchUseNexusForGameBarEnabled()
        result5 = SearchAllowAutoGameMode()
        result6 = SearchAllowGameDVR()
        result7 = SearchAppCaptureEnabled()
        result8 = SearchValueGameBar()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 == STATUS_DISABLED:
            AutoGameModeEnabledOn()
            GamePanelStartupTipIndexOn()
            ShowStartupPanelOn()
            UseNexusForGameBarEnabledOn()
            AllowAutoGameModeOn()
            AllowGameDVROn()
            AppCaptureEnabledOn()
            ValueGameBarOn()
        else:
            AutoGameModeEnabledOff()
            GamePanelStartupTipIndexOff()
            ShowStartupPanelOff()
            UseNexusForGameBarEnabledOff()
            AllowAutoGameModeOff()
            AllowGameDVROff()
            AppCaptureEnabledOff()
            ValueGameBarOff()
        self.updateGameBar()

    def updateMultyPlanOverplay(self):
        result = SearchOverlayTestMode()
        if result == STATUS_DISABLED:
            self.labelMultyPlanOverplay.setText(STATUS_DISABLED)
            self.labelMultyPlanOverplay.setStyleSheet('color:green')
        else:
            self.labelMultyPlanOverplay.setText(STATUS_ENABLED)
            self.labelMultyPlanOverplay.setStyleSheet('color:red')

    def MultyPlanOverplay_clicked(self):
        result = SearchOverlayTestMode()
        if result == STATUS_DISABLED:
            OverlayTestModeOn()
        else:
            OverlayTestModeOff()
        self.updateMultyPlanOverplay()

    def updateWindowsFirewall(self):
        result1 = SearchEnableFirewall()
        result2 = SearchEnableFirewall2()
        if result1 and result2 == STATUS_DISABLED:
            self.labelWindowsFirewall.setText(STATUS_DISABLED)
            self.labelWindowsFirewall.setStyleSheet('color:green')
        else:
            self.labelWindowsFirewall.setText(STATUS_ENABLED)
            self.labelWindowsFirewall.setStyleSheet('color:red')

    def WindowsFirewall_clicked(self):
        result1 = SearchEnableFirewall()
        result2 = SearchEnableFirewall2()
        if result1 and result2 == STATUS_DISABLED:
            EnableFirewallOn()
            EnableFirewall2On()
        else:
            EnableFirewallOff()
            EnableFirewall2Off()
        self.updateWindowsFirewall()

    def updateWindowsUAC(self):
        result1 = SearchPromptOnSecureDesktop()
        result2 = SearchConsentPromptBehaviorAdmin()
        if result1 and result2 == STATUS_DISABLED:
            self.labelWindowsUAC.setText(STATUS_DISABLED)
            self.labelWindowsUAC.setStyleSheet('color:green')
        else:
            self.labelWindowsUAC.setText(STATUS_ENABLED)
            self.labelWindowsUAC.setStyleSheet('color:red')

    def WindowsUAC_clicked(self):
        result1 = SearchPromptOnSecureDesktop()
        result2 = SearchConsentPromptBehaviorAdmin()
        if result1 and result2 == STATUS_DISABLED:
            PromptOnSecureDesktopOn()
            ConsentPromptBehaviorAdminOn()
        else:
            PromptOnSecureDesktopOff()
            ConsentPromptBehaviorAdminOff()
        self.updateWindowsUAC()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = BaseSet()
    energy_window.show()
    sys.exit(app.exec())
