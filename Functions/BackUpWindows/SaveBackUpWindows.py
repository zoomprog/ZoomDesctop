import json
import winreg

from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog
import subprocess
from enum import Enum, auto

from Functions.BaseSettings.MouseAcceleration.MouseAcceleration import SearchMouseSpeed, SearchMouseThreshold1, SearchMouseThreshold2
from Functions.BaseSettings.ProtectionNotifications.ProtectionNotifications import SearchNotificationEnable1, SearchNotificationEnable2, SearchDisableNotifications1
from Functions.BaseSettings.AutoUpdateDriversatSystemstartup.AutoUpdateDriversatSystemstartup import SearchExcludeWUDriversInQualityUpdate, SearchSearchOrderConfig
from Functions.BaseSettings.UWP.UWP import SearchGlobalUserDisabled, SearchBackgroundAppGlobalToggle, SearchBackgroundAppGlobalToggleStart
from Functions.BaseSettings.AutoUpdatingAppsStore.AutoUpdatingAppsStore import SearchAutoDownload
from Functions.BaseSettings.Appearance.Appearance import (SearchTaskbarAnimations, SearchIconsOnly, SearchListviewShadow, SearchListviewAlphaSelect, SearchMinAnimate, SearchDragFullWindows, SearchEnableAeroPeek, SearchFontSmoothing, SearchVisualFXSetting, SearchVisualFXSetting2)
from Functions.BaseSettings.GameBar.GameBar import (SearchAutoGameModeEnabled, SearchGamePanelStartupTipIndex, SearchShowStartupPanel, SearchUseNexusForGameBarEnabled, SearchAllowAutoGameMode, SearchAllowGameDVR, SearchAppCaptureEnabled, SearchValueGameBar)
from Functions.BaseSettings.MultyPlanOverplay.MultyPlanOverplay import SearchOverlayTestMode
from Functions.BaseSettings.WindowsFirewall.WindowsFirewall import SearchEnableFirewall, SearchEnableFirewall2
from Functions.BaseSettings.UAC.UAC import SearchPromptOnSecureDesktop, SearchConsentPromptBehaviorAdmin
from Functions.Twics.Search.SearchSystemResponsiveness import SystemResponsivenessSearch
from Functions.Twics.Search.SearchWin32PrioritySeparation import get_win32_priority_separation_Search
from Functions.Twics.Search.SearchMeltdownSpectre import MeltdownSpectre_Search
from Functions.Twics.Search.SearchWindowsReservedStorage import check_reserved_storage_Search
from Functions.Twics.Search.SearchSvchost import check_svc_host_split_threshold_Search
from Functions.Twics.Search.SearchUpdateLastNFS import nfs_atime_status_windows_Update
from Functions.Twics.Search.SearchConvertNameFile83 import ConvertNameFile83_Update
from Functions.Twics.Search.SearchDiagnosricEvents import check_logs_status
from Functions.Task.TasksForAnalysis.TasksForAnalysis import SearchAnalyzeSystem, SearchBackup
from Functions.Task.DiagnosticTasks.DiagnosticTasks import SearchProactiveScan
from Functions.Task.DiagnosticTasks.DiagnosticTasks import (SearchRecommendedTroubleshootingScanner, SearchMicrosoftWindowsDiskDiagnosticDataCollector, SearchScheduled, SearchMicrosoftWindowsDiskDiagnosticResolver, SearchDiagnostics, SearchStorageSense, SearchRunFullMemoryDiagnostic, SearchProcessMemoryDiagnosticEvents, SearchAnalyzeSystemTask, SearchBgTaskRegistrationMaintenanceTask,
                                                            Searchappuriverifierdaily, SearchUsageDataReporting, SearchCalibrationLoader)
from Functions.Task.NetPrecompilation.NetPrecompilation import (SearchNETFrameworkNGENv4030319, SearchNETFrameworkNGENv403031964, SearchNETFrameworkNGENv403031964Critical, NETFrameworkNGENv403031964CriticalOn, NETFrameworkNGENv403031964Criticaloff,
                                                                SearchNETFrameworkNGENv4030319Critical)
from Functions.Task.AutoProxyDetection.AutoProxyDetection import SearchProxy
from Functions.Task.InstallingAndRemovingLanguages.InstallingAndRemovingLanguages import (SearchSynchronizLanguageSettings, SearchInstallation, SearchReconcileLanguageResources, SearchUninstallation, SearchLPRemove)
from Functions.Task.AutoPerformanceCheck.AutoPerformanceCheck import SearchWinSAT
from Functions.Task.MapsLocation.MapsLocation import SearchMapsToastTask, SearchMapsUpdateTask, SearchNotifications, SearchWindowsActionDialog
from Functions.Task.RemoteControl.RemoteControl import SearchRemoteAssistanceTask
from Functions.Task.CleaningTasks.CleaningTasks import SearchCleanupTemporaryState, SearchDsSvcCleanup, SearchSilentCleanup, SearchCleanupOfflineContent, SearchCacheTask
from Functions.Task.OnOffMicrosoftStore.MicrosoftStore import check_microsoft_store_status, check_microsoft_store_status2
from Functions.Task.Xbox.Xbox import check_xbox_status
from Functions.Privacy.Telemetria.Telemetria import SearchStart1, SearchStart2, SearchStart3, SearchStart4
from Functions.Privacy.TelemetriaWebCome.TelemetriaWebCome import check_task_status, SearchSetEmptyDebugger
from Functions.Privacy.TaskMCA.TaskMCA import check_TaskMCA_status_CompatibilityAppraiser
from Functions.Privacy.UpdateDateCEIP.UpdateDateCEIP import check_ProgramDataUpdater
from Functions.Privacy.TaskApplicationImpactTelemetry.TaskApplicationImpactTelemetry import check_ait_agent_task
from Functions.Privacy.ProductivityAppReminder.ProductivityAppReminder import check_StartupAppTask
from Functions.Privacy.TaskCEIP.TaskCEIP import check_Proxy, check_BthSQM, check_Consolidator, check_KernelCeipTask, check_UsbCeip
from Functions.Privacy.CEIPSQM.CEIPSQM import SearchCEIPSQM
from Functions.Privacy.TelemetrApplicationImpact.TelemetrApplicationImpact import SearchAITEnable
from Functions.Privacy.TelemetrNalogDate.TelemetrNalogDate import SearchAllowTelemetry, SearchAllowTelemetry2, SearchAllowTelemetry3, SearchLimitEnhancedDiagnosticDataWindowsAnalytics
from Functions.Privacy.TelemetrLicense.TelemetrLicense import SearchNoGenTicket
from Functions.Privacy.WER.WER import SearchDisabled, SearchDisabled2, SearchDefaultConsent, SearchDefaultOverrideBehavior, SearchDontSendAdditionalData, SearchLoggingDisabled, SearchStartWER, SearchStartWER2, check_QueueReporting
from Functions.Privacy.ActiveVoiceForCortan.ActiveVoiceForCortan import SearchAgentActivationEnabled, SearchLetAppsActivateWithVoice, check_ProgramDataUpdater
from Functions.Privacy.ActiveVoiceForCortanBlockSystem.ActiveVoiceForCortanBlockSystem import SearchAgentActivationOnLockScreenEnabled, SearchLetAppsActivateWithVoiceAboveLock
from Functions.Privacy.WindowsLocationProvider.WindowsLocationProvider import SearchDisableWindowsLocationProvider, SearchDisableLocationScripting, SearchDisableLocation, SearchSensorPermissionState, SearchSensorPermissionState2
from Functions.Privacy.AllowIndexingEncryptedStoresOrItems.AllowIndexingEncryptedStoresOrItems import SearchAllowIndexingEncryptedStoresOrItems, SearchAlwaysUseAutoLangDetection, SearchAllowSearchToUseLocation, SearchDisableWebSearch1, SearchConnectedSearchUseWeb, SearchBingSearchEnabled
from Functions.Privacy.TargetedAdverisingAndMarketing.TargetedAdverisingAndMarketing import (SearchSubscribedContent338393Enabled, SearchSubscribedContent353694Enabled, SearchSubscribedContent353696Enabled, SearchDisableSoftLanding, SearchDisableWindowsSpotlightFeatures, SearchDisableWindowsConsumerFeatures)
from Functions.Privacy.CloudSaving.CloudSaving import (SearchDisableSettingSync, SearchDisableSettingSyncUserOverride, SearchDisableSyncOnPaidNetwork, SearchSyncPolicy, SearchDisableApplicationSettingSync, SearchDisableApplicationSettingSyncUserOverride, SearchDisableAppSyncSettingSync, SearchDisableAppSyncSettingSyncUserOverride, SearchDisableCredentialsSettingSync,
                                                       SearchDisableCredentialsSettingSyncUserOverride, SearchEnabledCloudSaving, SearchDisableDesktopThemeSettingSync, SearchDisableDesktopThemeSettingSyncUserOverride, SearchDisablePersonalizationSettingSync, SearchDisablePersonalizationSettingSyncUserOverride, SearchDisableStartLayoutSettingSync, SearchDisableStartLayoutSettingSyncUserOverride,
                                                       SearchDisableWebBrowserSettingSync, SearchDisableWebBrowserSettingSyncUserOverride, SearchDisableWindowsSettingSync, SearchDisableWindowsSettingSyncUserOverride, SearchEnabledLanguage)
from Functions.Privacy.CloudVoice.CloudVoice import SearchHasAccepted
from Functions.Privacy.WindowsPrivacyConsentDisclaimer.WindowsPrivacyConsentDisclaimer import SearchAcceptedPrivacyPolicy
from Functions.Privacy.WindowsFeedbackandDiagnostics.WindowsFeedbackandDiagnostics import (SearchNumberOfSIUFInPeriod, SearchPeriodInNanoSeconds, SearchDoNotShowFeedbackNotifications, SearchDmClient, SearchDmClientOnScenarioDownload)
from Functions.Privacy.CollectTextMessagesandHandwritingInput.CollectTextMessagesandHandwritingInput import SearchRestrictImplicitInkCollection, SearchRestrictImplicitTextCollection, SearchHarvestContacts
from Functions.Privacy.Sensor.Sensor import SearchDisableSensors
from Functions.Privacy.WiFiSense.WiFiSense import Searchvalue1, Searchvalue2, SearchAutoConnectAllowedOEM
from Functions.Privacy.HideMostUsedApps.HideMostUsedApps import SearchHideMostUsedApps
from Functions.Privacy.InventoryCollector.InvenoryCollector import SearchDisableInventory, ICDeviceSearch, DeviceUserSearch
from Functions.Privacy.SiteAccessToTheListOfLanguages.SiteAccessToTheListOfLanguages import SearchHttpAcceptLanguageOptOut
from Functions.Privacy.RecordingActions.RecordingActions import SearchHttpAcceptLanguageOptOutRAOut
from Functions.Privacy.FeedbackAsYouType.FeedbackAsYouType import SearchEnabledFAYT
from Functions.Privacy.ActivityFeed.ActivityFeed import SearchEnableActivityFeed
from Functions.Privacy.ApplicationAccessToLocation.ApplicationAccessToLocation import SearchValueAATL, SearchStatusAATL, SearchLetAppsAccessLocation
from Functions.Privacy.ApplicationAccessToAccountInformation.ApplicationAccessToAccountInformation import SearchValueAATI, SearchLetAppsAccessAccountInfo
from Functions.Privacy.ApplicationAccessToMotionData.ApplicationAccessToMotionData import SearchValueAATMD, SearchLetAppsAccessMotion
from Functions.Privacy.AppAccessToPhone.AppAccessToPhone import SearchLetAppsAccessPhone
from Functions.Privacy.ApplicationAccessToTrustedDevices.ApplicationAccessToTrustedDevices import SearchLetAppsAccessTrustedDevices
from Functions.Privacy.AppAccessToDeviceSynchronization.AppAccessToDeviceSynchronization import SearchLetAppsSyncWithDevices
from Functions.Privacy.ApplicationsAccessDiagnosticInformationAboutOtherApplications.ApplicationsAccessDiagnosticInformationAboutOtherApplications import SearchValueAADAOA, SearchLetAppsAccessMotion
from Functions.Privacy.ApplicationAccessToContacts.ApplicationAccessToContacts import SearchalueContact, SearchLetAppsAccessContacts
from Functions.Privacy.ApplicationAccessToCalendar.ApplicationAccessToCalendar import SearchValueCalendar1, SearchLetAppsAccessCalendar
from Functions.Privacy.ApplicationAccessToCallLog.ApplicationAccessToCallLog import SearchValueCallAccess, SearchLetAppsAccessCallHistory
from Functions.Privacy.ApplicationAccessToEmail.ApplicationAccessToEmail import SearchValueEmail, SearchLetAppsAccessEmail
from Functions.Privacy.ApplicationAccessToTasks.ApplicationAccessToTasks import SearchValueTask, SearchLetAppsAccessTasks
from Functions.Privacy.ApplicationAccessToMessages.ApplicationAccessToMessages import SearchValueMessage, SearchLetAppsAccessCalendar2
from Functions.Privacy.ApplicationAccessToRadio.ApplicationAccessToRadio import SearchValueRadio, SearchLetAppsAccessRadios
from Functions.Privacy.AppAccessToBluetoothDevices.AppAccessToBluetoothDevices import SearchValueBluetooth
from Functions.Privacy.ApplicationAccessToTheDocumentsFolder.ApplicationAccessToTheDocumentsFolder import SearchValueDocs
from Functions.Privacy.ApplicationAccessToThePicturesFolder.pushApplicationAccessToThePicturesFolder import SearchValuePicturesLibrary
from Functions.Privacy.ApplicationAccessToTheVideosFolder.ApplicationAccessToTheVideosFolder import SearchVideosLibrary
from Functions.Privacy.ApplicationAccessToAnotherFileSystem.ApplicationAccessToAnotherFileSystem import SearchAccessFileSystem

STATUS_DISABLED = "Disabled"
STATUS_ENABLED = "Enabled"
STATUS_ERROR = "Error"
Bar = 0


class SystemStatus(Enum):
    DISABLED = auto()
    ENABLED = auto()
    ERROR = auto()


def updateMouseAcceleration():
    global Bar
    result1 = SearchMouseSpeed()
    result2 = SearchMouseThreshold1()
    result3 = SearchMouseThreshold2()
    if result1 and result2 and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED

def updateProtectionNotifications():
    global Bar
    result1 = SearchNotificationEnable1()
    result2 = SearchNotificationEnable2()
    result3 = SearchDisableNotifications1()
    if result1 and result2 and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAutoUpdateDriversatSystemstartup():
    global Bar
    result1 = SearchExcludeWUDriversInQualityUpdate()
    result2 = SearchSearchOrderConfig()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateUWP():
    global Bar
    result1 = SearchGlobalUserDisabled()
    result2 = SearchBackgroundAppGlobalToggleStart()
    result3 = SearchBackgroundAppGlobalToggle()
    if result1 and result2 and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAutoUpdatingAppsStore():
    global Bar
    result = SearchAutoDownload()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAppearance():
    global Bar
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
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateGameBar():
    global Bar
    result1 = SearchAutoGameModeEnabled()
    result2 = SearchGamePanelStartupTipIndex()
    result3 = SearchShowStartupPanel()
    result4 = SearchUseNexusForGameBarEnabled()
    result5 = SearchAllowAutoGameMode()
    result6 = SearchAllowGameDVR()
    result7 = SearchAppCaptureEnabled()
    result8 = SearchValueGameBar()
    if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateMultyPlanOverplay():
    global Bar
    result = SearchOverlayTestMode()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWindowsFirewall():
    global Bar
    result1 = SearchEnableFirewall()
    result2 = SearchEnableFirewall2()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWindowsUAC():
    global Bar
    result1 = SearchPromptOnSecureDesktop()
    result2 = SearchConsentPromptBehaviorAdmin()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateSystemResponsiveness():
    global Bar
    result = SystemResponsivenessSearch()
    status = result.get("SystemResponsiveness", STATUS_ERROR)
    if status == "Disable":
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWin32_priority_separation():
    global Bar
    result = get_win32_priority_separation_Search()
    if result is not None:
        if result == 26:
            return STATUS_DISABLED
        elif result == 2:
            return STATUS_ENABLED
        else:
            print(f"{result}")
    else:
        print('Не удалось получитьзначения Win32')


def updateMeltdownSpectre():
    global Bar
    result = MeltdownSpectre_Search()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWindowsReservedStorage():
    global Bar
    result = check_reserved_storage_Search()
    if result == STATUS_ENABLED:
        return STATUS_ENABLED
    else:
        return STATUS_DISABLED

def updateSvchost():
    global Bar
    result = check_svc_host_split_threshold_Search()
    if result == STATUS_ENABLED:
        return STATUS_ENABLED
    else:
        return STATUS_DISABLED


def updateUpdateLastNFS():
    global Bar
    result = nfs_atime_status_windows_Update()
    if result == 1:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateConvertNameFile83():
    global Bar
    result = ConvertNameFile83_Update()
    if result == 1:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateDiagnosricEvents():
    global Bar
    logs = [
        "Microsoft-Windows-SleepStudy/Diagnostic",
        "Microsoft-Windows-Kernel-Processor-Power/Diagnostic",
        "Microsoft-Windows-UserModePowerService/Diagnostic"
    ]
    result = check_logs_status(logs)
    if all(status == 'Disabled' for status in result):
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTasksForAnalysis():
    global Bar
    result1 = SearchAnalyzeSystem()
    result2 = SearchBackup()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateDiagnosticTasks():
    global Bar
    result1 = SearchProactiveScan()
    result2 = SearchRecommendedTroubleshootingScanner()
    result3 = SearchMicrosoftWindowsDiskDiagnosticDataCollector()
    result4 = SearchScheduled()
    result5 = SearchMicrosoftWindowsDiskDiagnosticResolver()
    result6 = SearchDiagnostics()
    result7 = SearchStorageSense()
    result8 = SearchRunFullMemoryDiagnostic()
    result9 = SearchProcessMemoryDiagnosticEvents()
    result10 = SearchAnalyzeSystemTask()
    result11 = SearchBgTaskRegistrationMaintenanceTask()
    result12 = Searchappuriverifierdaily()
    result13 = SearchUsageDataReporting()
    result14 = SearchCalibrationLoader()
    if result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9 and result10 and result11 and result12 and result13 and result14 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateNetPrecompilation():
    global Bar
    result1 = SearchNETFrameworkNGENv4030319()
    result2 = SearchNETFrameworkNGENv403031964()
    result3 = SearchNETFrameworkNGENv403031964Critical()
    result4 = SearchNETFrameworkNGENv4030319Critical()
    if result1 and result2 and result3 and result4 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAutoProxyDetection():
    global Bar
    result = SearchProxy()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateInstallingAndRemovingLanguages():
    global Bar
    result1 = SearchSynchronizLanguageSettings()
    result2 = SearchInstallation()
    result3 = SearchReconcileLanguageResources()
    result4 = SearchUninstallation()
    result5 = SearchLPRemove()
    if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAutoPerformanceCheck():
    global Bar
    result = SearchWinSAT()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateMapsLocation():
    global Bar
    result1 = SearchMapsToastTask()
    result2 = SearchMapsUpdateTask()
    result3 = SearchNotifications()
    result4 = SearchWindowsActionDialog()
    if result1 and result2 and result3 and result4 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateRemoteControl():
    global Bar
    result = SearchRemoteAssistanceTask()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateCleaningTasks():
    global Bar
    result1 = SearchCleanupTemporaryState()
    result2 = SearchDsSvcCleanup()
    result3 = SearchSilentCleanup()
    result4 = SearchCleanupOfflineContent()
    result5 = SearchCacheTask()
    if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateMicrosoftStore():
    global Bar
    result = check_microsoft_store_status()
    result2 = check_microsoft_store_status2()
    if result and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWindowsXBOX():
    global Bar
    result = check_xbox_status()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTelemetria():
    global Bar
    result1 = SearchStart1()
    result2 = SearchStart2()
    result3 = SearchStart3()
    result4 = SearchStart4()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTelemetriaWebCome():
    global Bar
    result1 = SearchSetEmptyDebugger()
    result2 = check_task_status()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def uodateTaskMCA():
    global Bar
    result1 = check_TaskMCA_status_CompatibilityAppraiser()
    result2 = SearchSetEmptyDebugger()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateUpdateDateCEIP():
    global Bar
    result = check_ProgramDataUpdater()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTaskApplicationImpactTelemetry():
    global Bar
    result = check_ait_agent_task()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def uodateProductivityAppReminder():
    global Bar
    result = check_StartupAppTask()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTaskCEIP():
    global Bar
    result1 = check_Proxy()
    result2 = check_BthSQM()
    result3 = check_Consolidator()
    result4 = check_KernelCeipTask()
    result5 = check_UsbCeip()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateCEIPSQM():
    global Bar
    result = SearchCEIPSQM()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTelemetrApplicationImpact():
    global Bar
    result = SearchAITEnable()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTelemetrNalogDate():
    global Bar
    result1 = SearchAllowTelemetry()
    result2 = SearchAllowTelemetry2()
    result3 = SearchAllowTelemetry3()
    result4 = SearchLimitEnhancedDiagnosticDataWindowsAnalytics()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTelemetrLicense():
    global Bar
    result = SearchNoGenTicket()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWer():
    global Bar
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
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateActiveVoiceForCortan():
    global Bar
    result1 = SearchAgentActivationEnabled()
    result2 = SearchLetAppsActivateWithVoice()
    result3 = check_ProgramDataUpdater()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateActiveVoiceForCortanBlockSystem():
    global Bar
    result1 = SearchAgentActivationOnLockScreenEnabled()
    result2 = SearchLetAppsActivateWithVoiceAboveLock()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWindowsLocationProvider():
    global Bar
    result1 = SearchDisableWindowsLocationProvider()
    result2 = SearchDisableLocationScripting()
    result3 = SearchDisableLocation()
    result4 = SearchSensorPermissionState()
    result5 = SearchSensorPermissionState2()
    if result5 == STATUS_DISABLED and result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAllowIndexingEncryptedStoresOrItems():
    global Bar
    result1 = SearchAllowIndexingEncryptedStoresOrItems()
    result2 = SearchAlwaysUseAutoLangDetection()
    result3 = SearchAllowSearchToUseLocation()
    result4 = SearchDisableWebSearch1()
    result5 = SearchConnectedSearchUseWeb()
    result6 = SearchBingSearchEnabled()
    if result1 == STATUS_DISABLED and result2 == STATUS_DISABLED and result3 == STATUS_DISABLED and result4 == STATUS_DISABLED and result5 == STATUS_DISABLED and result6 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateTargetedAdverisingAndMarketing():
    global Bar
    result1 = SearchSubscribedContent338393Enabled()
    result2 = SearchSubscribedContent353694Enabled()
    result3 = SearchSubscribedContent353696Enabled()
    result4 = SearchDisableSoftLanding()
    result5 = SearchDisableWindowsSpotlightFeatures()
    result6 = SearchDisableWindowsConsumerFeatures()
    if result1 and result2 and result3 and result4 and result5 and result6 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateCloudSaving():
    global Bar
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
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateCloudVoice():
    global Bar
    result = SearchHasAccepted()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWindowsSearchDateCollection():
    global Bar
    result = SearchAcceptedPrivacyPolicy()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWindowsPrivacyConsentDisclaimer():
    global Bar
    result1 = SearchNumberOfSIUFInPeriod()
    result2 = SearchPeriodInNanoSeconds()
    result3 = SearchDoNotShowFeedbackNotifications()
    result4 = SearchDmClient()
    result5 = SearchDmClientOnScenarioDownload()
    if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateCollectTextMessagesandHandwritingInput():
    global Bar
    result1 = SearchRestrictImplicitInkCollection()
    result2 = SearchRestrictImplicitTextCollection()
    result3 = SearchHarvestContacts()
    if result1 and result2 and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateSensor():
    global Bar
    result = SearchDisableSensors()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateWiFiSense():
    global Bar
    result1 = Searchvalue1()
    result2 = Searchvalue2()
    result3 = SearchAutoConnectAllowedOEM()
    if result1 and result2 and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateHideMostUsedApps():
    global Bar
    result1 = SearchHideMostUsedApps()
    if result1 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateInventoryCollector():
    global Bar
    result1 = SearchDisableInventory()
    result2 = ICDeviceSearch()
    result3 = DeviceUserSearch()
    if result1 and result2 and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateSiteAccessToTheListOfLanguages():
    global Bar
    result = SearchHttpAcceptLanguageOptOut()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateRecordingActions():
    global Bar
    result = SearchHttpAcceptLanguageOptOutRAOut()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateFeedbackAsYouType():
    global Bar
    result = SearchEnabledFAYT()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateActivityFeed():
    global Bar
    result = SearchEnableActivityFeed()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToLocation():
    global Bar
    result1 = SearchValueAATL()
    result2 = SearchStatusAATL()
    result3 = SearchLetAppsAccessLocation()
    if result1 and result2 and result3 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToAccountInformation():
    global Bar
    result1 = SearchValueAATI()
    result2 = SearchLetAppsAccessAccountInfo()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToMotionData():
    global Bar
    result1 = SearchValueAATMD()
    result2 = SearchLetAppsAccessMotion()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAppAccessToPhone():
    global Bar
    result = SearchLetAppsAccessPhone()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToTrustedDevices():
    global Bar
    result = SearchLetAppsAccessTrustedDevices()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToDeviceSynchronization():
    global Bar
    result = SearchLetAppsSyncWithDevices()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationsAccessDiagnosticInformationAboutOtherApplications():
    global Bar
    result1 = SearchValueAADAOA()
    result2 = SearchLetAppsAccessMotion()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToContacts():
    global Bar
    result1 = SearchalueContact()
    result2 = SearchLetAppsAccessContacts()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToCalendar():
    global Bar
    result1 = SearchValueCalendar1()
    result2 = SearchLetAppsAccessCalendar()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToCallLog():
    global Bar
    result1 = SearchValueCallAccess()
    result2 = SearchLetAppsAccessCallHistory()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToEmail():
    global Bar
    result1 = SearchValueEmail()
    result2 = SearchLetAppsAccessEmail()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToTasks():
    global Bar
    result1 = SearchValueTask()
    result2 = SearchLetAppsAccessTasks()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToMessages():
    global Bar
    result1 = SearchValueMessage()
    result2 = SearchLetAppsAccessCalendar2()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToRadio():
    global Bar
    result1 = SearchValueRadio()
    result2 = SearchLetAppsAccessRadios()
    if result1 and result2 == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateAppAccessToBluetoothDevices():
    global Bar
    result = SearchValueBluetooth()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToTheDocumentsFolder():
    global Bar
    result = SearchValueDocs()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToThePicturesFolder():
    global Bar
    result = SearchValuePicturesLibrary()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToTheVideosFolder():
    global Bar
    result = SearchVideosLibrary()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED


def updateApplicationAccessToAnotherFileSystem():
    global Bar
    result = SearchAccessFileSystem()
    if result == STATUS_DISABLED:
        return STATUS_DISABLED
    else:
        return STATUS_ENABLED




data = {
    'updateMouseAcceleration': str(updateMouseAcceleration()),
    'updateProtectionNotifications': str(updateProtectionNotifications()),
    'updateAutoUpdateDriversatSystemstartup': str(updateAutoUpdateDriversatSystemstartup()),
    'updateUWP': str(updateUWP()),
    'updateAutoUpdatingAppsStore': str(updateAutoUpdatingAppsStore()),
    'updateAppearance': str(updateAppearance()),
    'updateGameBar': str(updateGameBar()),
    'updateMultyPlanOverplay': str(updateMultyPlanOverplay()),
    'updateWindowsFirewall': str(updateWindowsFirewall()),
    'updateWindowsUAC': str(updateWindowsUAC()),
    'updateDiagnosricEvents': str(updateDiagnosricEvents()),
    'updateConvertNameFile83': str(updateConvertNameFile83()),
    'updateUpdateLastNFS': str(updateUpdateLastNFS()),
    'updateSvchost': str(updateSvchost()),
    'updateWindowsReservedStorage': str(updateWindowsReservedStorage()),
    'updateMeltdownSpectre': str(updateMeltdownSpectre()),
    'updateWin32_priority_separation': str(updateWin32_priority_separation()),
    'updateSystemResponsiveness': str(updateSystemResponsiveness()),
    'updateTasksForAnalysis': str(updateTasksForAnalysis()),
    'updateDiagnosticTasks': str(updateDiagnosticTasks()),
    'updateNetPrecompilation': str(updateNetPrecompilation()),
    'updateAutoProxyDetection': str(updateAutoProxyDetection()),
    'updateInstallingAndRemovingLanguages': str(updateInstallingAndRemovingLanguages()),
    'updateAutoPerformanceCheck': str(updateAutoPerformanceCheck()),
    'updateMapsLocation': str(updateMapsLocation()),
    'updateRemoteControl': str(updateRemoteControl()),
    'updateCleaningTasks': str(updateCleaningTasks()),
    'updateMicrosoftStore': str(updateMicrosoftStore()),
    'updateWindowsXBOX': str(updateWindowsXBOX()),
    'updateTelemetria': str(updateTelemetria()),
    'updateTelemetriaWebCome': str(updateTelemetriaWebCome()),
    'uodateTaskMCA': str(uodateTaskMCA()),
    'updateUpdateDateCEIP': str(updateUpdateDateCEIP()),
    'updateTaskApplicationImpactTelemetry': str(updateTaskApplicationImpactTelemetry()),
    'uodateProductivityAppReminder': str(uodateProductivityAppReminder()),
    'updateTaskCEIP': str(updateTaskCEIP()),
    'updateCEIPSQM': str(updateCEIPSQM()),
    'updateTelemetrApplicationImpact': str(updateTelemetrApplicationImpact()),
    'updateTelemetrNalogDate': str(updateTelemetrNalogDate()),
    'updateTelemetrLicense': str(updateTelemetrLicense()),
    'updateActiveVoiceForCortan': str(updateActiveVoiceForCortan()),
    'updateWer': str(updateWer()),
    'updateActiveVoiceForCortanBlockSystem': str(updateActiveVoiceForCortanBlockSystem()),
    'updateWindowsLocationProvider': str(updateWindowsLocationProvider()),
    'updateAllowIndexingEncryptedStoresOrItems': str(updateAllowIndexingEncryptedStoresOrItems()),
    'updateTargetedAdverisingAndMarketing': str(updateTargetedAdverisingAndMarketing()),
    'updateCloudSaving': str(updateCloudSaving()),
    'updateCloudVoice': str(updateCloudVoice()),
    'updateWindowsSearchDateCollection': str(updateWindowsSearchDateCollection()),
    'updateWindowsPrivacyConsentDisclaimer': str(updateWindowsPrivacyConsentDisclaimer()),
    'updateCollectTextMessagesandHandwritingInput': str(updateCollectTextMessagesandHandwritingInput()),
    'updateSensor': str(updateSensor()),
    'updateWiFiSense': str(updateWiFiSense()),
    'updateHideMostUsedApps': str(updateHideMostUsedApps()),
    'updateInventoryCollector': str(updateInventoryCollector()),
    'updateSiteAccessToTheListOfLanguages': str(updateSiteAccessToTheListOfLanguages()),
    'updateRecordingActions': str(updateRecordingActions()),
    'updateFeedbackAsYouType': str(updateFeedbackAsYouType()),
    'updateActivityFeed': str(updateActivityFeed()),
    'updateApplicationAccessToLocation': str(updateApplicationAccessToLocation()),
    'updateApplicationAccessToAccountInformation': str(updateApplicationAccessToAccountInformation()),
    'updateApplicationAccessToMotionData': str(updateApplicationAccessToMotionData()),
    'updateAppAccessToPhone': str(updateAppAccessToPhone()),
    'updateApplicationAccessToTrustedDevices': str(updateApplicationAccessToTrustedDevices()),
    'updateApplicationAccessToDeviceSynchronization': str(updateApplicationAccessToDeviceSynchronization()),
    'updateApplicationsAccessDiagnosticInformationAboutOtherApplications': str(updateApplicationsAccessDiagnosticInformationAboutOtherApplications()),
    'updateApplicationAccessToContacts': str(updateApplicationAccessToContacts()),
    'updateApplicationAccessToCalendar': str(updateApplicationAccessToCalendar()),
    'updateApplicationAccessToCallLog': str(updateApplicationAccessToCallLog()),
    'updateApplicationAccessToEmail': str(updateApplicationAccessToEmail()),
    'updateApplicationAccessToTasks': str(updateApplicationAccessToTasks()),
    'updateApplicationAccessToMessages': str(updateApplicationAccessToMessages()),
    'updateApplicationAccessToRadio': str(updateApplicationAccessToRadio()),
    'updateAppAccessToBluetoothDevices': str(updateAppAccessToBluetoothDevices()),
    'updateApplicationAccessToTheDocumentsFolder': str(updateApplicationAccessToTheDocumentsFolder()),
    'updateApplicationAccessToThePicturesFolder': str(updateApplicationAccessToThePicturesFolder()),
    'updateApplicationAccessToAnotherFileSystem': str(updateApplicationAccessToAnotherFileSystem())
}
# Сериализуем данные в строку в формате JSON и записываем в файл
with open('BakUpFile\BKFILE.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
