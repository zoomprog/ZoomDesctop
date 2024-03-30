import sys
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.Privacy import Ui_WindowsPrivacy

from Functions.Privacy.Telemetria.Telemetria import Start1On, Start1Off, Start2On, Start2Off, Start3On, Start3Off, Start4On, Start4Off, SearchStart1, SearchStart2, SearchStart3, SearchStart4
from Functions.Privacy.TelemetriaWebCome.TelemetriaWebCome import *

from enum import Enum, auto


class SystemStatus(Enum):
    DISABLED = auto()
    ENABLED = auto()
    ERROR = auto()


# Constants for repeated strings
STATUS_DISABLED = "Disabled"
STATUS_ENABLED = "Enabled"
STATUS_ERROR = "Error"


class WindowsPrivacy(QDialog, Ui_WindowsPrivacy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.positionButton()
        self.positionTextLabel()

        self.updateTelemetria()
        #self.updateTelemetriaWebCome()
        self.pushTelemetria.clicked.connect(self.TelemetriaButtonClick)

    def positionButton(self):
        frame_list = [
            "pushTelemetria",
            "pushTelemetriaWebCome",
            "pushTaskMCA",
            "pushUpdateDateCEIP",
            "pushTaskApplicationImpactTelemetry",
            "pushProductivityAppReminder",
            "pushTaskCEIP",
            "pushCEIPSQM",
            "pushTaskCEIP",
            "pushTaskApplicationImpactTelemetry",
            "pushProductivityAppReminder",
            "pushTaskCEIP",
            "pushTelemetrApplicationImpact",
            "pushTelemetrNalogDate",
            "pushTelemetrLicense",
            "pushWER",
            "pushActiveVoiceForCortan",
            "pushActiveVoiceForCortanBlockSystem",
            "pushWindowsLocationProvider",
            "pushWindowsSearchDateCollection",
            "pushTargetedAdverisingAndMarketing",
            "pushCloudSaving",
            "pushCloudVoice",
            "pushWindowsPrivacyConsentDisclaimer",
            "pushWindowsFeedbackandDiagnostics",
            "pushCollectTextMessagesandHandwritingInput",
            "pushSensor",
            "pushWiFiSense",
            "pushHideMostUsedApps",
            "pushHideInventoryCollector",
            "pushSiteAccessToTheListOfLanguages",
            "pushRecordingActions",
            "pushFeedbackAsYouType",
            "pushActivityFeed",
            "pushApplicationAccessToLocation",
            "pushApplicationAccessToAccountInformation",
            "pushApplicationAccessToMotionData",
            "pushAppAccessToPhone",
            "pushApplicationAccessToTrustedDevices",
            "pushAppAccessToDeviceSynchronization",
            "pushSyncAppsWithWirelessDevices",
            "pushApplicationsAccessDiagnosticInformationAboutOtherApplications",
            "pushApplicationAccessToContacts",
            "pushApplicationAccessToCalendar",
            "pushApplicationAccessToCallLog",
            "pushApplicationAccessToEmail",
            "pushApplicationAccessToTasks",
            "pushApplicationAccessToMessages",
            "pushApplicationAccessToRadio",
            "pushAppAccessToBluetoothDevices",
            "pushApplicationAccessToTheDocumentsFolder",
            "pushApplicationAccessToThePicturesFolder",
            "pushApplicationAccessToTheVideosFolder",
            "pushApplicationAccessToAnotherFileSystem"
        ]
        x_position = 780
        # Loop through button names and set their position
        for button_name in frame_list:
            button = getattr(self, button_name)
            button.move(x_position, 7)

    def positionTextLabel(self):
        TextLabel_list = [
            "labelTelemetria",
            "labelTelemetriaWebCome",
            "labelClearTaskMCA",
            "labelUpdateDateCEIP",
            "labelTaskApplicationImpactTelemetry",
            "labelProductivityAppReminder",
            "labelTaskCEIP",
            "labelCEIPSQM",
            "labelTaskCEIP",
            "labelTaskApplicationImpactTelemetry",
            "labelProductivityAppReminder",
            "labelTaskCEIP",
            "labelTelemetrApplicationImpact",
            "labelTelemetrNalogDate",
            "labelTelemetrLicense",
            "labelWER",
            "labelActiveVoiceForCortan",
            "labelActiveVoiceForCortanBlockSystem",
            "labelWindowsLocationProvider",
            "labelWindowsSearchDateCollection",
            "labelTargetedAdverisingAndMarketing",
            "labelCloudSaving",
            "labelCloudVoice",
            "labelWindowsPrivacyConsentDisclaimer",
            "labelWindowsFeedbackandDiagnostics",
            "labelCollectTextMessagesandHandwritingInput",
            "labelSensor",
            "labelWiFiSense",
            "labelHideMostUsedApps",
            "labelInventoryCollector",
            "labelSiteAccessToTheListOfLanguages",
            "labelRecordingActions",
            "labelFeedbackAsYouType",
            "labelActivityFeed",
            "labelApplicationAccessToLocation",
            "labelApplicationAccessToAccountInformation",
            "labelApplicationAccessToMotionData",
            "labelAppAccessToPhone",
            "labelApplicationAccessToTrustedDevices",
            "labelAppAccessToDeviceSynchronization",
            "labelSyncAppsWithWirelessDevices",
            "labelApplicationsAccessDiagnosticInformationAboutOtherApplications",
            "labelApplicationAccessToContacts",
            "labelApplicationAccessToCalendar",
            "labelApplicationAccessToCallLog",
            "labelApplicationAccessToEmail",
            "labelApplicationAccessToTasks",
            "labelApplicationAccessToMessages",
            "labelApplicationAccessToRadio",
            "labelAppAccessToBluetoothDevices",
            "labelApplicationAccessToTheDocumentsFolder",
            "labelApplicationAccessToThePicturesFolder",
            "labelApplicationAccessToTheVideosFolder",
            "labelApplicationAccessToAnotherFileSystem"
        ]
        x_position = 600
        # Loop through button names and set their position
        for button_name in TextLabel_list:
            button = getattr(self, button_name)
            button.move(x_position, 7)

    def updateTelemetria(self):
        result1 = SearchStart1()
        result2 = SearchStart2()
        result3 = SearchStart3()
        result4 = SearchStart4()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
            self.labelTelemetria.setText('Disabled')
            self.labelTelemetria.setStyleSheet('color:green')
        else:
            self.labelTelemetria.setText('Enabled')
            self.labelTelemetria.setStyleSheet('color:red')

    def TelemetriaButtonClick(self):
        result1 = SearchStart1()
        result2 = SearchStart2()
        result3 = SearchStart3()
        result4 = SearchStart4()
        print(result1, result2, result3, result4)
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
            Start1On()
            Start2On()
            Start3On()
            Start4On()
        else:
            Start1Off()
            Start2Off()
            Start3Off()
            Start4Off()
        self.updateTelemetria()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = WindowsPrivacy()
    energy_window.show()
    sys.exit(app.exec())
