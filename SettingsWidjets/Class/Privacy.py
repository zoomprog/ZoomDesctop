import sys
from PyQt6.QtWidgets import QDialog, QApplication
from SettingsWidjets.Privacy import Ui_WindowsPrivacy

from Functions.Privacy.Telemetria.Telemetria import Start1On, Start1Off, Start2On, Start2Off, Start3On, Start3Off, Start4On, Start4Off, SearchStart1, SearchStart2, SearchStart3, SearchStart4
from Functions.Privacy.TelemetriaWebCome.TelemetriaWebCome import enable_task_schtasks, disable_task_schtasks, check_task_status, SetEmptyDebuggerOn, SetEmptyDebuggerOff, SearchSetEmptyDebugger
from Functions.Privacy.TaskMCA.TaskMCA import enable_TaskMCA_CompatibilityAppraiser, disable_TaskMCA_CompatibilityAppraiser, check_TaskMCA_status_CompatibilityAppraiser
from Functions.Privacy.UpdateDateCEIP.UpdateDateCEIP import check_ProgramDataUpdater, enable_ProgramDataUpdater, disable_ProgramDataUpdater
from Functions.Privacy.TaskApplicationImpactTelemetry.TaskApplicationImpactTelemetry import check_ait_agent_task, enable_ait_agent_task, disable_ait_agent_task
from Functions.Privacy.ProductivityAppReminder.ProductivityAppReminder import check_StartupAppTask, enable_StartupAppTask, disable_StartupAppTask
from Functions.Privacy.TaskCEIP.TaskCEIP import check_Proxy, enable_Proxy, disable_Proxy, check_BthSQM, enable_BthSQM, disable_BthSQM, check_Consolidator, enable_Consolidator, disable_Consolidator, check_KernelCeipTask, enable_KernelCeipTask, disable_KernelCeipTask, check_UsbCeip, enable_UsbCeip, disable_UsbCeip
from Functions.Privacy.CEIPSQM.CEIPSQM import CEIPSQMOn, CEIPSQMOff, SearchCEIPSQM
from Functions.Privacy.TelemetrApplicationImpact.TelemetrApplicationImpact import AITEnableOn, AITEnableOff, SearchAITEnable
from Functions.Privacy.TelemetrNalogDate.TelemetrNalogDate import AllowTelemetryOn, AllowTelemetryOff, SearchAllowTelemetry, AllowTelemetry2On, AllowTelemetry2Off, SearchAllowTelemetry2, AllowTelemetry3On, AllowTelemetry3Off, SearchAllowTelemetry3, LimitEnhancedDiagnosticDataWindowsAnalyticsOn, LimitEnhancedDiagnosticDataWindowsAnalyticsOff, SearchLimitEnhancedDiagnosticDataWindowsAnalytics
from Functions.Privacy.TelemetrLicense.TelemetrLicense import NoGenTicketOn, NoGenTicketOff, SearchNoGenTicket
from Functions.Privacy.WER.WER import DisabledOn, DisabledOff, SearchDisabled, Disabled2On, Disabled2Off, SearchDisabled2, DefaultConsentOn, DefaultConsentOff, SearchDefaultConsent, DefaultOverrideBehaviorOn, DefaultOverrideBehaviorOff, SearchDefaultOverrideBehavior, DontSendAdditionalDataOn, DontSendAdditionalDataOff, SearchDontSendAdditionalData, LoggingDisabledOn, LoggingDisabledOff, \
    SearchLoggingDisabled, StartWEROn, StartWEROff, SearchStartWER, StartWER2On, StartWER2Off, SearchStartWER2, check_QueueReporting, enable_QueueReporting, disable_QueueReporting
from Functions.Privacy.ActiveVoiceForCortan.ActiveVoiceForCortan import AgentActivationEnabledOn, AgentActivationEnabledOff, SearchAgentActivationEnabled, LetAppsActivateWithVoiceOn, LetAppsActivateWithVoiceOff, SearchLetAppsActivateWithVoice, check_ProgramDataUpdater, enable_ProgramDataUpdater, disable_ProgramDataUpdater
from Functions.Privacy.ActiveVoiceForCortanBlockSystem.ActiveVoiceForCortanBlockSystem import AgentActivationOnLockScreenEnabledOn, AgentActivationOnLockScreenEnabledOff, SearchAgentActivationOnLockScreenEnabled, LetAppsActivateWithVoiceAboveLockOn, LetAppsActivateWithVoiceAboveLockOff, SearchLetAppsActivateWithVoiceAboveLock
from Functions.Privacy.WindowsLocationProvider.WindowsLocationProvider import DisableWindowsLocationProviderOn, DisableWindowsLocationProviderOff, SearchDisableWindowsLocationProvider, DisableLocationScriptingOn, DisableLocationScriptingOff, SearchDisableLocationScripting, DisableLocationOn, DisableLocationOff, SearchDisableLocation, SensorPermissionStateOn, SensorPermissionStateOff, \
    SearchSensorPermissionState, SensorPermissionState2On, SensorPermissionState2Off, SearchSensorPermissionState2
from Functions.Privacy.AllowIndexingEncryptedStoresOrItems.AllowIndexingEncryptedStoresOrItems import DAllowIndexingEncryptedStoresOrItemsOn, AllowIndexingEncryptedStoresOrItemsOff, SearchAllowIndexingEncryptedStoresOrItems, AlwaysUseAutoLangDetectionOn, AlwaysUseAutoLangDetectionOff, SearchAlwaysUseAutoLangDetection, AllowSearchToUseLocationOn, AllowSearchToUseLocationOff, \
    SearchAllowSearchToUseLocation, DisableWebSearch1On, DisableWebSearch1Off, SearchDisableWebSearch1, ConnectedSearchUseWebOn, ConnectedSearchUseWebOff, SearchConnectedSearchUseWeb, BingSearchEnabledOn, BingSearchEnabledOff, SearchBingSearchEnabled
from Functions.Privacy.TargetedAdverisingAndMarketing.TargetedAdverisingAndMarketing import SubscribedContent338393EnabledOn, SubscribedContent338393EnabledOff, SearchSubscribedContent338393Enabled, SubscribedContent353694EnabledOn, SubscribedContent353694EnabledOff, SearchSubscribedContent353694Enabled, SubscribedContent353696EnabledOn, SubscribedContent353696EnabledOff, SearchSubscribedContent353696Enabled, DisableSoftLandingOn, DisableSoftLandingOff, SearchDisableSoftLanding, DisableWindowsSpotlightFeaturesOn, DisableWindowsSpotlightFeaturesOff, SearchDisableWindowsSpotlightFeatures, DisableWindowsConsumerFeaturesOn, DisableWindowsConsumerFeaturesOff, SearchDisableWindowsConsumerFeatures
from Functions.Privacy.CloudSaving.CloudSaving import DisableSettingSyncOn, DisableSettingSyncOff, SearchDisableSettingSync, DisableSettingSyncUserOverrideOn, DisableSettingSyncUserOverrideOff, SearchDisableSettingSyncUserOverride, DisableSyncOnPaidNetworkOn, DisableSyncOnPaidNetworkOff, SearchDisableSyncOnPaidNetwork, SyncPolicyOn, SyncPolicyOff, SearchSyncPolicy, DisableApplicationSettingSyncOn, DisableApplicationSettingSyncOff, SearchDisableApplicationSettingSync, DisableApplicationSettingSyncUserOverrideOn, DisableApplicationSettingSyncUserOverrideOff, SearchDisableApplicationSettingSyncUserOverride, DisableAppSyncSettingSyncOn, DisableAppSyncSettingSyncOff, SearchDisableAppSyncSettingSync, DisableAppSyncSettingSyncUserOverrideOn, DisableAppSyncSettingSyncUserOverrideOff, SearchDisableAppSyncSettingSyncUserOverride
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
        self.updateTelemetriaWebCome()
        self.uodateTaskMCA()
        self.updateUpdateDateCEIP()
        self.updateTaskApplicationImpactTelemetry()
        self.uodateProductivityAppReminder()
        self.updateTaskCEIP()
        self.updateCEIPSQM()
        self.updateTelemetrApplicationImpact()
        self.updateTelemetrNalogDate()
        self.updateTelemetrLicense()
        self.updateWer()
        self.updateActiveVoiceForCortan()
        self.updateActiveVoiceForCortanBlockSystem()
        self.updateWindowsLocationProvider()
        self.updateAllowIndexingEncryptedStoresOrItems()
        self.updateTargetedAdverisingAndMarketing()
        self.updateCloudSaving()

        self.pushTelemetria.clicked.connect(self.TelemetriaButtonClick)
        self.pushTelemetriaWebCome.clicked.connect(self.TelemetriaWebComeButtonClick)
        self.pushTaskMCA.clicked.connect(self.TaskMCAButtonClick)
        self.pushUpdateDateCEIP.clicked.connect(self.UpdateDateCEIPButtonClick)
        self.pushTaskApplicationImpactTelemetry.clicked.connect(self.TaskApplicationImpactTelemetryButtonClick)
        self.pushProductivityAppReminder.clicked.connect(self.ProductivityAppReminderButtonClick)
        self.pushTaskCEIP.clicked.connect(self.TaskCEIPButtonClick)
        self.pushCEIPSQM.clicked.connect(self.CEIPSQMButtonClick)
        self.pushTelemetrApplicationImpact.clicked.connect(self.TelemetrApplicationImpactButtonClick)
        self.pushTelemetrNalogDate.clicked.connect(self.TelemetrNalogDateButtonClick)
        self.pushTelemetrLicense.clicked.connect(self.TelemetrLicenseButtonClick)
        self.pushWER.clicked.connect(self.WERButtonClick)
        self.pushActiveVoiceForCortan.clicked.connect(self.ActiveVoiceForCortanButtonClick)
        self.pushActiveVoiceForCortanBlockSystem.clicked.connect(self.ActiveVoiceForCortanBlockSystemButtonClick)
        self.pushWindowsLocationProvider.clicked.connect(self.WindowsLocationProviderButtonClick)
        self.pushWindowsSearchDateCollection.clicked.connect(self.WindowsSearchDateCollectionButtonClick)
        self.pushTargetedAdverisingAndMarketing.clicked.connect(self.TargetedAdverisingAndMarketingButtonClick)
        self.pushCloudSaving.clicked.connect(self.CloudSavingButtonClick)

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

    def updateTelemetriaWebCome(self):
        result1 = SearchSetEmptyDebugger()
        result2 = check_task_status()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
            self.labelTelemetriaWebCome.setText(STATUS_DISABLED)
            self.labelTelemetriaWebCome.setStyleSheet('color:green')
        else:
            self.labelTelemetriaWebCome.setText(STATUS_ENABLED)
            self.labelTelemetriaWebCome.setStyleSheet('color:red')

    def TelemetriaWebComeButtonClick(self):
        result1 = SearchSetEmptyDebugger()
        result2 = check_task_status()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
            enable_task_schtasks()
            SetEmptyDebuggerOff()
        else:
            disable_task_schtasks()
            SetEmptyDebuggerOn()
        self.updateTelemetriaWebCome()

    def uodateTaskMCA(self):
        result1 = check_TaskMCA_status_CompatibilityAppraiser()
        result2 = SearchSetEmptyDebugger()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
            self.labelClearTaskMCA.setText(STATUS_DISABLED)
            self.labelClearTaskMCA.setStyleSheet('color:green')
        else:
            self.labelClearTaskMCA.setText(STATUS_ENABLED)
            self.labelClearTaskMCA.setStyleSheet('color:red')

    def TaskMCAButtonClick(self):
        result1 = check_TaskMCA_status_CompatibilityAppraiser()
        result2 = SearchSetEmptyDebugger()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
            enable_TaskMCA_CompatibilityAppraiser()
            SetEmptyDebuggerOff()
        else:
            disable_TaskMCA_CompatibilityAppraiser()
            SetEmptyDebuggerOn()
        self.uodateTaskMCA()

    def updateUpdateDateCEIP(self):
        result = check_ProgramDataUpdater()
        if result == STATUS_DISABLED:
            self.labelUpdateDateCEIP.setText(STATUS_DISABLED)
            self.labelUpdateDateCEIP.setStyleSheet('color:green')
        else:
            self.labelUpdateDateCEIP.setText(STATUS_ENABLED)
            self.labelUpdateDateCEIP.setStyleSheet('color:red')

    def UpdateDateCEIPButtonClick(self):
        result = check_ProgramDataUpdater()
        if result == STATUS_DISABLED:
            enable_ProgramDataUpdater()
        else:
            disable_ProgramDataUpdater()
        self.updateUpdateDateCEIP()

    def updateTaskApplicationImpactTelemetry(self):
        result = check_ait_agent_task()
        if result == STATUS_DISABLED:
            self.labelTaskApplicationImpactTelemetry.setText(STATUS_DISABLED)
            self.labelTaskApplicationImpactTelemetry.setStyleSheet('color:green')
        else:
            self.labelTaskApplicationImpactTelemetry.setText(STATUS_ENABLED)
            self.labelTaskApplicationImpactTelemetry.setStyleSheet('color:red')

    def TaskApplicationImpactTelemetryButtonClick(self):
        result = check_ait_agent_task()
        if result == STATUS_DISABLED:
            enable_ait_agent_task()
        else:
            disable_ait_agent_task()
        self.updateTaskApplicationImpactTelemetry()

    def uodateProductivityAppReminder(self):
        result = check_StartupAppTask()
        if result == STATUS_DISABLED:
            self.labelProductivityAppReminder.setText(STATUS_DISABLED)
            self.labelProductivityAppReminder.setStyleSheet('color:green')
        else:
            self.labelProductivityAppReminder.setText(STATUS_ENABLED)
            self.labelProductivityAppReminder.setStyleSheet('color:red')

    def ProductivityAppReminderButtonClick(self):
        result = check_StartupAppTask()
        if result == STATUS_DISABLED:
            enable_StartupAppTask()
        else:
            disable_StartupAppTask()
        self.uodateProductivityAppReminder()

    def updateTaskCEIP(self):
        result1 = check_Proxy()
        result2 = check_BthSQM()
        result3 = check_Consolidator()
        result4 = check_KernelCeipTask()
        result5 = check_UsbCeip()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED:
            self.labelTaskCEIP.setText(STATUS_DISABLED)
            self.labelTaskCEIP.setStyleSheet('color:green')
        else:
            self.labelTaskCEIP.setText(STATUS_ENABLED)
            self.labelTaskCEIP.setStyleSheet('color:red')

    def TaskCEIPButtonClick(self):
        result1 = check_Proxy()
        result2 = check_BthSQM()
        result3 = check_Consolidator()
        result4 = check_KernelCeipTask()
        result5 = check_UsbCeip()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED:
            enable_Proxy()
            enable_BthSQM()
            enable_Consolidator()
            enable_KernelCeipTask()
            enable_UsbCeip()
        else:
            disable_Proxy()
            disable_BthSQM()
            disable_Consolidator()
            disable_KernelCeipTask()
            disable_UsbCeip()
        self.updateTaskCEIP()

    def updateCEIPSQM(self):
        result = SearchCEIPSQM()
        if result == STATUS_DISABLED:
            self.labelCEIPSQM.setText(STATUS_DISABLED)
            self.labelCEIPSQM.setStyleSheet('color:green')
        else:
            self.labelCEIPSQM.setText(STATUS_ENABLED)
            self.labelCEIPSQM.setStyleSheet('color:red')

    def CEIPSQMButtonClick(self):
        result = SearchCEIPSQM()
        if result == STATUS_DISABLED:
            CEIPSQMOn()
        else:
            CEIPSQMOff()
        self.updateCEIPSQM()

    def updateTelemetrApplicationImpact(self):
        result = SearchAITEnable()
        if result == STATUS_DISABLED:
            self.labelTelemetrApplicationImpact.setText(STATUS_DISABLED)
            self.labelTelemetrApplicationImpact.setStyleSheet('color:green')
        else:
            self.labelTelemetrApplicationImpact.setText(STATUS_ENABLED)
            self.labelTelemetrApplicationImpact.setStyleSheet('color:red')

    def TelemetrApplicationImpactButtonClick(self):
        result = SearchAITEnable()
        if result == STATUS_DISABLED:
            AITEnableOn()
        else:
            AITEnableOff()
        self.updateTelemetrApplicationImpact()

    def updateTelemetrNalogDate(self):
        result1 = SearchAllowTelemetry()
        result2 = SearchAllowTelemetry2()
        result3 = SearchAllowTelemetry3()
        result4 = SearchLimitEnhancedDiagnosticDataWindowsAnalytics()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
            self.labelTelemetrNalogDate.setText(STATUS_DISABLED)
            self.labelTelemetrNalogDate.setStyleSheet('color:green')
        else:
            self.labelTelemetrNalogDate.setText(STATUS_ENABLED)
            self.labelTelemetrNalogDate.setStyleSheet('color:red')

    def TelemetrNalogDateButtonClick(self):
        result1 = SearchAllowTelemetry()
        result2 = SearchAllowTelemetry2()
        result3 = SearchAllowTelemetry3()
        result4 = SearchLimitEnhancedDiagnosticDataWindowsAnalytics()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
            LimitEnhancedDiagnosticDataWindowsAnalyticsOn()
            AllowTelemetry3On()
            AllowTelemetry2On()
            AllowTelemetryOn()
        else:
            LimitEnhancedDiagnosticDataWindowsAnalyticsOff()
            AllowTelemetry3Off()
            AllowTelemetry2Off()
            AllowTelemetryOff()
        self.updateTelemetrNalogDate()

    def updateTelemetrLicense(self):
        result = SearchNoGenTicket()
        if result == STATUS_DISABLED:
            self.labelTelemetrLicense.setText(STATUS_DISABLED)
            self.labelTelemetrLicense.setStyleSheet('color:green')
        else:
            self.labelTelemetrLicense.setText(STATUS_ENABLED)
            self.labelTelemetrLicense.setStyleSheet('color:red')

    def TelemetrLicenseButtonClick(self):
        result = SearchNoGenTicket()
        if result == STATUS_DISABLED:
            NoGenTicketOn()
        else:
            NoGenTicketOff()
        self.updateTelemetrLicense()

    def updateWer(self):
        result1 = SearchDisabled()
        result2 = SearchDisabled2()
        result3 = SearchDefaultConsent()
        result4 = SearchDefaultOverrideBehavior()
        result5 = SearchDontSendAdditionalData()
        result6 = SearchLoggingDisabled()
        result7 = SearchStartWER()
        result8 = SearchStartWER2()
        result9 = check_QueueReporting()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED and result6 == STATUS_DISABLED and result6 == STATUS_DISABLED and result7 == STATUS_DISABLED and result8 == STATUS_DISABLED and result9 == STATUS_DISABLED:
            self.labelWER.setText(STATUS_DISABLED)
            self.labelWER.setStyleSheet('color:green')
        else:
            self.labelWER.setText(STATUS_ENABLED)
            self.labelWER.setStyleSheet('color:red')

    def WERButtonClick(self):

        result1 = SearchDisabled()
        result2 = SearchDisabled2()
        result3 = SearchDefaultConsent()
        result4 = SearchDefaultOverrideBehavior()
        result5 = SearchDontSendAdditionalData()
        result6 = SearchLoggingDisabled()
        result7 = SearchStartWER()
        result8 = SearchStartWER2()
        result9 = check_QueueReporting()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED and result6 == STATUS_DISABLED and result7 == STATUS_DISABLED and result8 == STATUS_DISABLED and result9 == STATUS_DISABLED:
            DisabledOn()
            Disabled2On()
            DefaultConsentOn()
            DefaultOverrideBehaviorOn()
            DontSendAdditionalDataOn()
            DontSendAdditionalDataOn()
            LoggingDisabledOn()
            StartWEROn()
            StartWER2On()
            enable_QueueReporting()
        else:
            DisabledOff()
            Disabled2Off()
            DefaultConsentOff()
            DefaultOverrideBehaviorOff()
            DefaultOverrideBehaviorOff()
            DontSendAdditionalDataOff()
            LoggingDisabledOff()
            StartWEROff()
            StartWER2Off()
            disable_QueueReporting()
        self.updateWer()

    def updateActiveVoiceForCortan(self):
        result1 = SearchAgentActivationEnabled()
        result2 = SearchLetAppsActivateWithVoice()
        result3 = check_ProgramDataUpdater()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED:
            self.labelActiveVoiceForCortan.setText(STATUS_DISABLED)
            self.labelActiveVoiceForCortan.setStyleSheet('color:green')
        else:
            self.labelActiveVoiceForCortan.setText(STATUS_ENABLED)
            self.labelActiveVoiceForCortan.setStyleSheet('color:red')

    def ActiveVoiceForCortanButtonClick(self):
        result1 = SearchAgentActivationEnabled()
        result2 = SearchLetAppsActivateWithVoice()
        result3 = check_ProgramDataUpdater()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED:
            AgentActivationEnabledOn()
            LetAppsActivateWithVoiceOn()
            enable_ProgramDataUpdater()
        else:
            AgentActivationEnabledOff()
            LetAppsActivateWithVoiceOff()
            disable_ProgramDataUpdater()
        self.updateActiveVoiceForCortan()

    def updateActiveVoiceForCortanBlockSystem(self):
        result1 = SearchAgentActivationOnLockScreenEnabled()
        result2 = SearchLetAppsActivateWithVoiceAboveLock()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
            self.labelActiveVoiceForCortanBlockSystem.setText(STATUS_DISABLED)
            self.labelActiveVoiceForCortanBlockSystem.setStyleSheet('color:green')
        else:
            self.labelActiveVoiceForCortanBlockSystem.setText(STATUS_ENABLED)
            self.labelActiveVoiceForCortanBlockSystem.setStyleSheet('color:red')

    def ActiveVoiceForCortanBlockSystemButtonClick(self):
        result1 = SearchAgentActivationOnLockScreenEnabled()
        result2 = SearchLetAppsActivateWithVoiceAboveLock()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
            AgentActivationOnLockScreenEnabledOn()
            LetAppsActivateWithVoiceAboveLockOn()
        else:
            AgentActivationOnLockScreenEnabledOff()
            LetAppsActivateWithVoiceAboveLockOff()
        self.updateActiveVoiceForCortanBlockSystem()

    def updateWindowsLocationProvider(self):
        result1 = SearchDisableWindowsLocationProvider()
        result2 = SearchDisableLocationScripting()
        result3 = SearchDisableLocation()
        result4 = SearchSensorPermissionState()
        result5 = SearchSensorPermissionState2()
        if result5 == STATUS_DISABLED and result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
            self.labelWindowsLocationProvider.setText(STATUS_DISABLED)
            self.labelWindowsLocationProvider.setStyleSheet('color:green')
        else:
            self.labelWindowsLocationProvider.setText(STATUS_ENABLED)
            self.labelWindowsLocationProvider.setStyleSheet('color:red')

    def WindowsLocationProviderButtonClick(self):
        result1 = SearchDisableWindowsLocationProvider()
        result2 = SearchDisableLocationScripting()
        result3 = SearchDisableLocation()
        result4 = SearchSensorPermissionState()
        result5 = SearchSensorPermissionState2()
        if result5 == STATUS_DISABLED and result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
            DisableWindowsLocationProviderOn()
            DisableLocationScriptingOn()
            DisableLocationOn()
            SensorPermissionStateOn()
            SensorPermissionState2On()

        else:
            DisableWindowsLocationProviderOff()
            DisableLocationScriptingOff()
            DisableLocationOff()
            SensorPermissionStateOff()
            SensorPermissionState2Off()
        self.updateWindowsLocationProvider()

    def updateAllowIndexingEncryptedStoresOrItems(self):
        result1 = SearchAllowIndexingEncryptedStoresOrItems()
        result2 = SearchAlwaysUseAutoLangDetection()
        result3 = SearchAllowSearchToUseLocation()
        result4 = SearchDisableWebSearch1()
        result5 = SearchConnectedSearchUseWeb()
        result6 = SearchBingSearchEnabled()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED and result6 == STATUS_DISABLED:
            self.labelWindowsSearchDateCollection.setText(STATUS_DISABLED)
            self.labelWindowsSearchDateCollection.setStyleSheet('color:green')
        else:
            self.labelWindowsSearchDateCollection.setText(STATUS_ENABLED)
            self.labelWindowsSearchDateCollection.setStyleSheet('color:red')

    def WindowsSearchDateCollectionButtonClick(self):
        result1 = SearchAllowIndexingEncryptedStoresOrItems()
        result2 = SearchAlwaysUseAutoLangDetection()
        result3 = SearchAllowSearchToUseLocation()
        result4 = SearchDisableWebSearch1()
        result5 = SearchConnectedSearchUseWeb()
        result6 = SearchBingSearchEnabled()
        if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED and result6 == STATUS_DISABLED:
            DAllowIndexingEncryptedStoresOrItemsOn()
            AlwaysUseAutoLangDetectionOn()
            AllowSearchToUseLocationOn()
            DisableWebSearch1On()
            ConnectedSearchUseWebOn()
            BingSearchEnabledOn()
        else:
            AllowIndexingEncryptedStoresOrItemsOff()
            AlwaysUseAutoLangDetectionOff()
            AllowSearchToUseLocationOff()
            DisableWebSearch1Off()
            ConnectedSearchUseWebOff()
            BingSearchEnabledOff()
        self.updateAllowIndexingEncryptedStoresOrItems()

    def updateTargetedAdverisingAndMarketing(self):
        result1 = SearchSubscribedContent338393Enabled()
        result2 = SearchSubscribedContent353694Enabled()
        result3 = SearchSubscribedContent353696Enabled()
        result4 = SearchDisableSoftLanding()
        result5 = SearchDisableWindowsSpotlightFeatures()
        result6 = SearchDisableWindowsConsumerFeatures()
        print(result2)
        if result1 and result2 and result3 and result4 and result5 and result6 == STATUS_DISABLED:
            self.labelTargetedAdverisingAndMarketing.setText(STATUS_DISABLED)
            self.labelTargetedAdverisingAndMarketing.setStyleSheet('color:green')
        else:
            self.labelTargetedAdverisingAndMarketing.setText(STATUS_ENABLED)
            self.labelTargetedAdverisingAndMarketing.setStyleSheet('color:red')

    def TargetedAdverisingAndMarketingButtonClick(self):
        result1 = SearchSubscribedContent338393Enabled()
        result2 = SearchSubscribedContent353694Enabled()
        result3 = SearchSubscribedContent353696Enabled()
        result4 = SearchDisableSoftLanding()
        result5 = SearchDisableWindowsSpotlightFeatures()
        result6 = SearchDisableWindowsConsumerFeatures()
        print(result1, result2)
        if result1 and result2 and result3 and result4 and result5 and result6 == STATUS_DISABLED:
            SubscribedContent338393EnabledOn()
            SubscribedContent353694EnabledOn()
            SubscribedContent353696EnabledOn()
            DisableSoftLandingOn()
            DisableWindowsSpotlightFeaturesOn()
            DisableWindowsConsumerFeaturesOn()
        else:
            SubscribedContent338393EnabledOff()
            SubscribedContent353694EnabledOff()
            SubscribedContent353696EnabledOff()
            DisableSoftLandingOff()
            DisableWindowsSpotlightFeaturesOff()
            DisableWindowsConsumerFeaturesOff()
        self.updateTargetedAdverisingAndMarketing()

    def updateCloudSaving(self):
        result1 = SearchDisableSettingSync()
        result2 = SearchDisableSettingSyncUserOverride()
        result3 = SearchDisableSyncOnPaidNetwork()
        result4 = SearchSyncPolicy()
        result5 = SearchDisableApplicationSettingSync()
        result6 = SearchDisableApplicationSettingSyncUserOverride()
        result7 = SearchDisableAppSyncSettingSync()
        result8 = SearchDisableAppSyncSettingSyncUserOverride()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 == STATUS_DISABLED:
            self.labelCloudSaving.setText(STATUS_DISABLED)
            self.labelCloudSaving.setStyleSheet('color:green')
        else:
            self.labelCloudSaving.setText(STATUS_ENABLED)
            self.labelCloudSaving.setStyleSheet('color:red')

    def CloudSavingButtonClick(self):
        result1 = SearchDisableSettingSync()
        result2 = SearchDisableSettingSyncUserOverride()
        result3 = SearchDisableSyncOnPaidNetwork()
        result4 = SearchSyncPolicy()
        result5 = SearchDisableApplicationSettingSync()
        result6 = SearchDisableApplicationSettingSyncUserOverride()
        result7 = SearchDisableAppSyncSettingSync()
        result8 = SearchDisableAppSyncSettingSyncUserOverride()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 == STATUS_DISABLED:
            DisableSettingSyncOn()
            DisableSettingSyncUserOverrideOn()
            DisableSyncOnPaidNetworkOn()
            SyncPolicyOn()
            DisableApplicationSettingSyncOn()
            DisableApplicationSettingSyncUserOverrideOn()
            DisableAppSyncSettingSyncOn()
            DisableAppSyncSettingSyncUserOverrideOn()
        else:
            DisableSettingSyncOff()
            DisableSettingSyncUserOverrideOff()
            DisableSyncOnPaidNetworkOff()
            SyncPolicyOff()
            DisableApplicationSettingSyncOff()
            DisableApplicationSettingSyncUserOverrideOff()
            DisableAppSyncSettingSyncOff()
            DisableAppSyncSettingSyncUserOverrideOff()
        self.updateCloudSaving()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = WindowsPrivacy()
    energy_window.show()
    sys.exit(app.exec())
