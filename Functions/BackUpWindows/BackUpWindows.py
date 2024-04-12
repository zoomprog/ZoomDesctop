import os
import winreg
import json
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog
import subprocess
from enum import Enum, auto

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

from Functions.Twics.Search.SearchSvchost import check_svc_host_split_threshold_Search
from Functions.Twics.Disable.DisableSvchost import svc_host_split_threshold_Disable
from Functions.Twics.Enable.EnableSvchost import svc_host_split_threshold_Enable

from Functions.Twics.Search.SearchUpdateLastNFS import nfs_atime_status_windows_Update
from Functions.Twics.Disable.DisableUpdateLastNFS import nfs_atime_status_windows_Disable
from Functions.Twics.Enable.EnableUpdateLastNFS import nfs_atime_status_windows_Enable

from Functions.Twics.Search.SearchConvertNameFile83 import ConvertNameFile83_Update
from Functions.Twics.Disable.DisableConvertNameFile83 import ConvertNameFile83_Disable
from Functions.Twics.Enable.EnableConvertNameFile83 import ConvertNameFile83_Enable

from Functions.Twics.Search.SearchDiagnosricEvents import check_logs_status
from Functions.Twics.Disable.DisableDiagnosricEvents import disable_event_viewer_logs
from Functions.Twics.Enable.EnableDiagnosricEvents import enable_event_viewer_logs

from Functions.Task.TasksForAnalysis.TasksForAnalysis import SearchAnalyzeSystem, AnalyzeSystemOn, AnalyzeSystemOff, SearchBackup, BackupOn, BackupOff
from Functions.Task.DiagnosticTasks.DiagnosticTasks import SearchProactiveScan, ProactiveScanOn, ProactiveScanOff
from Functions.Task.DiagnosticTasks.DiagnosticTasks import (SearchRecommendedTroubleshootingScanner, RecommendedTroubleshootingScannerOn, RecommendedTroubleshootingScannerOff, SearchMicrosoftWindowsDiskDiagnosticDataCollector, MicrosoftWindowsDiskDiagnosticDataCollectorOn, MicrosoftWindowsDiskDiagnosticDataCollectorOff, SearchScheduled, ScheduledOn, ScheduledOff,
                                                            SearchMicrosoftWindowsDiskDiagnosticResolver, MicrosoftWindowsDiskDiagnosticResolverOn, MicrosoftWindowsDiskDiagnosticResolverOff, SearchDiagnostics, DiagnosticsOn, DiagnosticsOff, SearchStorageSense, StorageSenseOn, StorageSenseOff, SearchRunFullMemoryDiagnostic, RunFullMemoryDiagnosticOn, RunFullMemoryDiagnosticOff,
                                                            SearchProcessMemoryDiagnosticEvents, ProcessMemoryDiagnosticEventsOn, ProcessMemoryDiagnosticEventsOff, SearchAnalyzeSystemTask, AnalyzeSystemTaskOn, AnalyzeSystemTaskOff, SearchBgTaskRegistrationMaintenanceTask, BgTaskRegistrationMaintenanceTaskOn, BgTaskRegistrationMaintenanceTaskOff, Searchappuriverifierdaily, appuriverifierdailyOn,
                                                            appuriverifierdailyOff, SearchUsageDataReporting, UsageDataReportingOn, UsageDataReportingOff, SearchCalibrationLoader, CalibrationLoaderOn, CalibrationLoaderOff)
from Functions.Task.NetPrecompilation.NetPrecompilation import (SearchNETFrameworkNGENv4030319, NETFrameworkNGENv4030319On, NETFrameworkNGENv4030319Off, SearchNETFrameworkNGENv403031964, NETFrameworkNGENv403031964On, NETFrameworkNGENv403031964off, SearchNETFrameworkNGENv403031964Critical, NETFrameworkNGENv403031964CriticalOn, NETFrameworkNGENv403031964Criticaloff,
                                                                SearchNETFrameworkNGENv4030319Critical, NETFrameworkNGENv4030319CriticalOn, NETFrameworkNGENv4030319Criticaloff)
from Functions.Task.AutoProxyDetection.AutoProxyDetection import SearchProxy, ProxyOn, ProxyOff
from Functions.Task.InstallingAndRemovingLanguages.InstallingAndRemovingLanguages import (SearchSynchronizLanguageSettings, SynchronizLanguageSettingsOn, SynchronizLanguageSettingsOff, SearchInstallation, InstallationOn, InstallationOff, SearchReconcileLanguageResources, ReconcileLanguageResourcesOn, ReconcileLanguageResourcesOff, SearchUninstallation, UninstallationOn, UninstallationOff,
                                                                                          SearchLPRemove, LPRemoveOn, LPRemoveOff)
from Functions.Task.AutoPerformanceCheck.AutoPerformanceCheck import SearchWinSAT, WinSATOn, WinSATOff
from Functions.Task.MapsLocation.MapsLocation import SearchMapsToastTask, MapsToastTaskOn, MapsToastTaskOff, SearchMapsUpdateTask, MapsUpdateTaskOn, MapsUpdateTaskOff, SearchNotifications, NotificationsOff, NotificationsOn, SearchWindowsActionDialog, WindowsActionDialogOff, WindowsActionDialogOn
from Functions.Task.RemoteControl.RemoteControl import SearchRemoteAssistanceTask, RemoteAssistanceTaskOn, RemoteAssistanceTaskOff
from Functions.Task.CleaningTasks.CleaningTasks import SearchCleanupTemporaryState, CleanupTemporaryStateOn, CleanupTemporaryStateOff, SearchDsSvcCleanup, DsSvcCleanupOn, DsSvcCleanupOff, SearchSilentCleanup, SilentCleanupOn, SilentCleanupOff, SearchCleanupOfflineContent, CleanupOfflineContentOn, CleanupOfflineContentOff, SearchCacheTask, CacheTaskOn, CacheTaskOff
from Functions.Task.OnOffMicrosoftStore.MicrosoftStore import disable_microsoft_store, enable_microsoft_store, check_microsoft_store_status, check_microsoft_store_status2, enable_microsoft_store2, disable_microsoft_store2
from Functions.Task.Xbox.Xbox import check_xbox_status, enable_xbox, disable_xbox

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
from Functions.Privacy.ApplicationAccessToAccountInformation.ApplicationAccessToAccountInformation import ValueAATIOn, ValueAATIOff, SearchValueAATI, LetAppsAccessAccountInfoOn, LetAppsAccessAccountInfoOff, SearchLetAppsAccessAccountInfo
from Functions.Privacy.ApplicationAccessToMotionData.ApplicationAccessToMotionData import ValueAATMDOn, ValueAATMDOff, SearchValueAATMD, LetAppsAccessMotionOn, LetAppsAccessMotionOff, SearchLetAppsAccessMotion
from Functions.Privacy.AppAccessToPhone.AppAccessToPhone import LetAppsAccessPhoneOn, LetAppsAccessPhoneOff, SearchLetAppsAccessPhone
from Functions.Privacy.ApplicationAccessToTrustedDevices.ApplicationAccessToTrustedDevices import LetAppsAccessTrustedDevicesOn, LetAppsAccessTrustedDevicesOff, SearchLetAppsAccessTrustedDevices
from Functions.Privacy.AppAccessToDeviceSynchronization.AppAccessToDeviceSynchronization import LetAppsSyncWithDevicesOn, LetAppsSyncWithDevicesOff, SearchLetAppsSyncWithDevices
from Functions.Privacy.ApplicationsAccessDiagnosticInformationAboutOtherApplications.ApplicationsAccessDiagnosticInformationAboutOtherApplications import ValueAADAOAOn, ValueAADAOAOff, SearchValueAADAOA, LetAppsAccessMotionOn, LetAppsAccessMotionOff, SearchLetAppsAccessMotion
from Functions.Privacy.ApplicationAccessToContacts.ApplicationAccessToContacts import ValueContactOn, ValueContactOff, SearchalueContact, LetAppsAccessContactsOn, LetAppsAccessContactsOff, SearchLetAppsAccessContacts
from Functions.Privacy.ApplicationAccessToCalendar.ApplicationAccessToCalendar import ValueCalendar1On, ValueCalendar1Off, SearchValueCalendar1, LetAppsAccessCalendarOn, LetAppsAccessCalendarOff, SearchLetAppsAccessCalendar
from Functions.Privacy.ApplicationAccessToCallLog.ApplicationAccessToCallLog import ValueCallAccessOn, ValueCallAccessOff, SearchValueCallAccess, LetAppsAccessCallHistoryOn, LetAppsAccessCallHistoryOff, SearchLetAppsAccessCallHistory
from Functions.Privacy.ApplicationAccessToEmail.ApplicationAccessToEmail import ValueEmailOn, ValueEmailOff, SearchValueEmail, LetAppsAccessEmailOn, LetAppsAccessEmailOff, SearchLetAppsAccessEmail
from Functions.Privacy.ApplicationAccessToTasks.ApplicationAccessToTasks import ValueTaskOn, ValueTaskOff, SearchValueTask, LetAppsAccessTasksOn, LetAppsAccessTasksOff, SearchLetAppsAccessTasks
from Functions.Privacy.ApplicationAccessToMessages.ApplicationAccessToMessages import ValueMessageOn, ValueMessageOff, SearchValueMessage, LetAppsAccessCalendar2On, LetAppsAccessCalendar2Off, SearchLetAppsAccessCalendar2
from Functions.Privacy.ApplicationAccessToRadio.ApplicationAccessToRadio import ValueRadioOn, ValueRadioOff, SearchValueRadio, LetAppsAccessRadiosOn, LetAppsAccessRadiosOff, SearchLetAppsAccessRadios
from Functions.Privacy.AppAccessToBluetoothDevices.AppAccessToBluetoothDevices import ValueBluetoothOn, ValueBluetoothOff, SearchValueBluetooth
from Functions.Privacy.ApplicationAccessToTheDocumentsFolder.ApplicationAccessToTheDocumentsFolder import ValueDocsOn, ValueDocsOff,SearchValueDocs
from Functions.Privacy.ApplicationAccessToThePicturesFolder.pushApplicationAccessToThePicturesFolder import ValuePicturesLibraryOn, ValuePicturesLibraryOff, SearchValuePicturesLibrary
from Functions.Privacy.ApplicationAccessToTheVideosFolder.ApplicationAccessToTheVideosFolder import VideosLibraryOn, VideosLibraryOff, SearchVideosLibrary
from Functions.Privacy.ApplicationAccessToAnotherFileSystem.ApplicationAccessToAnotherFileSystem import AccessFileSystemOn, AccessFileSystemOff, SearchAccessFileSystem



STATUS_DISABLED = "Disabled"
STATUS_ENABLED = "Enabled"
STATUS_ERROR = "Error"
Bar = 0

with open('BakUpFile/BKFILE.json', 'r', encoding='utf-8') as file:
    funct = json.load(file)



class SystemStatus(Enum):
    DISABLED = auto()
    ENABLED = auto()
    ERROR = auto()


def updateMouseAcceleration():
    if funct['updateMouseAcceleration'] == STATUS_DISABLED:
        MouseSpeedOn()
        MouseThreshold1On()
        MouseThreshold2On()
    else:
        print('2')
        MouseSpeedOff()
        MouseThreshold1Off()
        MouseThreshold2Off()


def updateProtectionNotifications():
    if funct['updateProtectionNotifications'] == STATUS_DISABLED:
        NotificationEnable1On()
        NotificationEnable2On()
        DisableNotifications1On()
    else:
        NotificationEnable1Off()
        NotificationEnable2Off()
        DisableNotifications1Off()


def updateAutoUpdateDriversatSystemstartup():
    if funct['updateAutoUpdateDriversatSystemstartup'] == STATUS_DISABLED:
        ExcludeWUDriversInQualityUpdateOn()
        SearchOrderConfigOn()
    else:
        ExcludeWUDriversInQualityUpdateOff()
        SearchOrderConfigOff()



def updateUWP():
    if funct['updateUWP'] == STATUS_DISABLED:
        GlobalUserDisabledOn()
        BackgroundAppGlobalToggleStartOn()
        BackgroundAppGlobalToggleOn()
    else:
        GlobalUserDisabledOff()
        GBackgroundAppGlobalToggleStartOff()
        BackgroundAppGlobalToggleOff()



def updateAutoUpdatingAppsStore():
    if funct['updateAutoUpdatingAppsStore'] == STATUS_DISABLED:
        AutoDownloadOn()
    else:
        AutoDownloadOff()


def updateAppearance():
    if funct['updateAppearance'] == STATUS_DISABLED:
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


def updateGameBar():
    if funct['updateGameBar'] == STATUS_DISABLED:
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


def updateMultyPlanOverplay():
    if funct['updateMultyPlanOverplay'] == STATUS_DISABLED:
        OverlayTestModeOn()
    else:
        OverlayTestModeOff()



def updateWindowsFirewall():
    if funct['updateWindowsFirewall'] == STATUS_DISABLED:
        EnableFirewallOn()
        EnableFirewall2On()
    else:
        EnableFirewallOff()
        EnableFirewall2Off()

def updateWindowsUAC():
    if funct['updateWindowsUAC'] == STATUS_DISABLED:
        PromptOnSecureDesktopOn()
        ConsentPromptBehaviorAdminOn()
    else:
        PromptOnSecureDesktopOff()
        ConsentPromptBehaviorAdminOff()


def updateSystemResponsiveness():
    if funct['updateSystemResponsiveness'] == STATUS_DISABLED:
        SystemResponsivenessEnable()
    else:
        SystemResponsivenessDisable()



def updateWin32_priority_separation():
    if funct['updateWin32_priority_separation'] == STATUS_DISABLED:
        set_win32_priority_separation_Disable(2)
    else:
        set_win32_priority_separation_Enable(26)



def updateMeltdownSpectre():
    if funct['updateMeltdownSpectre'] == STATUS_DISABLED:
        MeltdownSpectre_Enable()
    else:
        MeltdownSpectre_Disable()



def updateWindowsReservedStorage():
    if funct['updateWindowsReservedStorage'] == STATUS_DISABLED:
        disable_reserved_storage()
    else:
        enable_reserved_storage()



def updateSvchost():
    if funct['updateSvchost'] == STATUS_DISABLED:
        svc_host_split_threshold_Disable()
    else:
        svc_host_split_threshold_Enable()


def updateUpdateLastNFS():
    if funct['updateUpdateLastNFS'] == STATUS_DISABLED:
        nfs_atime_status_windows_Disable()
    else:
        nfs_atime_status_windows_Enable()



def updateConvertNameFile83():
    if funct['updateConvertNameFile83'] == STATUS_DISABLED:
        ConvertNameFile83_Disable()
    else:
        ConvertNameFile83_Enable()



def updateDiagnosricEvents():
    logs = [
        "Microsoft-Windows-SleepStudy/Diagnostic",
        "Microsoft-Windows-Kernel-Processor-Power/Diagnostic",
        "Microsoft-Windows-UserModePowerService/Diagnostic"
    ]
    if funct['updateDiagnosricEvents'] == STATUS_DISABLED:
        enable_event_viewer_logs(logs)
    else:
        disable_event_viewer_logs(logs)


def updateTasksForAnalysis():
    if funct['updateTasksForAnalysis'] == STATUS_DISABLED:
        AnalyzeSystemOn()
        BackupOn()
    else:
        AnalyzeSystemOff()
        BackupOff()



def updateDiagnosticTasks():
    if funct['updateDiagnosticTasks'] == STATUS_DISABLED:
        ProactiveScanOn()
        RecommendedTroubleshootingScannerOn()
        MicrosoftWindowsDiskDiagnosticDataCollectorOn()
        ScheduledOn()
        MicrosoftWindowsDiskDiagnosticResolverOn()
        DiagnosticsOn()
        StorageSenseOn()
        RunFullMemoryDiagnosticOn()
        ProcessMemoryDiagnosticEventsOn()
        AnalyzeSystemTaskOn()
        BgTaskRegistrationMaintenanceTaskOn()
        appuriverifierdailyOn()
        UsageDataReportingOn()
        CalibrationLoaderOn()
    else:
        ProactiveScanOff()
        RecommendedTroubleshootingScannerOff()
        MicrosoftWindowsDiskDiagnosticDataCollectorOff()
        ScheduledOff()
        MicrosoftWindowsDiskDiagnosticResolverOff()
        DiagnosticsOff()
        StorageSenseOff()
        RunFullMemoryDiagnosticOff()
        ProcessMemoryDiagnosticEventsOff()
        AnalyzeSystemTaskOff()
        BgTaskRegistrationMaintenanceTaskOff()
        appuriverifierdailyOff()
        UsageDataReportingOff()
        CalibrationLoaderOff()



def updateNetPrecompilation():
    if funct['updateNetPrecompilation'] == STATUS_DISABLED:
        NETFrameworkNGENv4030319On()
        NETFrameworkNGENv403031964On()
        NETFrameworkNGENv403031964CriticalOn()
        NETFrameworkNGENv4030319CriticalOn()
    else:
        NETFrameworkNGENv4030319Off()
        NETFrameworkNGENv403031964off()
        NETFrameworkNGENv403031964Criticaloff()
        NETFrameworkNGENv4030319Criticaloff()



def updateAutoProxyDetection():
    if funct['updateAutoProxyDetection'] == STATUS_DISABLED:
        ProxyOn()
    else:
        ProxyOff()


def updateInstallingAndRemovingLanguages():
    if funct['updateInstallingAndRemovingLanguages'] == STATUS_DISABLED:
        SynchronizLanguageSettingsOn()
        InstallationOn()
        ReconcileLanguageResourcesOn()
        UninstallationOn()
        LPRemoveOn()
    else:
        SynchronizLanguageSettingsOff()
        InstallationOff()
        ReconcileLanguageResourcesOff()
        UninstallationOff()
        LPRemoveOff()


def updateAutoPerformanceCheck():
    if funct['updateAutoPerformanceCheck'] == STATUS_DISABLED:
        WinSATOn()
    else:
        WinSATOff()


def updateMapsLocation():
    if funct['updateMapsLocation'] == STATUS_DISABLED:
        MapsToastTaskOn()
        MapsUpdateTaskOn()
        NotificationsOn()
        WindowsActionDialogOn()
    else:
        MapsToastTaskOff()
        MapsUpdateTaskOff()
        NotificationsOff()
        WindowsActionDialogOff()


def updateRemoteControl():
    if funct['updateRemoteControl'] == STATUS_DISABLED:
        RemoteAssistanceTaskOn()
    else:
        RemoteAssistanceTaskOff()


def updateCleaningTasks():
    if funct['updateCleaningTasks'] == STATUS_DISABLED:
        CleanupTemporaryStateOn()
        DsSvcCleanupOn()
        SilentCleanupOn()
        CleanupOfflineContentOn()
        CacheTaskOn()
    else:
        CleanupTemporaryStateOff()
        DsSvcCleanupOff()
        SilentCleanupOff()
        CleanupOfflineContentOff()
        CacheTaskOff()


def updateMicrosoftStore():
    if funct['updateMicrosoftStore'] == STATUS_DISABLED:
        enable_microsoft_store()
        enable_microsoft_store2()
    else:
        disable_microsoft_store()
        disable_microsoft_store2()



def updateWindowsXBOX():
    if funct['updateWindowsXBOX'] == STATUS_DISABLED:
        enable_xbox()
    else:
        disable_xbox()



def updateTelemetria():
    if funct['updateTelemetria'] == STATUS_DISABLED:
        Start1On()
        Start2On()
        Start3On()
        Start4On()
    else:
        Start1Off()
        Start2Off()
        Start3Off()
        Start4Off()



def updateTelemetriaWebCome():
    if funct['updateTelemetriaWebCome'] == STATUS_DISABLED:
        enable_task_schtasks()
        SetEmptyDebuggerOff()
    else:
        disable_task_schtasks()
        SetEmptyDebuggerOn()


def uodateTaskMCA():
    if funct['uodateTaskMCA'] == STATUS_DISABLED:
        enable_TaskMCA_CompatibilityAppraiser()
        SetEmptyDebuggerOff()
    else:
        disable_TaskMCA_CompatibilityAppraiser()
        SetEmptyDebuggerOn()


def updateUpdateDateCEIP():
    if funct['updateUpdateDateCEIP'] == STATUS_DISABLED:
        enable_ProgramDataUpdater()
    else:
        disable_ProgramDataUpdater()


def updateTaskApplicationImpactTelemetry():
    if funct['updateTaskApplicationImpactTelemetry'] == STATUS_DISABLED:
        enable_ait_agent_task()
    else:
        disable_ait_agent_task()



def uodateProductivityAppReminder():
    if funct['uodateProductivityAppReminder'] == STATUS_DISABLED:
        enable_StartupAppTask()
    else:
        disable_StartupAppTask()



def updateTaskCEIP():
    if funct['updateTaskCEIP'] == STATUS_DISABLED:
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


def updateCEIPSQM():
    if funct['updateCEIPSQM'] == STATUS_DISABLED:
        CEIPSQMOn()
    else:
        CEIPSQMOff()



def updateTelemetrApplicationImpact():
    if funct['updateTelemetrApplicationImpact'] == STATUS_DISABLED:
        AITEnableOn()
    else:
        AITEnableOff()



def updateTelemetrNalogDate():
    if funct['updateTelemetrNalogDate'] ==  STATUS_DISABLED:
        LimitEnhancedDiagnosticDataWindowsAnalyticsOn()
        AllowTelemetry3On()
        AllowTelemetry2On()
        AllowTelemetryOn()
    else:
        LimitEnhancedDiagnosticDataWindowsAnalyticsOff()
        AllowTelemetry3Off()
        AllowTelemetry2Off()
        AllowTelemetryOff()



def updateTelemetrLicense():
    if funct['updateTelemetrLicense'] == STATUS_DISABLED:
        NoGenTicketOn()
    else:
        NoGenTicketOff()



def updateWer():
    if funct['updateWer'] == STATUS_DISABLED:
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



def updateActiveVoiceForCortan():
    if funct['updateActiveVoiceForCortan'] == STATUS_DISABLED:
        AgentActivationEnabledOn()
        LetAppsActivateWithVoiceOn()
        enable_ProgramDataUpdater()
    else:
        AgentActivationEnabledOff()
        LetAppsActivateWithVoiceOff()
        disable_ProgramDataUpdater()



def updateActiveVoiceForCortanBlockSystem():
    if funct['updateActiveVoiceForCortanBlockSystem'] == STATUS_DISABLED:
        AgentActivationOnLockScreenEnabledOn()
        LetAppsActivateWithVoiceAboveLockOn()
    else:
        AgentActivationOnLockScreenEnabledOff()
        LetAppsActivateWithVoiceAboveLockOff()



def updateWindowsLocationProvider():
    if funct['updateWindowsLocationProvider'] == STATUS_DISABLED:
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

def updateAllowIndexingEncryptedStoresOrItems():
    if funct['updateAllowIndexingEncryptedStoresOrItems'] == STATUS_DISABLED:
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



def updateTargetedAdverisingAndMarketing():
    if funct['updateTargetedAdverisingAndMarketing'] == STATUS_DISABLED:
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


def updateCloudSaving():
    if funct['updateCloudSaving'] == STATUS_DISABLED:
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



def updateCloudVoice():
    if funct['updateCloudVoice'] == STATUS_DISABLED:
        HasAcceptedOn()
    else:
        HasAcceptedOff()


def updateWindowsSearchDateCollection():
    if funct['updateWindowsSearchDateCollection'] == STATUS_DISABLED:
        AcceptedPrivacyPolicyOn()
    else:
        AcceptedPrivacyPolicyOff()



def updateWindowsPrivacyConsentDisclaimer():
    if funct['updateWindowsPrivacyConsentDisclaimer'] == STATUS_DISABLED:
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




def updateCollectTextMessagesandHandwritingInput():
    if funct['updateCollectTextMessagesandHandwritingInput'] == STATUS_DISABLED:
        RestrictImplicitInkCollectionOn()
        RestrictImplicitTextCollectionOn()
        HarvestContactsOn()
    else:
        RestrictImplicitInkCollectionOff()
        RestrictImplicitTextCollectionOff()
        HarvestContactsOff()


def updateSensor():
    if funct['updateSensor'] == STATUS_DISABLED:
        DisableSensorsOn()
    else:
        DisableSensorsOff()


def updateWiFiSense():
    if funct['updateWiFiSense'] == STATUS_DISABLED:
        value1On()
        value2On()
        AutoConnectAllowedOEMOn()
    else:
        value1Off()
        value2Off()
        AutoConnectAllowedOEMOff()


def updateHideMostUsedApps():
    if funct['updateHideMostUsedApps'] == STATUS_DISABLED:
        HideMostUsedAppsOn()
    else:
        HideMostUsedAppsOff()


def updateInventoryCollector():
    if funct['updateInventoryCollector'] == STATUS_DISABLED:
        DisableInventoryOn()
        ICDeviceOn()
        DeviceUserOn()
    else:
        DisableInventoryOff()
        ICDeviceOff()
        DeviceUserOff()




def updateSiteAccessToTheListOfLanguages():
    if funct['updateSiteAccessToTheListOfLanguages'] == STATUS_DISABLED:
        HttpAcceptLanguageOptOutOn()
    else:
        HttpAcceptLanguageOptOutOff()


def updateRecordingActions():
    if funct['updateRecordingActions'] == STATUS_DISABLED:
        HttpAcceptLanguageOptOutRAOn()
    else:
        HttpAcceptLanguageOptOutRAOff()


def updateFeedbackAsYouType():
    if funct['updateFeedbackAsYouType'] == STATUS_DISABLED:
        EnabledFAYTOn()
    else:
        EnabledFAYTOff()


def updateActivityFeed():
    if funct['updateActivityFeed'] == STATUS_DISABLED:
        EnableActivityFeedOn()
    else:
        EnableActivityFeedOff()


def updateApplicationAccessToLocation():
    if funct['updateApplicationAccessToLocation'] == STATUS_DISABLED:
        ValueAATLOn()
        StatusAATLOn()
        LetAppsAccessLocationOn()
    else:
        ValueAATLOff()
        StatusAATLOff()
        LetAppsAccessLocationOff()



def updateApplicationAccessToAccountInformation():
    if funct['updateApplicationAccessToAccountInformation'] == STATUS_DISABLED:
        ValueAATIOn()
        LetAppsAccessAccountInfoOn()
    else:
        ValueAATIOff()
        LetAppsAccessAccountInfoOff()


def updateApplicationAccessToMotionData():
    if funct['updateApplicationAccessToMotionData'] == STATUS_DISABLED:
        ValueAATMDOn()
        LetAppsAccessMotionOn()
    else:
        LetAppsAccessMotionOff()
        ValueAATMDOff()


def updateAppAccessToPhone():
    if funct['updateAppAccessToPhone'] == STATUS_DISABLED:
        LetAppsAccessPhoneOn()
    else:
        LetAppsAccessPhoneOff()



def updateApplicationAccessToTrustedDevices():
    if funct['updateApplicationAccessToTrustedDevices'] == STATUS_DISABLED:
        LetAppsAccessTrustedDevicesOn()
    else:
        LetAppsAccessTrustedDevicesOff()



def updateApplicationAccessToDeviceSynchronization():
    if funct['updateApplicationAccessToDeviceSynchronization'] == STATUS_DISABLED:
        LetAppsSyncWithDevicesOn()
    else:
        LetAppsSyncWithDevicesOff()


def updateApplicationsAccessDiagnosticInformationAboutOtherApplications():
    if funct['updateApplicationsAccessDiagnosticInformationAboutOtherApplications'] == STATUS_DISABLED:
        ValueAADAOAOn()
        LetAppsAccessMotionOn()
    else:
        ValueAADAOAOff()
        LetAppsAccessMotionOff()


def updateApplicationAccessToContacts():
    if funct['updateApplicationAccessToContacts'] == STATUS_DISABLED:
        ValueContactOn()
        LetAppsAccessContactsOn()
    else:
        ValueContactOff()
        LetAppsAccessContactsOff()


def updateApplicationAccessToCalendar():
    if funct['updateApplicationAccessToCalendar'] == STATUS_DISABLED:
        ValueCalendar1On()
        LetAppsAccessCalendarOn()
    else:
        ValueCalendar1Off()
        LetAppsAccessCalendarOff()



def updateApplicationAccessToCallLog():
    if funct['updateApplicationAccessToCallLog'] == STATUS_DISABLED:
        ValueCallAccessOn()
        LetAppsAccessCallHistoryOn()
    else:
        ValueCallAccessOff()
        LetAppsAccessCallHistoryOff()


def updateApplicationAccessToEmail():
    if funct['updateApplicationAccessToEmail'] == STATUS_DISABLED:
        ValueEmailOn()
        LetAppsAccessEmailOn()
    else:
        ValueEmailOff()
        LetAppsAccessEmailOff()


def updateApplicationAccessToTasks():
    if funct['updateApplicationAccessToTasks'] == STATUS_DISABLED:
        ValueTaskOn()
        LetAppsAccessTasksOn()
    else:
        ValueTaskOff()
        LetAppsAccessTasksOff()


def updateApplicationAccessToMessages():
    if funct['updateApplicationAccessToMessages'] == STATUS_DISABLED:
        ValueMessageOn()
        LetAppsAccessCalendar2On()
    else:
        ValueMessageOff()
        LetAppsAccessCalendar2Off()



def updateApplicationAccessToRadio():
    if funct['updateApplicationAccessToRadio'] == STATUS_DISABLED:
        ValueRadioOn()
        LetAppsAccessRadiosOn()
    else:
        ValueRadioOff()
        LetAppsAccessRadiosOff()


def updateAppAccessToBluetoothDevices():
    if funct['updateAppAccessToBluetoothDevices'] == STATUS_DISABLED:
        ValueBluetoothOn()
    else:
        ValueBluetoothOff()


def updateApplicationAccessToTheDocumentsFolder():
    if funct['updateApplicationAccessToTheDocumentsFolder'] == STATUS_DISABLED:
        ValueDocsOn()
    else:
        ValueDocsOff()


def updateApplicationAccessToThePicturesFolder():
    if funct['updateApplicationAccessToThePicturesFolder'] == STATUS_DISABLED:
        ValuePicturesLibraryOn()
    else:
        ValuePicturesLibraryOff()


def updateApplicationAccessToTheVideosFolder():
    if funct['updateApplicationAccessToTheVideosFolder'] == STATUS_DISABLED:
        VideosLibraryOn()
    else:
        VideosLibraryOff()


def updateApplicationAccessToAnotherFileSystem():
    if funct['updateApplicationAccessToAnotherFileSystem'] == STATUS_DISABLED:
        AccessFileSystemOn()
    else:
        AccessFileSystemOff()

updateApplicationAccessToAnotherFileSystem()
updateApplicationAccessToThePicturesFolder()
updateApplicationAccessToTheDocumentsFolder()
updateAppAccessToBluetoothDevices()
updateApplicationAccessToRadio()
updateApplicationAccessToMessages()
updateApplicationAccessToTasks()
updateApplicationAccessToEmail()
updateApplicationAccessToCallLog()
updateApplicationAccessToCalendar()
updateApplicationAccessToContacts()
updateApplicationsAccessDiagnosticInformationAboutOtherApplications()
updateApplicationAccessToDeviceSynchronization()
updateApplicationAccessToTrustedDevices()
updateAppAccessToPhone()
updateApplicationAccessToMotionData()
updateApplicationAccessToAccountInformation()
updateApplicationAccessToLocation()
updateActivityFeed()
updateFeedbackAsYouType()
updateRecordingActions()
updateSiteAccessToTheListOfLanguages()
updateInventoryCollector()
updateHideMostUsedApps()
updateWiFiSense()
updateSensor()
updateCollectTextMessagesandHandwritingInput()
updateWindowsPrivacyConsentDisclaimer()
updateWindowsSearchDateCollection()
updateCloudVoice()
updateCloudSaving()
updateTargetedAdverisingAndMarketing()
updateAllowIndexingEncryptedStoresOrItems()
updateWindowsLocationProvider()
updateActiveVoiceForCortanBlockSystem()
updateWer()
updateActiveVoiceForCortan()
updateTelemetrLicense()
updateTelemetrNalogDate()
updateTelemetrApplicationImpact()
updateCEIPSQM()
updateTaskCEIP()
uodateProductivityAppReminder()
updateTaskApplicationImpactTelemetry()
updateUpdateDateCEIP()
uodateTaskMCA()
updateTelemetriaWebCome()
updateTelemetria()
updateWindowsXBOX()
updateMicrosoftStore()
updateCleaningTasks()
updateRemoteControl()
updateMapsLocation()
updateAutoPerformanceCheck()
updateInstallingAndRemovingLanguages()
updateAutoProxyDetection()
updateNetPrecompilation()
updateDiagnosticTasks()
updateTasksForAnalysis()
updateSystemResponsiveness()
updateWin32_priority_separation()
updateMeltdownSpectre()
updateWindowsReservedStorage()
updateSvchost()
updateUpdateLastNFS()
updateConvertNameFile83()
updateDiagnosricEvents()
updateWindowsUAC()
updateWindowsFirewall()
updateMouseAcceleration()
updateProtectionNotifications()
updateAutoUpdateDriversatSystemstartup()
updateUWP()
updateAutoUpdatingAppsStore()
updateAppearance()
updateGameBar()
updateMultyPlanOverplay()
#удаляем json файл
if os.path.exists('BakUpFile\BKFILE.json'):
    os.remove('BakUpFile\BKFILE.json')

