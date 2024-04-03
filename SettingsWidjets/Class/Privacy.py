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
from Functions.Privacy.TargetedAdverisingAndMarketing.TargetedAdverisingAndMarketing import (SubscribedContent338393EnabledOn, SubscribedContent338393EnabledOff, SearchSubscribedContent338393Enabled, SubscribedContent353694EnabledOn, SubscribedContent353694EnabledOff, SearchSubscribedContent353694Enabled, SubscribedContent353696EnabledOn, SubscribedContent353696EnabledOff,
                                                                                             SearchSubscribedContent353696Enabled, DisableSoftLandingOn, DisableSoftLandingOff, SearchDisableSoftLanding, DisableWindowsSpotlightFeaturesOn, DisableWindowsSpotlightFeaturesOff, SearchDisableWindowsSpotlightFeatures, DisableWindowsConsumerFeaturesOn, DisableWindowsConsumerFeaturesOff,
                                                                                             SearchDisableWindowsConsumerFeatures)
from Functions.Privacy.CloudSaving.CloudSaving import (DisableSettingSyncOn, DisableSettingSyncOff, SearchDisableSettingSync, DisableSettingSyncUserOverrideOn, DisableSettingSyncUserOverrideOff, SearchDisableSettingSyncUserOverride, DisableSyncOnPaidNetworkOn, DisableSyncOnPaidNetworkOff, SearchDisableSyncOnPaidNetwork, SyncPolicyOn, SyncPolicyOff, SearchSyncPolicy,
                                                       DisableApplicationSettingSyncOn, DisableApplicationSettingSyncOff, SearchDisableApplicationSettingSync, DisableApplicationSettingSyncUserOverrideOn, DisableApplicationSettingSyncUserOverrideOff, SearchDisableApplicationSettingSyncUserOverride, DisableAppSyncSettingSyncOn, DisableAppSyncSettingSyncOff, SearchDisableAppSyncSettingSync,
                                                       DisableAppSyncSettingSyncUserOverrideOn, DisableAppSyncSettingSyncUserOverrideOff, SearchDisableAppSyncSettingSyncUserOverride, DisableCredentialsSettingSyncOn, DisableCredentialsSettingSyncOff, SearchDisableCredentialsSettingSync, DisableCredentialsSettingSyncUserOverrideOn, DisableCredentialsSettingSyncUserOverrideOff,
                                                       SearchDisableCredentialsSettingSyncUserOverride, EnabledCloudSavingOn, EnabledCloudSavingOff, SearchEnabledCloudSaving, DisableDesktopThemeSettingSyncOn, DisableDesktopThemeSettingSyncOff, SearchDisableDesktopThemeSettingSync, DisableDesktopThemeSettingSyncUserOverrideOn, DisableDesktopThemeSettingSyncUserOverrideOff,
                                                       SearchDisableDesktopThemeSettingSyncUserOverride, DisablePersonalizationSettingSyncOn, DisablePersonalizationSettingSyncOff, SearchDisablePersonalizationSettingSync, DisablePersonalizationSettingSyncUserOverrideOn, DisablePersonalizationSettingSyncUserOverrideOff, SearchDisablePersonalizationSettingSyncUserOverride,
                                                       DisableStartLayoutSettingSyncOn, DisableStartLayoutSettingSyncOff, SearchDisableStartLayoutSettingSync, DisableStartLayoutSettingSyncUserOverrideOn, DisableStartLayoutSettingSyncUserOverrideOff, SearchDisableStartLayoutSettingSyncUserOverride, DisableWebBrowserSettingSyncOn, DisableWebBrowserSettingSyncOff,
                                                       SearchDisableWebBrowserSettingSync, DisableWebBrowserSettingSyncUserOverrideOn, DisableWebBrowserSettingSyncUserOverrideOff, SearchDisableWebBrowserSettingSyncUserOverride, DisableWindowsSettingSyncOn, DisableWindowsSettingSyncOff, SearchDisableWindowsSettingSync, DisableWindowsSettingSyncUserOverrideOn,
                                                       DisableWindowsSettingSyncUserOverrideOff, SearchDisableWindowsSettingSyncUserOverride, SearchEnabledLanguage, EnabledLanguageOn, EnabledLanguageOff)
from Functions.Privacy.CloudVoice.CloudVoice import HasAcceptedOn, HasAcceptedOff, SearchHasAccepted
from Functions.Privacy.WindowsPrivacyConsentDisclaimer.WindowsPrivacyConsentDisclaimer import AcceptedPrivacyPolicyOn, AcceptedPrivacyPolicyOff, SearchAcceptedPrivacyPolicy
from Functions.Privacy.WindowsFeedbackandDiagnostics.WindowsFeedbackandDiagnostics import (NumberOfSIUFInPeriodOn, NumberOfSIUFInPeriodOff, SearchNumberOfSIUFInPeriod, PeriodInNanoSecondsOn, PeriodInNanoSecondsOff, SearchPeriodInNanoSeconds, DoNotShowFeedbackNotificationsOn, DoNotShowFeedbackNotificationsOff, SearchDoNotShowFeedbackNotifications, DmClientOn, DmClientOff, SearchDmClient,
                                                                                           SearchDmClientOnScenarioDownload, DmClientOnScenarioDownloadOn, DmClientOnScenarioDownloadOff)
from Functions.Privacy.CollectTextMessagesandHandwritingInput.CollectTextMessagesandHandwritingInput import RestrictImplicitInkCollectionOn, RestrictImplicitInkCollectionOff, SearchRestrictImplicitInkCollection, RestrictImplicitTextCollectionOn, RestrictImplicitTextCollectionOff, SearchRestrictImplicitTextCollection, HarvestContactsOn, HarvestContactsOff, SearchHarvestContacts
from Functions.Privacy.Sensor.Sensor import DisableSensorsOn, DisableSensorsOff, SearchDisableSensors
from Functions.Privacy.WiFiSense.WiFiSense import value1On, value1Off, Searchvalue1, value2On, value2Off, Searchvalue2, AutoConnectAllowedOEMOn, AutoConnectAllowedOEMOff, SearchAutoConnectAllowedOEM
from Functions.Privacy.HideMostUsedApps.HideMostUsedApps import HideMostUsedAppsOn, HideMostUsedAppsOff, SearchHideMostUsedApps
from Functions.Privacy.InventoryCollector.InvenoryCollector import DisableInventoryOn, DisableInventoryOff, SearchDisableInventory, ICDeviceSearch, ICDeviceOn, ICDeviceOff, DeviceUserSearch, DeviceUserOn, DeviceUserOff
from Functions.Privacy.SiteAccessToTheListOfLanguages.SiteAccessToTheListOfLanguages import HttpAcceptLanguageOptOutOn, HttpAcceptLanguageOptOutOff, SearchHttpAcceptLanguageOptOut
from Functions.Privacy.RecordingActions.RecordingActions import HttpAcceptLanguageOptOutRAOn, HttpAcceptLanguageOptOutRAOff, SearchHttpAcceptLanguageOptOutRAOut
from Functions.Privacy.FeedbackAsYouType.FeedbackAsYouType import EnabledFAYTOn, EnabledFAYTOff, SearchEnabledFAYT
from Functions.Privacy.ActivityFeed.ActivityFeed import EnableActivityFeedOn, EnableActivityFeedOff, SearchEnableActivityFeed
from Functions.Privacy.ApplicationAccessToLocation.ApplicationAccessToLocation import ValueAATLOn, ValueAATLOff, SearchValueAATL, StatusAATLOn, StatusAATLOff, SearchStatusAATL, LetAppsAccessLocationOn, LetAppsAccessLocationOff, SearchLetAppsAccessLocation

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
        self.updateCloudVoice()
        self.updateWindowsSearchDateCollection()
        self.updateWindowsPrivacyConsentDisclaimer()
        self.updateCollectTextMessagesandHandwritingInput()
        self.updateSensor()
        self.updateWiFiSense()
        self.updateHideMostUsedApps()
        self.updateInventoryCollector()
        self.updateSiteAccessToTheListOfLanguages()
        self.updateRecordingActions()
        self.updateFeedbackAsYouType()
        self.updateActivityFeed()
        self.updateApplicationAccessToLocation()

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
        self.pushCloudVoice.clicked.connect(self.CloudVoiceButtonClick)
        self.pushWindowsPrivacyConsentDisclaimer.clicked.connect(self.WindowsPrivacyConsentDisclaimerButtonClick)
        self.pushWindowsFeedbackandDiagnostics.clicked.connect(self.WindowsFeedbackandDiagnosticsButtonClick)
        self.pushCollectTextMessagesandHandwritingInput.clicked.connect(self.CollectTextMessages)
        self.pushSensor.clicked.connect(self.SensorButtonClick)
        self.pushWiFiSense.clicked.connect(self.WiFiSenseButtonClick)
        self.pushHideMostUsedApps.clicked.connect(self.HideMostUsedAppsButtonClick)
        self.pushHideInventoryCollector.clicked.connect(self.HideInventoryCollectorButtonClick)
        self.pushSiteAccessToTheListOfLanguages.clicked.connect(self.SiteAccessToTheListOfLanguagesButtonClick)
        self.pushRecordingActions.clicked.connect(self.RecordingActionsButtonClick)
        self.pushFeedbackAsYouType.clicked.connect(self.FeedbackAsYouTypeButtonClick)
        self.pushActivityFeed.clicked.connect(self.ActivityFeedButtonClick)
        self.pushApplicationAccessToLocation.clicked.connect(self.ApplicationAccessToLocationButtonClick)

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
        result9 = SearchDisableCredentialsSettingSync()
        result10 = SearchDisableCredentialsSettingSyncUserOverride()
        result11 = SearchEnabledCloudSaving()
        result12 = SearchDisableDesktopThemeSettingSync()
        result13 = SearchDisableDesktopThemeSettingSyncUserOverride()
        result14 = SearchDisablePersonalizationSettingSync()
        result15 = SearchDisablePersonalizationSettingSyncUserOverride()
        result16 = SearchDisableStartLayoutSettingSync()
        result17 = SearchDisableStartLayoutSettingSyncUserOverride()
        result18 = SearchDisableWebBrowserSettingSync()
        result19 = SearchDisableWebBrowserSettingSyncUserOverride()
        result20 = SearchDisableWindowsSettingSync()
        result21 = SearchDisableWindowsSettingSyncUserOverride()
        result22 = SearchEnabledLanguage()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9 and result10 and result11 and result12 and result13 and result14 and result15 and result16 and result17 and result18 and result19 and result20 and result21 and result22 == STATUS_DISABLED:
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
        result9 = SearchDisableCredentialsSettingSync()
        result10 = SearchDisableCredentialsSettingSyncUserOverride()
        result11 = SearchEnabledCloudSaving()
        result12 = SearchDisableDesktopThemeSettingSync()
        result13 = SearchDisableDesktopThemeSettingSyncUserOverride()
        result14 = SearchDisablePersonalizationSettingSync()
        result15 = SearchDisablePersonalizationSettingSyncUserOverride()
        result16 = SearchDisableStartLayoutSettingSync()
        result17 = SearchDisableStartLayoutSettingSyncUserOverride()
        result18 = SearchDisableWebBrowserSettingSync()
        result19 = SearchDisableWebBrowserSettingSyncUserOverride()
        result20 = SearchDisableWindowsSettingSync()
        result21 = SearchDisableWindowsSettingSyncUserOverride()
        result22 = SearchEnabledLanguage()
        if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9 and result10 and result11 and result12 and result13 and result14 and result15 and result16 and result17 and result18 and result19 and result20 and result21 and result22 == STATUS_DISABLED:
            DisableSettingSyncOn()
            DisableSettingSyncUserOverrideOn()
            DisableSyncOnPaidNetworkOn()
            SyncPolicyOn()
            DisableApplicationSettingSyncOn()
            DisableApplicationSettingSyncUserOverrideOn()
            DisableAppSyncSettingSyncOn()
            DisableAppSyncSettingSyncUserOverrideOn()
            DisableCredentialsSettingSyncOn()
            DisableCredentialsSettingSyncUserOverrideOn()
            EnabledCloudSavingOn()
            DisableDesktopThemeSettingSyncOn()
            DisableDesktopThemeSettingSyncUserOverrideOn()
            DisablePersonalizationSettingSyncOn()
            DisablePersonalizationSettingSyncUserOverrideOn()
            DisableStartLayoutSettingSyncOn()
            DisableStartLayoutSettingSyncUserOverrideOn()
            DisableWebBrowserSettingSyncOn()
            DisableWebBrowserSettingSyncUserOverrideOn()
            DisableWindowsSettingSyncOn()
            DisableWindowsSettingSyncUserOverrideOn()
            EnabledLanguageOn()
        else:
            DisableSettingSyncOff()
            DisableSettingSyncUserOverrideOff()
            DisableSyncOnPaidNetworkOff()
            SyncPolicyOff()
            DisableApplicationSettingSyncOff()
            DisableApplicationSettingSyncUserOverrideOff()
            DisableAppSyncSettingSyncOff()
            DisableAppSyncSettingSyncUserOverrideOff()
            DisableCredentialsSettingSyncOff()
            DisableCredentialsSettingSyncUserOverrideOff()
            EnabledCloudSavingOff()
            DisableDesktopThemeSettingSyncOff()
            DisableDesktopThemeSettingSyncUserOverrideOff()
            DisablePersonalizationSettingSyncOff()
            DisablePersonalizationSettingSyncUserOverrideOff()
            DisableStartLayoutSettingSyncOff()
            DisableStartLayoutSettingSyncUserOverrideOff()
            DisableWebBrowserSettingSyncOff()
            DisableWebBrowserSettingSyncUserOverrideOff()
            DisableWindowsSettingSyncOff()
            DisableWindowsSettingSyncUserOverrideOff()
            EnabledLanguageOff()
        self.updateCloudSaving()

    def updateCloudVoice(self):
        result = SearchHasAccepted()
        if result == STATUS_DISABLED:
            self.labelCloudVoice.setText(STATUS_DISABLED)
            self.labelCloudVoice.setStyleSheet('color:green')
        else:
            self.labelCloudVoice.setText(STATUS_ENABLED)
            self.labelCloudVoice.setStyleSheet('color:red')

    def CloudVoiceButtonClick(self):
        result = SearchHasAccepted()
        if result == STATUS_DISABLED:
            HasAcceptedOn()
        else:
            HasAcceptedOff()
        self.updateCloudVoice()

    def updateWindowsSearchDateCollection(self):
        result = SearchAcceptedPrivacyPolicy()
        if result == STATUS_DISABLED:
            self.labelWindowsPrivacyConsentDisclaimer.setText(STATUS_DISABLED)
            self.labelWindowsPrivacyConsentDisclaimer.setStyleSheet('color:green')
        else:
            self.labelWindowsPrivacyConsentDisclaimer.setText(STATUS_ENABLED)
            self.labelWindowsPrivacyConsentDisclaimer.setStyleSheet('color:red')

    def WindowsPrivacyConsentDisclaimerButtonClick(self):
        result = SearchAcceptedPrivacyPolicy()
        if result == STATUS_DISABLED:
            AcceptedPrivacyPolicyOn()
        else:
            AcceptedPrivacyPolicyOff()
        self.updateWindowsSearchDateCollection()

    def updateWindowsPrivacyConsentDisclaimer(self):
        result1 = SearchNumberOfSIUFInPeriod()
        result2 = SearchPeriodInNanoSeconds()
        result3 = SearchDoNotShowFeedbackNotifications()
        result4 = SearchDmClient()
        result5 = SearchDmClientOnScenarioDownload()
        if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
            self.labelWindowsFeedbackandDiagnostics.setText(STATUS_DISABLED)
            self.labelWindowsFeedbackandDiagnostics.setStyleSheet('color:green')
        else:
            self.labelWindowsFeedbackandDiagnostics.setText(STATUS_ENABLED)
            self.labelWindowsFeedbackandDiagnostics.setStyleSheet('color:red')


    def WindowsFeedbackandDiagnosticsButtonClick(self):
        result1 = SearchNumberOfSIUFInPeriod()
        result2 = SearchPeriodInNanoSeconds()
        result3 = SearchDoNotShowFeedbackNotifications()
        result4 = SearchDmClient()
        result5 = SearchDmClientOnScenarioDownload()
        if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
            NumberOfSIUFInPeriodOn()
            PeriodInNanoSecondsOn()
            DoNotShowFeedbackNotificationsOn()
            DmClientOn()
            DmClientOnScenarioDownloadOn()
        else:
            NumberOfSIUFInPeriodOff()
            PeriodInNanoSecondsOff()
            DoNotShowFeedbackNotificationsOff()
            DmClientOff()
            DmClientOnScenarioDownloadOff()
        self.updateWindowsPrivacyConsentDisclaimer()

    def updateCollectTextMessagesandHandwritingInput(self):
        result1 = SearchRestrictImplicitInkCollection()
        result2 = SearchRestrictImplicitTextCollection()
        result3 = SearchHarvestContacts()
        if result1 and result2 and result3 == STATUS_DISABLED:
            self.labelCollectTextMessagesandHandwritingInput.setText(STATUS_DISABLED)
            self.labelCollectTextMessagesandHandwritingInput.setStyleSheet('color:green')
        else:
            self.labelCollectTextMessagesandHandwritingInput.setText(STATUS_ENABLED)
            self.labelCollectTextMessagesandHandwritingInput.setStyleSheet('color:red')

    def CollectTextMessages(self):
        result1 = SearchRestrictImplicitInkCollection()
        result2 = SearchRestrictImplicitTextCollection()
        result3 = SearchHarvestContacts()
        if result1 and result2 and result3 == STATUS_DISABLED:
            RestrictImplicitInkCollectionOn()
            RestrictImplicitTextCollectionOn()
            HarvestContactsOn()
        else:
            RestrictImplicitInkCollectionOff()
            RestrictImplicitTextCollectionOff()
            HarvestContactsOff()
        self.updateCollectTextMessagesandHandwritingInput()

    def updateSensor(self):
        result = SearchDisableSensors()
        if result == STATUS_DISABLED:
            self.labelSensor.setText(STATUS_DISABLED)
            self.labelSensor.setStyleSheet('color:green')
        else:
            self.labelSensor.setText(STATUS_ENABLED)
            self.labelSensor.setStyleSheet('color:red')

    def SensorButtonClick(self):
        result = SearchDisableSensors()
        if result == STATUS_DISABLED:
            DisableSensorsOn()
        else:
            DisableSensorsOff()
        self.updateSensor()

    def updateWiFiSense(self):
        result1 = Searchvalue1()
        result2 = Searchvalue2()
        result3 = SearchAutoConnectAllowedOEM()
        if result1 and result2 and result3 == STATUS_DISABLED:
            self.labelWiFiSense.setText(STATUS_DISABLED)
            self.labelWiFiSense.setStyleSheet('color:green')
        else:
            self.labelWiFiSense.setText(STATUS_ENABLED)
            self.labelWiFiSense.setStyleSheet('color:red')

    def WiFiSenseButtonClick(self):
        result1 = Searchvalue1()
        result2 = Searchvalue2()
        result3 = SearchAutoConnectAllowedOEM()
        if result1 and result2 and result3 == STATUS_DISABLED:
            value1On()
            value2On()
            AutoConnectAllowedOEMOn()
        else:
            value1Off()
            value2Off()
            AutoConnectAllowedOEMOff()
        self.updateWiFiSense()

    def updateHideMostUsedApps(self):
        result1 = SearchHideMostUsedApps()
        if result1 == STATUS_DISABLED:
            self.labelHideMostUsedApps.setText(STATUS_ENABLED)
            self.labelHideMostUsedApps.setStyleSheet('color:green')
        else:
            self.labelHideMostUsedApps.setText(STATUS_DISABLED)
            self.labelHideMostUsedApps.setStyleSheet('color:red')

    def HideMostUsedAppsButtonClick(self):
        result1 = SearchHideMostUsedApps()
        if result1 == STATUS_DISABLED:
            HideMostUsedAppsOn()
        else:
            HideMostUsedAppsOff()
        self.updateHideMostUsedApps()

    def updateInventoryCollector(self):
        result1 = SearchDisableInventory()
        result2 = ICDeviceSearch()
        result3 = DeviceUserSearch()
        if result1 and result2 and result3 == STATUS_DISABLED:
            self.labelInventoryCollector.setText(STATUS_DISABLED)
            self.labelInventoryCollector.setStyleSheet('color:green')
        else:
            self.labelInventoryCollector.setText(STATUS_ENABLED)
            self.labelInventoryCollector.setStyleSheet('color:red')

    def HideInventoryCollectorButtonClick(self):
        result1 = SearchDisableInventory()
        result2 = ICDeviceSearch()
        result3 = DeviceUserSearch()
        if result1 and result2 and result3 == STATUS_DISABLED:
            DisableInventoryOn()
            ICDeviceOn()
            DeviceUserOn()
        else:
            DisableInventoryOff()
            ICDeviceOff()
            DeviceUserOff()
        self.updateInventoryCollector()

    def updateSiteAccessToTheListOfLanguages(self):
        result = SearchHttpAcceptLanguageOptOut()
        if result == STATUS_DISABLED:
            self.labelSiteAccessToTheListOfLanguages.setText(STATUS_DISABLED)
            self.labelSiteAccessToTheListOfLanguages.setStyleSheet('color:green')
        else:
            self.labelSiteAccessToTheListOfLanguages.setText(STATUS_ENABLED)
            self.labelSiteAccessToTheListOfLanguages.setStyleSheet('color:red')

    def SiteAccessToTheListOfLanguagesButtonClick(self):
        result = SearchHttpAcceptLanguageOptOut()
        if result == STATUS_DISABLED:
            HttpAcceptLanguageOptOutOn()
        else:
            HttpAcceptLanguageOptOutOff()
        self.updateSiteAccessToTheListOfLanguages()

    def updateRecordingActions(self):
        result = SearchHttpAcceptLanguageOptOutRAOut()
        if result == STATUS_DISABLED:
            self.labelRecordingActions.setText(STATUS_DISABLED)
            self.labelRecordingActions.setStyleSheet('color:green')
        else:
            self.labelRecordingActions.setText(STATUS_ENABLED)
            self.labelRecordingActions.setStyleSheet('color:red')

    def RecordingActionsButtonClick(self):
        result = SearchHttpAcceptLanguageOptOutRAOut()
        if result == STATUS_DISABLED:
            HttpAcceptLanguageOptOutRAOn()
        else:
            HttpAcceptLanguageOptOutRAOff()
        self.updateRecordingActions()

    def updateFeedbackAsYouType(self):
        result = SearchEnabledFAYT()
        if result == STATUS_DISABLED:
            self.labelFeedbackAsYouType.setText(STATUS_DISABLED)
            self.labelFeedbackAsYouType.setStyleSheet('color:green')
        else:
            self.labelFeedbackAsYouType.setText(STATUS_ENABLED)
            self.labelFeedbackAsYouType.setStyleSheet('color:red')

    def FeedbackAsYouTypeButtonClick(self):
        result = SearchEnabledFAYT()
        if result == STATUS_DISABLED:
            EnabledFAYTOn()
        else:
            EnabledFAYTOff()
        self.updateFeedbackAsYouType()

    def updateActivityFeed(self):
        result = SearchEnableActivityFeed()
        if result == STATUS_DISABLED:
            self.labelActivityFeed.setText(STATUS_DISABLED)
            self.labelActivityFeed.setStyleSheet('color:green')
        else:
            self.labelActivityFeed.setText(STATUS_ENABLED)
            self.labelActivityFeed.setStyleSheet('color:red')

    def ActivityFeedButtonClick(self):
        result = SearchEnableActivityFeed()
        if result == STATUS_DISABLED:
            EnableActivityFeedOn()
        else:
            EnableActivityFeedOff()
        self.updateActivityFeed()

    def updateApplicationAccessToLocation(self):
        result1 = SearchValueAATL()
        result2 = SearchStatusAATL()
        result3 = SearchLetAppsAccessLocation()
        if result1 and result2 and result3 == STATUS_DISABLED:
            self.labelApplicationAccessToLocation.setText(STATUS_DISABLED)
            self.labelApplicationAccessToLocation.setStyleSheet('color:green')
        else:
            self.labelApplicationAccessToLocation.setText(STATUS_ENABLED)
            self.labelApplicationAccessToLocation.setStyleSheet('color:red')

    def ApplicationAccessToLocationButtonClick(self):
        result1 = SearchValueAATL()
        result2 = SearchStatusAATL()
        result3 = SearchLetAppsAccessLocation()
        if result1 and result2 and result3 == STATUS_DISABLED:
            ValueAATLOn()
            StatusAATLOn()
            LetAppsAccessLocationOn()
        else:
            ValueAATLOff()
            StatusAATLOff()
            LetAppsAccessLocationOff()
        self.updateApplicationAccessToLocation()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = WindowsPrivacy()
    energy_window.show()
    sys.exit(app.exec())
