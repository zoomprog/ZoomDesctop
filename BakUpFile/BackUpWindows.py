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
from Functions.BaseSettings.UWP.UWP import GlobalUserDisabledOn, GlobalUserDisabledOff, BackgroundAppGlobalToggleOn, BackgroundAppGlobalToggleOff, SearchBackgroundAppGlobalToggle, BackgroundAppGlobalToggleStartOn, GBackgroundAppGlobalToggleStartOff, SearchBackgroundAppGlobalToggleStart
from Functions.BaseSettings.AutoUpdatingAppsStore.AutoUpdatingAppsStore import AutoDownloadOn, AutoDownloadOff, SearchAutoDownload
from Functions.BaseSettings.Appearance.Appearance import (TaskbarAnimationsOn, TaskbarAnimationsOff, IconsOnlyOn, IconsOnlyOff, SearchIconsOnly, ListviewShadowOn, ListviewShadowOff, SearchListviewShadow, ListviewAlphaSelectOn, ListviewAlphaSelectOff, SearchListviewAlphaSelect, MinAnimateOn, MinAnimateOff, SearchMinAnimate, DragFullWindowsOn, DragFullWindowsOff,
                                                          EnableAeroPeekOn, EnableAeroPeekOff, FontSmoothingOn, FontSmoothingOff, SearchFontSmoothing, VisualFXSettingOn, VisualFXSettingOff, SearchVisualFXSetting, VisualFXSettingOn2, VisualFXSettingOff2, SearchVisualFXSetting2)
from Functions.BaseSettings.GameBar.GameBar import (AutoGameModeEnabledOn, AutoGameModeEnabledOff, GamePanelStartupTipIndexOn, GamePanelStartupTipIndexOff, ShowStartupPanelOn, ShowStartupPanelOff, UseNexusForGameBarEnabledOn, UseNexusForGameBarEnabledOff, SearchUseNexusForGameBarEnabled, AllowAutoGameModeOn,
                                                    AllowAutoGameModeOff, AllowGameDVROn, AllowGameDVROff, AppCaptureEnabledOff, AppCaptureEnabledOn, ValueGameBarOn, ValueGameBarOff)
from Functions.BaseSettings.MultyPlanOverplay.MultyPlanOverplay import OverlayTestModeOn, OverlayTestModeOff
from Functions.BaseSettings.WindowsFirewall.WindowsFirewall import EnableFirewallOn, EnableFirewallOff, EnableFirewall2On, EnableFirewall2Off
from Functions.BaseSettings.UAC.UAC import PromptOnSecureDesktopOn, PromptOnSecureDesktopOff, ConsentPromptBehaviorAdminOn, ConsentPromptBehaviorAdminOff


from Functions.Twics.Disable.DisableSystemResponsiveness import SystemResponsivenessDisable
from Functions.Twics.Enable.EnableSystemResponsiveness import SystemResponsivenessEnable


from Functions.Twics.Disable.DisableWin32PrioritySeparation import set_win32_priority_separation_Disable
from Functions.Twics.Enable.EnableWin32PrioritySeparation import set_win32_priority_separation_Enable


from Functions.Twics.Disable.DisableMeltdownSpectre import MeltdownSpectre_Disable
from Functions.Twics.Enable.EnableMeltdownSpectre import MeltdownSpectre_Enable


from Functions.Twics.Disable.DisableWindowsReservedStorage import disable_reserved_storage
from Functions.Twics.Enable.EnableWindowsReservedStorage import enable_reserved_storage


from Functions.Twics.Disable.DisableSvchost import svc_host_split_threshold_Disable
from Functions.Twics.Enable.EnableSvchost import svc_host_split_threshold_Enable


from Functions.Twics.Disable.DisableUpdateLastNFS import nfs_atime_status_windows_Disable
from Functions.Twics.Enable.EnableUpdateLastNFS import nfs_atime_status_windows_Enable


from Functions.Twics.Disable.DisableConvertNameFile83 import ConvertNameFile83_Disable
from Functions.Twics.Enable.EnableConvertNameFile83 import ConvertNameFile83_Enable


from Functions.Twics.Disable.DisableDiagnosricEvents import disable_event_viewer_logs
from Functions.Twics.Enable.EnableDiagnosricEvents import enable_event_viewer_logs

from Functions.Task.TasksForAnalysis.TasksForAnalysis import AnalyzeSystemOn, AnalyzeSystemOff, BackupOn, BackupOff
from Functions.Task.DiagnosticTasks.DiagnosticTasks import ProactiveScanOn, ProactiveScanOff
from Functions.Task.DiagnosticTasks.DiagnosticTasks import (RecommendedTroubleshootingScannerOn, RecommendedTroubleshootingScannerOff, MicrosoftWindowsDiskDiagnosticDataCollectorOn, MicrosoftWindowsDiskDiagnosticDataCollectorOff, ScheduledOn, ScheduledOff,
                                                            MicrosoftWindowsDiskDiagnosticResolverOn, MicrosoftWindowsDiskDiagnosticResolverOff, DiagnosticsOn, DiagnosticsOff, StorageSenseOn, StorageSenseOff,RunFullMemoryDiagnosticOn, RunFullMemoryDiagnosticOff,
                                                            ProcessMemoryDiagnosticEventsOn, ProcessMemoryDiagnosticEventsOff, AnalyzeSystemTaskOn, AnalyzeSystemTaskOff, BgTaskRegistrationMaintenanceTaskOn, BgTaskRegistrationMaintenanceTaskOff, appuriverifierdailyOn,
                                                            appuriverifierdailyOff, UsageDataReportingOn, UsageDataReportingOff, CalibrationLoaderOn, CalibrationLoaderOff)
from Functions.Task.NetPrecompilation.NetPrecompilation import (NETFrameworkNGENv4030319On, NETFrameworkNGENv4030319Off, NETFrameworkNGENv403031964On, NETFrameworkNGENv403031964off, NETFrameworkNGENv403031964CriticalOn, NETFrameworkNGENv403031964Criticaloff,
                                                                NETFrameworkNGENv4030319CriticalOn, NETFrameworkNGENv4030319Criticaloff)
from Functions.Task.AutoProxyDetection.AutoProxyDetection import ProxyOn, ProxyOff
from Functions.Task.InstallingAndRemovingLanguages.InstallingAndRemovingLanguages import (SynchronizLanguageSettingsOn, SynchronizLanguageSettingsOff, InstallationOn, InstallationOff, ReconcileLanguageResourcesOn, ReconcileLanguageResourcesOff, UninstallationOn, UninstallationOff,
                                                                                          LPRemoveOn, LPRemoveOff)
from Functions.Task.AutoPerformanceCheck.AutoPerformanceCheck import WinSATOn, WinSATOff
from Functions.Task.MapsLocation.MapsLocation import MapsToastTaskOn, MapsToastTaskOff, MapsUpdateTaskOn, MapsUpdateTaskOff, NotificationsOff, NotificationsOn, WindowsActionDialogOff, WindowsActionDialogOn
from Functions.Task.RemoteControl.RemoteControl import RemoteAssistanceTaskOn, RemoteAssistanceTaskOff
from Functions.Task.CleaningTasks.CleaningTasks import CleanupTemporaryStateOn, CleanupTemporaryStateOff, DsSvcCleanupOn, DsSvcCleanupOff, SilentCleanupOn, SilentCleanupOff, CleanupOfflineContentOn, CleanupOfflineContentOff, SearchCacheTask, CacheTaskOn, CacheTaskOff
from Functions.Task.OnOffMicrosoftStore.MicrosoftStore import disable_microsoft_store, enable_microsoft_store, enable_microsoft_store2, disable_microsoft_store2
from Functions.Task.Xbox.Xbox import enable_xbox, disable_xbox

from Functions.Privacy.Telemetria.Telemetria import Start1On, Start1Off, Start2On, Start2Off, Start3On, Start3Off, Start4On, Start4Off
from Functions.Privacy.TelemetriaWebCome.TelemetriaWebCome import enable_task_schtasks, disable_task_schtasks,SetEmptyDebuggerOn, SetEmptyDebuggerOff
from Functions.Privacy.TaskMCA.TaskMCA import enable_TaskMCA_CompatibilityAppraiser, disable_TaskMCA_CompatibilityAppraiser
from Functions.Privacy.UpdateDateCEIP.UpdateDateCEIP import enable_ProgramDataUpdater, disable_ProgramDataUpdater
from Functions.Privacy.TaskApplicationImpactTelemetry.TaskApplicationImpactTelemetry import enable_ait_agent_task, disable_ait_agent_task
from Functions.Privacy.ProductivityAppReminder.ProductivityAppReminder import enable_StartupAppTask, disable_StartupAppTask
from Functions.Privacy.TaskCEIP.TaskCEIP import enable_Proxy, disable_Proxy, enable_BthSQM, disable_BthSQM, enable_Consolidator, disable_Consolidator, enable_KernelCeipTask, disable_KernelCeipTask, enable_UsbCeip, disable_UsbCeip
from Functions.Privacy.CEIPSQM.CEIPSQM import CEIPSQMOn, CEIPSQMOff
from Functions.Privacy.TelemetrApplicationImpact.TelemetrApplicationImpact import AITEnableOn, AITEnableOff
from Functions.Privacy.TelemetrNalogDate.TelemetrNalogDate import AllowTelemetryOn, AllowTelemetryOff, AllowTelemetry2On, AllowTelemetry2Off, AllowTelemetry3On, AllowTelemetry3Off, LimitEnhancedDiagnosticDataWindowsAnalyticsOn, LimitEnhancedDiagnosticDataWindowsAnalyticsOff
from Functions.Privacy.TelemetrLicense.TelemetrLicense import NoGenTicketOn, NoGenTicketOff
from Functions.Privacy.WER.WER import DisabledOn, DisabledOff, Disabled2On, Disabled2Off, DefaultConsentOn, DefaultConsentOff, DefaultOverrideBehaviorOn, DefaultOverrideBehaviorOff, DontSendAdditionalDataOn, DontSendAdditionalDataOff, LoggingDisabledOn, LoggingDisabledOff, \
    StartWEROn, StartWEROff, StartWER2On, StartWER2Off, enable_QueueReporting, disable_QueueReporting
from Functions.Privacy.ActiveVoiceForCortan.ActiveVoiceForCortan import AgentActivationEnabledOn, AgentActivationEnabledOff, LetAppsActivateWithVoiceOn, LetAppsActivateWithVoiceOff, enable_ProgramDataUpdater, disable_ProgramDataUpdater
from Functions.Privacy.ActiveVoiceForCortanBlockSystem.ActiveVoiceForCortanBlockSystem import AgentActivationOnLockScreenEnabledOn, AgentActivationOnLockScreenEnabledOff, LetAppsActivateWithVoiceAboveLockOn, LetAppsActivateWithVoiceAboveLockOff
from Functions.Privacy.WindowsLocationProvider.WindowsLocationProvider import DisableWindowsLocationProviderOn, DisableWindowsLocationProviderOff, DisableLocationScriptingOn, DisableLocationScriptingOff, DisableLocationOn, DisableLocationOff, SensorPermissionStateOn, SensorPermissionStateOff, SensorPermissionState2On, SensorPermissionState2Off
from Functions.Privacy.AllowIndexingEncryptedStoresOrItems.AllowIndexingEncryptedStoresOrItems import DAllowIndexingEncryptedStoresOrItemsOn, AllowIndexingEncryptedStoresOrItemsOff, AlwaysUseAutoLangDetectionOn, AlwaysUseAutoLangDetectionOff, AllowSearchToUseLocationOn, AllowSearchToUseLocationOff, \
    DisableWebSearch1On, DisableWebSearch1Off, ConnectedSearchUseWebOn, ConnectedSearchUseWebOff, BingSearchEnabledOn, BingSearchEnabledOff
from Functions.Privacy.TargetedAdverisingAndMarketing.TargetedAdverisingAndMarketing import (SubscribedContent338393EnabledOn, SubscribedContent338393EnabledOff, SubscribedContent353694EnabledOn, SubscribedContent353694EnabledOff, SubscribedContent353696EnabledOn, SubscribedContent353696EnabledOff,
                                                                                             DisableSoftLandingOn, DisableSoftLandingOff, DisableWindowsSpotlightFeaturesOn, DisableWindowsSpotlightFeaturesOff, DisableWindowsConsumerFeaturesOn, DisableWindowsConsumerFeaturesOff)
from Functions.Privacy.CloudSaving.CloudSaving import (DisableSettingSyncOn, DisableSettingSyncOff, DisableSettingSyncUserOverrideOn, DisableSettingSyncUserOverrideOff, DisableSyncOnPaidNetworkOn, DisableSyncOnPaidNetworkOff, SyncPolicyOn, SyncPolicyOff, DisableApplicationSettingSyncOn, DisableApplicationSettingSyncOff, DisableApplicationSettingSyncUserOverrideOn,
                                                       DisableApplicationSettingSyncUserOverrideOff, DisableAppSyncSettingSyncOn, DisableAppSyncSettingSyncOff, DisableAppSyncSettingSyncUserOverrideOn, DisableAppSyncSettingSyncUserOverrideOff, DisableCredentialsSettingSyncOn, DisableCredentialsSettingSyncOff, DisableCredentialsSettingSyncUserOverrideOn, DisableCredentialsSettingSyncUserOverrideOff,
                                                       EnabledCloudSavingOn, EnabledCloudSavingOff, DisableDesktopThemeSettingSyncOn, DisableDesktopThemeSettingSyncOff, DisableDesktopThemeSettingSyncUserOverrideOn, DisableDesktopThemeSettingSyncUserOverrideOff, DisablePersonalizationSettingSyncOn, DisablePersonalizationSettingSyncOff, DisablePersonalizationSettingSyncUserOverrideOn,
                                                       DisablePersonalizationSettingSyncUserOverrideOff, DisableStartLayoutSettingSyncOn, DisableStartLayoutSettingSyncOff, DisableStartLayoutSettingSyncUserOverrideOn, DisableStartLayoutSettingSyncUserOverrideOff, DisableWebBrowserSettingSyncOn, DisableWebBrowserSettingSyncOff, DisableWebBrowserSettingSyncUserOverrideOn,
                                                       DisableWebBrowserSettingSyncUserOverrideOff, DisableWindowsSettingSyncOn, DisableWindowsSettingSyncOff, DisableWindowsSettingSyncUserOverrideOn, DisableWindowsSettingSyncUserOverrideOff, EnabledLanguageOn, EnabledLanguageOff)
from Functions.Privacy.CloudVoice.CloudVoice import HasAcceptedOn, HasAcceptedOff
from Functions.Privacy.WindowsPrivacyConsentDisclaimer.WindowsPrivacyConsentDisclaimer import AcceptedPrivacyPolicyOn, AcceptedPrivacyPolicyOff
from Functions.Privacy.WindowsFeedbackandDiagnostics.WindowsFeedbackandDiagnostics import (NumberOfSIUFInPeriodOn, NumberOfSIUFInPeriodOff, PeriodInNanoSecondsOn, PeriodInNanoSecondsOff, DoNotShowFeedbackNotificationsOn, DoNotShowFeedbackNotificationsOff, DmClientOnScenarioDownloadOn, DmClientOnScenarioDownloadOff)
from Functions.Privacy.CollectTextMessagesandHandwritingInput.CollectTextMessagesandHandwritingInput import RestrictImplicitInkCollectionOn, RestrictImplicitInkCollectionOff, RestrictImplicitTextCollectionOn, RestrictImplicitTextCollectionOff, HarvestContactsOn, HarvestContactsOff
from Functions.Privacy.Sensor.Sensor import DisableSensorsOn, DisableSensorsOff
from Functions.Privacy.WiFiSense.WiFiSense import value1On, value1Off, value2On, value2Off, AutoConnectAllowedOEMOn, AutoConnectAllowedOEMOff
from Functions.Privacy.HideMostUsedApps.HideMostUsedApps import HideMostUsedAppsOn, HideMostUsedAppsOff
from Functions.Privacy.InventoryCollector.InvenoryCollector import DisableInventoryOn, DisableInventoryOff, ICDeviceOn, ICDeviceOff, DeviceUserOn, DeviceUserOff
from Functions.Privacy.SiteAccessToTheListOfLanguages.SiteAccessToTheListOfLanguages import HttpAcceptLanguageOptOutOn, HttpAcceptLanguageOptOutOff
from Functions.Privacy.RecordingActions.RecordingActions import HttpAcceptLanguageOptOutRAOn, HttpAcceptLanguageOptOutRAOff
from Functions.Privacy.FeedbackAsYouType.FeedbackAsYouType import EnabledFAYTOn, EnabledFAYTOff
from Functions.Privacy.ActivityFeed.ActivityFeed import EnableActivityFeedOn, EnableActivityFeedOff
from Functions.Privacy.ApplicationAccessToLocation.ApplicationAccessToLocation import ValueAATLOn, ValueAATLOff, StatusAATLOn, StatusAATLOff, LetAppsAccessLocationOn, LetAppsAccessLocationOff
from Functions.Privacy.ApplicationAccessToAccountInformation.ApplicationAccessToAccountInformation import ValueAATIOn, ValueAATIOff, LetAppsAccessAccountInfoOn, LetAppsAccessAccountInfoOff
from Functions.Privacy.ApplicationAccessToMotionData.ApplicationAccessToMotionData import ValueAATMDOn, ValueAATMDOff, LetAppsAccessMotionOn, LetAppsAccessMotionOff
from Functions.Privacy.AppAccessToPhone.AppAccessToPhone import LetAppsAccessPhoneOn, LetAppsAccessPhoneOff
from Functions.Privacy.ApplicationAccessToTrustedDevices.ApplicationAccessToTrustedDevices import LetAppsAccessTrustedDevicesOn, LetAppsAccessTrustedDevicesOff
from Functions.Privacy.AppAccessToDeviceSynchronization.AppAccessToDeviceSynchronization import LetAppsSyncWithDevicesOn, LetAppsSyncWithDevicesOff
from Functions.Privacy.ApplicationsAccessDiagnosticInformationAboutOtherApplications.ApplicationsAccessDiagnosticInformationAboutOtherApplications import ValueAADAOAOn, ValueAADAOAOff, LetAppsAccessMotionOn, LetAppsAccessMotionOff
from Functions.Privacy.ApplicationAccessToContacts.ApplicationAccessToContacts import ValueContactOn, ValueContactOff, LetAppsAccessContactsOn, LetAppsAccessContactsOff
from Functions.Privacy.ApplicationAccessToCalendar.ApplicationAccessToCalendar import ValueCalendar1On, ValueCalendar1Off, LetAppsAccessCalendarOn, LetAppsAccessCalendarOff
from Functions.Privacy.ApplicationAccessToCallLog.ApplicationAccessToCallLog import ValueCallAccessOn, ValueCallAccessOff, LetAppsAccessCallHistoryOn, LetAppsAccessCallHistoryOff
from Functions.Privacy.ApplicationAccessToEmail.ApplicationAccessToEmail import ValueEmailOn, ValueEmailOff, LetAppsAccessEmailOn, LetAppsAccessEmailOff
from Functions.Privacy.ApplicationAccessToTasks.ApplicationAccessToTasks import ValueTaskOn, ValueTaskOff, LetAppsAccessTasksOn, LetAppsAccessTasksOff
from Functions.Privacy.ApplicationAccessToMessages.ApplicationAccessToMessages import ValueMessageOn, ValueMessageOff, LetAppsAccessCalendar2On, LetAppsAccessCalendar2Off
from Functions.Privacy.ApplicationAccessToRadio.ApplicationAccessToRadio import ValueRadioOn, ValueRadioOff, LetAppsAccessRadiosOn, LetAppsAccessRadiosOff
from Functions.Privacy.AppAccessToBluetoothDevices.AppAccessToBluetoothDevices import ValueBluetoothOn, ValueBluetoothOff
from Functions.Privacy.ApplicationAccessToTheDocumentsFolder.ApplicationAccessToTheDocumentsFolder import ValueDocsOn, ValueDocsOff
from Functions.Privacy.ApplicationAccessToThePicturesFolder.pushApplicationAccessToThePicturesFolder import ValuePicturesLibraryOn, ValuePicturesLibraryOff
from Functions.Privacy.ApplicationAccessToTheVideosFolder.ApplicationAccessToTheVideosFolder import VideosLibraryOn, VideosLibraryOff
from Functions.Privacy.ApplicationAccessToAnotherFileSystem.ApplicationAccessToAnotherFileSystem import AccessFileSystemOn, AccessFileSystemOff



STATUS_DISABLED = "Disabled"
STATUS_ENABLED = "Enabled"
STATUS_ERROR = "Error"
Bar = 0





class SystemStatus(Enum):
    DISABLED = auto()
    ENABLED = auto()
    ERROR = auto()


def updateMouseAcceleration_back(funct):
    if funct['updateMouseAcceleration'] == STATUS_DISABLED:
        MouseSpeedOn()
        MouseThreshold1On()
        MouseThreshold2On()
    else:
        MouseSpeedOff()
        MouseThreshold1Off()
        MouseThreshold2Off()


def updateProtectionNotifications_back(funct):
    if funct['updateProtectionNotifications'] == STATUS_DISABLED:
        NotificationEnable1On()
        NotificationEnable2On()
        DisableNotifications1On()
    else:
        NotificationEnable1Off()
        NotificationEnable2Off()
        DisableNotifications1Off()


def updateAutoUpdateDriversatSystemstartup_back(funct):
    if funct['updateAutoUpdateDriversatSystemstartup'] == STATUS_DISABLED:
        ExcludeWUDriversInQualityUpdateOn()
        SearchOrderConfigOn()
    else:
        ExcludeWUDriversInQualityUpdateOff()
        SearchOrderConfigOff()



def updateUWP_back(funct):
    if funct['updateUWP'] == STATUS_DISABLED:
        GlobalUserDisabledOn()
        BackgroundAppGlobalToggleStartOn()
        BackgroundAppGlobalToggleOn()
    else:
        GlobalUserDisabledOff()
        GBackgroundAppGlobalToggleStartOff()
        BackgroundAppGlobalToggleOff()



def updateAutoUpdatingAppsStore_back(funct):
    if funct['updateAutoUpdatingAppsStore'] == STATUS_DISABLED:
        AutoDownloadOn()
    else:
        AutoDownloadOff()


def updateAppearance_back(funct):
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


def updateGameBar_back(funct):
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


def updateMultyPlanOverplay_back(funct):
    if funct['updateMultyPlanOverplay'] == STATUS_DISABLED:
        OverlayTestModeOn()
    else:
        OverlayTestModeOff()



def updateWindowsFirewall_back(funct):
    if funct['updateWindowsFirewall'] == STATUS_DISABLED:
        EnableFirewallOn()
        EnableFirewall2On()
    else:
        EnableFirewallOff()
        EnableFirewall2Off()

def updateWindowsUAC_back(funct):
    if funct['updateWindowsUAC'] == STATUS_DISABLED:
        PromptOnSecureDesktopOn()
        ConsentPromptBehaviorAdminOn()
    else:
        PromptOnSecureDesktopOff()
        ConsentPromptBehaviorAdminOff()


def updateSystemResponsiveness_back(funct):
    if funct['updateSystemResponsiveness'] == STATUS_DISABLED:
        SystemResponsivenessEnable()
    else:
        SystemResponsivenessDisable()



def updateWin32_priority_separation_back(funct):
    if funct['updateWin32_priority_separation'] == STATUS_DISABLED:
        set_win32_priority_separation_Disable(2)
    else:
        set_win32_priority_separation_Enable(26)



def updateMeltdownSpectre_back(funct):
    if funct['updateMeltdownSpectre'] == STATUS_DISABLED:
        MeltdownSpectre_Enable()
    else:
        MeltdownSpectre_Disable()



def updateWindowsReservedStorage_back(funct):
    if funct['updateWindowsReservedStorage'] == STATUS_DISABLED:
        disable_reserved_storage()
    else:
        enable_reserved_storage()



def updateSvchost_back(funct):
    if funct['updateSvchost'] == STATUS_DISABLED:
        svc_host_split_threshold_Disable()
    else:
        svc_host_split_threshold_Enable()


def updateUpdateLastNFS_back(funct):
    if funct['updateUpdateLastNFS'] == STATUS_DISABLED:
        nfs_atime_status_windows_Disable()
    else:
        nfs_atime_status_windows_Enable()



def updateConvertNameFile83_back(funct):
    if funct['updateConvertNameFile83'] == STATUS_DISABLED:
        ConvertNameFile83_Disable()
    else:
        ConvertNameFile83_Enable()



def updateDiagnosricEvents_back(funct):
    logs = [
        "Microsoft-Windows-SleepStudy/Diagnostic",
        "Microsoft-Windows-Kernel-Processor-Power/Diagnostic",
        "Microsoft-Windows-UserModePowerService/Diagnostic"
    ]
    if funct['updateDiagnosricEvents'] == STATUS_DISABLED:
        enable_event_viewer_logs(logs)
    else:
        disable_event_viewer_logs(logs)


def updateTasksForAnalysis_back(funct):
    if funct['updateTasksForAnalysis'] == STATUS_DISABLED:
        AnalyzeSystemOn()
        BackupOn()
    else:
        AnalyzeSystemOff()
        BackupOff()



def updateDiagnosticTasks_back(funct):
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



def updateNetPrecompilation_back(funct):
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



def updateAutoProxyDetection_back(funct):
    if funct['updateAutoProxyDetection'] == STATUS_DISABLED:
        ProxyOn()
    else:
        ProxyOff()


def updateInstallingAndRemovingLanguages_back(funct):
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


def updateAutoPerformanceCheck_back(funct):
    if funct['updateAutoPerformanceCheck'] == STATUS_DISABLED:
        WinSATOn()
    else:
        WinSATOff()


def updateMapsLocation_back(funct):
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


def updateRemoteControl_back(funct):
    if funct['updateRemoteControl'] == STATUS_DISABLED:
        RemoteAssistanceTaskOn()
    else:
        RemoteAssistanceTaskOff()


def updateCleaningTasks_back(funct):
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


def updateMicrosoftStore_back(funct):
    if funct['updateMicrosoftStore'] == STATUS_DISABLED:
        enable_microsoft_store()
        enable_microsoft_store2()
    else:
        disable_microsoft_store()
        disable_microsoft_store2()



def updateWindowsXBOX_back(funct):
    if funct['updateWindowsXBOX'] == STATUS_DISABLED:
        enable_xbox()
    else:
        disable_xbox()



def updateTelemetria_back(funct):
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



def updateTelemetriaWebCome_back(funct):
    if funct['updateTelemetriaWebCome'] == STATUS_DISABLED:
        enable_task_schtasks()
        SetEmptyDebuggerOff()
    else:
        disable_task_schtasks()
        SetEmptyDebuggerOn()


def uodateTaskMCA_back(funct):
    if funct['uodateTaskMCA'] == STATUS_DISABLED:
        enable_TaskMCA_CompatibilityAppraiser()
        SetEmptyDebuggerOff()
    else:
        disable_TaskMCA_CompatibilityAppraiser()
        SetEmptyDebuggerOn()


def updateUpdateDateCEIP_back(funct):
    if funct['updateUpdateDateCEIP'] == STATUS_DISABLED:
        enable_ProgramDataUpdater()
    else:
        disable_ProgramDataUpdater()


def updateTaskApplicationImpactTelemetry_back(funct):
    if funct['updateTaskApplicationImpactTelemetry'] == STATUS_DISABLED:
        enable_ait_agent_task()
    else:
        disable_ait_agent_task()



def uodateProductivityAppReminder_back(funct):
    if funct['uodateProductivityAppReminder'] == STATUS_DISABLED:
        enable_StartupAppTask()
    else:
        disable_StartupAppTask()



def updateTaskCEIP_back(funct):
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


def updateCEIPSQM_back(funct):
    if funct['updateCEIPSQM'] == STATUS_DISABLED:
        CEIPSQMOn()
    else:
        CEIPSQMOff()



def updateTelemetrApplicationImpact_back(funct):
    if funct['updateTelemetrApplicationImpact'] == STATUS_DISABLED:
        AITEnableOn()
    else:
        AITEnableOff()



def updateTelemetrNalogDate_back(funct):
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



def updateTelemetrLicense_back(funct):
    if funct['updateTelemetrLicense'] == STATUS_DISABLED:
        NoGenTicketOn()
    else:
        NoGenTicketOff()



def updateWer_back(funct):
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



def updateActiveVoiceForCortan_back(funct):
    if funct['updateActiveVoiceForCortan'] == STATUS_DISABLED:
        AgentActivationEnabledOn()
        LetAppsActivateWithVoiceOn()
        enable_ProgramDataUpdater()
    else:
        AgentActivationEnabledOff()
        LetAppsActivateWithVoiceOff()
        disable_ProgramDataUpdater()



def updateActiveVoiceForCortanBlockSystem_back(funct):
    if funct['updateActiveVoiceForCortanBlockSystem'] == STATUS_DISABLED:
        AgentActivationOnLockScreenEnabledOn()
        LetAppsActivateWithVoiceAboveLockOn()
    else:
        AgentActivationOnLockScreenEnabledOff()
        LetAppsActivateWithVoiceAboveLockOff()



def updateWindowsLocationProvider_back(funct):
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

def updateAllowIndexingEncryptedStoresOrItems_back(funct):
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



def updateTargetedAdverisingAndMarketing_back(funct):
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


def updateCloudSaving_back(funct):
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



def updateCloudVoice_back(funct):
    if funct['updateCloudVoice'] == STATUS_DISABLED:
        HasAcceptedOn()
    else:
        HasAcceptedOff()


def updateWindowsSearchDateCollection_back(funct):
    if funct['updateWindowsSearchDateCollection'] == STATUS_DISABLED:
        AcceptedPrivacyPolicyOn()
    else:
        AcceptedPrivacyPolicyOff()



def updateWindowsPrivacyConsentDisclaimer_back(funct):
    if funct['updateWindowsPrivacyConsentDisclaimer'] == STATUS_DISABLED:
        NumberOfSIUFInPeriodOn()
        PeriodInNanoSecondsOn()
        DoNotShowFeedbackNotificationsOn()
        DmClientOnScenarioDownloadOn()
    else:
        NumberOfSIUFInPeriodOff()
        PeriodInNanoSecondsOff()
        DoNotShowFeedbackNotificationsOff()
        DmClientOnScenarioDownloadOff()




def updateCollectTextMessagesandHandwritingInput_back(funct):
    if funct['updateCollectTextMessagesandHandwritingInput'] == STATUS_DISABLED:
        RestrictImplicitInkCollectionOn()
        RestrictImplicitTextCollectionOn()
        HarvestContactsOn()
    else:
        RestrictImplicitInkCollectionOff()
        RestrictImplicitTextCollectionOff()
        HarvestContactsOff()


def updateSensor_back(funct):
    if funct['updateSensor'] == STATUS_DISABLED:
        DisableSensorsOn()
    else:
        DisableSensorsOff()


def updateWiFiSense_back(funct):
    if funct['updateWiFiSense'] == STATUS_DISABLED:
        value1On()
        value2On()
        AutoConnectAllowedOEMOn()
    else:
        value1Off()
        value2Off()
        AutoConnectAllowedOEMOff()


def updateHideMostUsedApps_back(funct):
    if funct['updateHideMostUsedApps'] == STATUS_DISABLED:
        HideMostUsedAppsOn()
    else:
        HideMostUsedAppsOff()


def updateInventoryCollector_back(funct):
    if funct['updateInventoryCollector'] == STATUS_DISABLED:
        DisableInventoryOn()
        ICDeviceOn()
        DeviceUserOn()
    else:
        DisableInventoryOff()
        ICDeviceOff()
        DeviceUserOff()




def updateSiteAccessToTheListOfLanguages_back(funct):
    if funct['updateSiteAccessToTheListOfLanguages'] == STATUS_DISABLED:
        HttpAcceptLanguageOptOutOn()
    else:
        HttpAcceptLanguageOptOutOff()


def updateRecordingActions_back(funct):
    if funct['updateRecordingActions'] == STATUS_DISABLED:
        HttpAcceptLanguageOptOutRAOn()
    else:
        HttpAcceptLanguageOptOutRAOff()


def updateFeedbackAsYouType_back(funct):
    if funct['updateFeedbackAsYouType'] == STATUS_DISABLED:
        EnabledFAYTOn()
    else:
        EnabledFAYTOff()


def updateActivityFeed_back(funct):
    if funct['updateActivityFeed'] == STATUS_DISABLED:
        EnableActivityFeedOn()
    else:
        EnableActivityFeedOff()


def updateApplicationAccessToLocation_back(funct):
    if funct['updateApplicationAccessToLocation'] == STATUS_DISABLED:
        ValueAATLOn()
        StatusAATLOn()
        LetAppsAccessLocationOn()
    else:
        ValueAATLOff()
        StatusAATLOff()
        LetAppsAccessLocationOff()



def updateApplicationAccessToAccountInformation_back(funct):
    if funct['updateApplicationAccessToAccountInformation'] == STATUS_DISABLED:
        ValueAATIOn()
        LetAppsAccessAccountInfoOn()
    else:
        ValueAATIOff()
        LetAppsAccessAccountInfoOff()


def updateApplicationAccessToMotionData_back(funct):
    if funct['updateApplicationAccessToMotionData'] == STATUS_DISABLED:
        ValueAATMDOn()
        LetAppsAccessMotionOn()
    else:
        LetAppsAccessMotionOff()
        ValueAATMDOff()


def updateAppAccessToPhone_back(funct):
    if funct['updateAppAccessToPhone'] == STATUS_DISABLED:
        LetAppsAccessPhoneOn()
    else:
        LetAppsAccessPhoneOff()



def updateApplicationAccessToTrustedDevices_back(funct):
    if funct['updateApplicationAccessToTrustedDevices'] == STATUS_DISABLED:
        LetAppsAccessTrustedDevicesOn()
    else:
        LetAppsAccessTrustedDevicesOff()



def updateApplicationAccessToDeviceSynchronization_back(funct):
    if funct['updateApplicationAccessToDeviceSynchronization'] == STATUS_DISABLED:
        LetAppsSyncWithDevicesOn()
    else:
        LetAppsSyncWithDevicesOff()


def updateApplicationsAccessDiagnosticInformationAboutOtherApplications_back(funct):
    if funct['updateApplicationsAccessDiagnosticInformationAboutOtherApplications'] == STATUS_DISABLED:
        ValueAADAOAOn()
        LetAppsAccessMotionOn()
    else:
        ValueAADAOAOff()
        LetAppsAccessMotionOff()


def updateApplicationAccessToContacts_back(funct):
    if funct['updateApplicationAccessToContacts'] == STATUS_DISABLED:
        ValueContactOn()
        LetAppsAccessContactsOn()
    else:
        ValueContactOff()
        LetAppsAccessContactsOff()


def updateApplicationAccessToCalendar_back(funct):
    if funct['updateApplicationAccessToCalendar'] == STATUS_DISABLED:
        ValueCalendar1On()
        LetAppsAccessCalendarOn()
    else:
        ValueCalendar1Off()
        LetAppsAccessCalendarOff()



def updateApplicationAccessToCallLog_back(funct):
    if funct['updateApplicationAccessToCallLog'] == STATUS_DISABLED:
        ValueCallAccessOn()
        LetAppsAccessCallHistoryOn()
    else:
        ValueCallAccessOff()
        LetAppsAccessCallHistoryOff()


def updateApplicationAccessToEmail_back(funct):
    if funct['updateApplicationAccessToEmail'] == STATUS_DISABLED:
        ValueEmailOn()
        LetAppsAccessEmailOn()
    else:
        ValueEmailOff()
        LetAppsAccessEmailOff()


def updateApplicationAccessToTasks_back(funct):
    if funct['updateApplicationAccessToTasks'] == STATUS_DISABLED:
        ValueTaskOn()
        LetAppsAccessTasksOn()
    else:
        ValueTaskOff()
        LetAppsAccessTasksOff()


def updateApplicationAccessToMessages_back(funct):
    if funct['updateApplicationAccessToMessages'] == STATUS_DISABLED:
        ValueMessageOn()
        LetAppsAccessCalendar2On()
    else:
        ValueMessageOff()
        LetAppsAccessCalendar2Off()



def updateApplicationAccessToRadio_back(funct):
    if funct['updateApplicationAccessToRadio'] == STATUS_DISABLED:
        ValueRadioOn()
        LetAppsAccessRadiosOn()
    else:
        ValueRadioOff()
        LetAppsAccessRadiosOff()


def updateAppAccessToBluetoothDevices_back(funct):
    if funct['updateAppAccessToBluetoothDevices'] == STATUS_DISABLED:
        ValueBluetoothOn()
    else:
        ValueBluetoothOff()


def updateApplicationAccessToTheDocumentsFolder_back(funct):
    if funct['updateApplicationAccessToTheDocumentsFolder'] == STATUS_DISABLED:
        ValueDocsOn()
    else:
        ValueDocsOff()


def updateApplicationAccessToThePicturesFolder_back(funct):
    if funct['updateApplicationAccessToThePicturesFolder'] == STATUS_DISABLED:
        ValuePicturesLibraryOn()
    else:
        ValuePicturesLibraryOff()


def updateApplicationAccessToTheVideosFolder_back(funct):
    if funct['updateApplicationAccessToTheVideosFolder'] == STATUS_DISABLED:
        VideosLibraryOn()
    else:
        VideosLibraryOff()


def updateApplicationAccessToAnotherFileSystem_back(funct):
    if funct['updateApplicationAccessToAnotherFileSystem'] == STATUS_DISABLED:
        AccessFileSystemOn()
    else:
        AccessFileSystemOff()

