import sys

from Functions.Task.TasksForAnalysis.TasksForAnalysis import SearchAnalyzeSystem, AnalyzeSystemOn, AnalyzeSystemOff, SearchBackup, BackupOn, BackupOff
from Functions.Task.DiagnosticTasks.DiagnosticTasks import SearchProactiveScan, ProactiveScanOn, ProactiveScanOff

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

        self.pushTasksForAnalysis.clicked.connect(self.tasksForAnalysisButtonClick)
        self.pushDiagnosticTasks.clicked.connect(self.diagnosticTasksButtonClick)

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
        if result1 == STATUS_DISABLED:
            self.labelDiagnosticTasks.setText(STATUS_DISABLED)
            self.labelDiagnosticTasks.setStyleSheet("color: green")
        else:
            self.labelDiagnosticTasks.setText(STATUS_ENABLED)
            self.labelDiagnosticTasks.setStyleSheet("color: red")

    def diagnosticTasksButtonClick(self):
        result1 = SearchProactiveScan()
        if result1 == STATUS_DISABLED:
            ProactiveScanOn()
        else:
            ProactiveScanOff()
        self.updateDiagnosticTasks()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = Task()
    energy_window.show()
    sys.exit(app.exec())

