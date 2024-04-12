import sys

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

from PyQt6.QtWidgets import QApplication, QDialog
from SettingsWidjets.Task import Ui_Task
from enum import Enum, auto


class SystemStatus(Enum):
    DISABLED = auto()
    ENABLED = auto()
    ERROR = auto()


# Constants for repeated strings
STATUS_DISABLED = "Disabled"
STATUS_ENABLED = "Enabled"
STATUS_ERROR = "Error"

class Task(QDialog, Ui_Task):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.positionButton()
        self.positionTextLabel()

        self.updateTasksForAnalysis()
        self.updateDiagnosticTasks()
        self.updateNetPrecompilation()
        self.updateAutoProxyDetection()
        self.updateInstallingAndRemovingLanguages()
        self.updateAutoPerformanceCheck()
        self.updateMapsLocation()
        self.updateRemoteControl()
        self.updateCleaningTasks()
        self.updateMicrosoftStore()
        self.updateWindowsXBOX()


        self.pushTasksForAnalysis.clicked.connect(self.tasksForAnalysisButtonClick)
        self.pushDiagnosticTasks.clicked.connect(self.diagnosticTasksButtonClick)
        self.pushNetPrecompilation.clicked.connect(self.NetPrecompilationButtonClick)
        self.pushAutoProxyDetection.clicked.connect(self.AutoProxyDetectionButtonClick)
        self.pushInstallingAndRemovingLanguages.clicked.connect(self.InstallingAndRemovingLanguagesButtonClick)
        self.pushAutoPerformanceCheck.clicked.connect(self.AutoPerformanceCheckButtonClick)
        self.pushMapsLocation.clicked.connect(self.MapsLocationButtonClick)
        self.pushRemoteControl.clicked.connect(self.RemoteControlButtonClick)
        self.pushCleaningTasks.clicked.connect(self.CleaningTasksButtonClick)
        self.pushMicrosoftStore.clicked.connect(self.MicrosoftStoreButtonClick)
        self.pushWindowsXBOX.clicked.connect(self.WindowsXBOXButtonClick)

    def positionTextLabel(self):
        TextLabel_list = [
            "labelTasksForAnalysis",
            "labelDiagnosticTasks",
            "labelNetPrecompilation",
            "labelAutoProxyDetection",
            "labelInstallingAndRemovingLanguages",
            "labelAutoPerformanceCheck",
            "labelMapsLocation",
            "labelRemoteControl",
            "labelMicrosoftSync",
            "labelCleaningTasks",
            "labelMicrosoftStore",
            "labelWindowsXBOX"
        ]
        x_position = 600
        # Loop through button names and set their position
        for button_name in TextLabel_list:
            button = getattr(self, button_name)
            button.move(x_position, 7)

    def positionButton(self):
        frame_list = [
            "pushTasksForAnalysis",
            "pushDiagnosticTasks",
            "pushNetPrecompilation",
            "pushAutoProxyDetection",
            "pushInstallingAndRemovingLanguages",
            "pushAutoPerformanceCheck",
            "pushMapsLocation",
            "pushRemoteControl",
            "pushMicrosoftSync",
            "pushCleaningTasks",
            "pushMicrosoftStore",
            "pushWindowsXBOX"
        ]
        x_position = 780
        for button_name in frame_list:
            button = getattr(self, button_name)
            button.move(x_position, 7)

    def updateTasksForAnalysis(self):
        result1 = SearchAnalyzeSystem()
        result2 = SearchBackup()
        if result1 and result2 == STATUS_DISABLED:
            self.labelTasksForAnalysis.setText(STATUS_DISABLED)
            self.labelTasksForAnalysis.setStyleSheet("color: green")
        else:
            self.labelTasksForAnalysis.setText(STATUS_ENABLED)
            self.labelTasksForAnalysis.setStyleSheet("color: red")

    def tasksForAnalysisButtonClick(self):
        result1 = SearchAnalyzeSystem()
        result2 = SearchBackup()
        if result1 and result2 == STATUS_DISABLED:
            AnalyzeSystemOn()
            BackupOn()
        else:
            AnalyzeSystemOff()
            BackupOff()
        self.updateTasksForAnalysis()

    def updateDiagnosticTasks(self):
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
            self.labelDiagnosticTasks.setText(STATUS_DISABLED)
            self.labelDiagnosticTasks.setStyleSheet("color: green")
        else:
            self.labelDiagnosticTasks.setText(STATUS_ENABLED)
            self.labelDiagnosticTasks.setStyleSheet("color: red")

    def diagnosticTasksButtonClick(self):
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
        self.updateDiagnosticTasks()
    def updateNetPrecompilation(self):
        result1 = SearchNETFrameworkNGENv4030319()
        result2 = SearchNETFrameworkNGENv403031964()
        result3 = SearchNETFrameworkNGENv403031964Critical()
        result4 = SearchNETFrameworkNGENv4030319Critical()
        if result1 and result2 and result3 and result4 == STATUS_DISABLED:
            self.labelNetPrecompilation.setText(STATUS_DISABLED)
            self.labelNetPrecompilation.setStyleSheet("color: green")
        else:
            self.labelNetPrecompilation.setText(STATUS_ENABLED)
            self.labelNetPrecompilation.setStyleSheet("color: red")

    def NetPrecompilationButtonClick(self):
        result1 = SearchNETFrameworkNGENv4030319()
        result2 = SearchNETFrameworkNGENv403031964()
        result3 = SearchNETFrameworkNGENv403031964Critical()
        result4 = SearchNETFrameworkNGENv4030319Critical()
        if result1 and result2 and result3 and result4 == STATUS_DISABLED:
            NETFrameworkNGENv4030319On()
            NETFrameworkNGENv403031964On()
            NETFrameworkNGENv403031964CriticalOn()
            NETFrameworkNGENv4030319CriticalOn()
        else:
            NETFrameworkNGENv4030319Off()
            NETFrameworkNGENv403031964off()
            NETFrameworkNGENv403031964Criticaloff()
            NETFrameworkNGENv4030319Criticaloff()
        self.updateNetPrecompilation()

    def updateAutoProxyDetection(self):
        result = SearchProxy()
        if result == STATUS_DISABLED:
            self.labelAutoProxyDetection.setText(STATUS_DISABLED)
            self.labelAutoProxyDetection.setStyleSheet("color: green")
        else:
            self.labelAutoProxyDetection.setText(STATUS_ENABLED)
            self.labelAutoProxyDetection.setStyleSheet("color: red")

    def AutoProxyDetectionButtonClick(self):
        result = SearchProxy()
        if result == STATUS_DISABLED:
            ProxyOn()
        else:
            ProxyOff()
        self.updateAutoProxyDetection()

    def updateInstallingAndRemovingLanguages(self):
        result1 = SearchSynchronizLanguageSettings()
        result2 = SearchInstallation()
        result3 = SearchReconcileLanguageResources()
        result4 = SearchUninstallation()
        result5 = SearchLPRemove()
        if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
            self.labelInstallingAndRemovingLanguages.setText(STATUS_DISABLED)
            self.labelInstallingAndRemovingLanguages.setStyleSheet("color: green")
        else:
            self.labelInstallingAndRemovingLanguages.setText(STATUS_ENABLED)
            self.labelInstallingAndRemovingLanguages.setStyleSheet("color: red")

    def InstallingAndRemovingLanguagesButtonClick(self):
        result1 = SearchSynchronizLanguageSettings()
        result2 = SearchInstallation()
        result3 = SearchReconcileLanguageResources()
        result4 = SearchUninstallation()
        result5 = SearchLPRemove()
        if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
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
        self.updateInstallingAndRemovingLanguages()

    def updateAutoPerformanceCheck(self):
        result = SearchWinSAT()
        if result == STATUS_DISABLED:
            self.labelAutoPerformanceCheck.setText(STATUS_DISABLED)
            self.labelAutoPerformanceCheck.setStyleSheet("color: green")
        else:
            self.labelAutoPerformanceCheck.setText(STATUS_ENABLED)
            self.labelAutoPerformanceCheck.setStyleSheet("color: red")

    def AutoPerformanceCheckButtonClick(self):
        result = SearchWinSAT()
        if result == STATUS_DISABLED:
            WinSATOn()
        else:
            WinSATOff()
        self.updateAutoPerformanceCheck()

    def updateMapsLocation(self):
        result1 = SearchMapsToastTask()
        result2 = SearchMapsUpdateTask()
        result3 = SearchNotifications()
        result4 = SearchWindowsActionDialog()
        if result1 and result2 and result3 and result4 == STATUS_DISABLED:
            self.labelMapsLocation.setText(STATUS_DISABLED)
            self.labelMapsLocation.setStyleSheet("color: green")
        else:
            self.labelMapsLocation.setText(STATUS_ENABLED)
            self.labelMapsLocation.setStyleSheet("color: red")

    def MapsLocationButtonClick(self):
        result1 = SearchMapsToastTask()
        result2 = SearchMapsUpdateTask()
        result3 = SearchNotifications()
        result4 = SearchWindowsActionDialog()
        if result1 and result2 and result3 and result4 == STATUS_DISABLED:
            MapsToastTaskOn()
            MapsUpdateTaskOn()
            NotificationsOn()
            WindowsActionDialogOn()
        else:
            MapsToastTaskOff()
            MapsUpdateTaskOff()
            NotificationsOff()
            WindowsActionDialogOff()
        self.updateMapsLocation()

    def updateRemoteControl(self):
        result = SearchRemoteAssistanceTask()
        if result == STATUS_DISABLED:
            self.labelRemoteControl.setText(STATUS_DISABLED)
            self.labelRemoteControl.setStyleSheet("color: green")
        else:
            self.labelRemoteControl.setText(STATUS_ENABLED)
            self.labelRemoteControl.setStyleSheet("color: red")

    def RemoteControlButtonClick(self):
        result = SearchRemoteAssistanceTask()
        if result == STATUS_DISABLED:
            RemoteAssistanceTaskOn()
        else:
            RemoteAssistanceTaskOff()
        self.updateRemoteControl()

    def updateCleaningTasks(self):
        result1 = SearchCleanupTemporaryState()
        result2 = SearchDsSvcCleanup()
        result3 = SearchSilentCleanup()
        result4 = SearchCleanupOfflineContent()
        result5 = SearchCacheTask()
        if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
            self.labelCleaningTasks.setText(STATUS_DISABLED)
            self.labelCleaningTasks.setStyleSheet("color: green")
        else:
            self.labelCleaningTasks.setText(STATUS_ENABLED)
            self.labelCleaningTasks.setStyleSheet("color: red")

    def CleaningTasksButtonClick(self):
        result1 = SearchCleanupTemporaryState()
        result2 = SearchDsSvcCleanup()
        result3 = SearchSilentCleanup()
        result4 = SearchCleanupOfflineContent()
        result5 = SearchCacheTask()
        if result1 and result2 and result3 and result4 and result5 == STATUS_DISABLED:
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
        self.updateCleaningTasks()

    def updateMicrosoftStore(self):
        result = check_microsoft_store_status()
        result2 = check_microsoft_store_status2()
        if result and result2 == STATUS_DISABLED:
            self.labelMicrosoftStore.setText(STATUS_DISABLED)
            self.labelMicrosoftStore.setStyleSheet("color: green")
        else:
            self.labelMicrosoftStore.setText(STATUS_ENABLED)
            self.labelMicrosoftStore.setStyleSheet("color: red")

    def MicrosoftStoreButtonClick(self):
        result = check_microsoft_store_status()
        result2 = check_microsoft_store_status2()
        if result and result2 == STATUS_DISABLED:
            enable_microsoft_store()
            enable_microsoft_store2()
        else:
            disable_microsoft_store()
            disable_microsoft_store2()
        self.updateMicrosoftStore()

    def updateWindowsXBOX(self):
        result = check_xbox_status()
        if result == STATUS_DISABLED:
            self.labelWindowsXBOX.setText(STATUS_DISABLED)
            self.labelWindowsXBOX.setStyleSheet("color: green")
        else:
            self.labelWindowsXBOX.setText(STATUS_ENABLED)
            self.labelWindowsXBOX.setStyleSheet("color: red")

    def WindowsXBOXButtonClick(self):
        result = check_xbox_status()
        if result == STATUS_DISABLED:
            enable_xbox()
        else:
            disable_xbox()
        self.updateWindowsXBOX()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = Task()
    energy_window.show()
    sys.exit(app.exec())

