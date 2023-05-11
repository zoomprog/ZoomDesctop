from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog
import main
from main import *

from SettingsWidjets.BaseSettings import Ui_BaseSettings

class BaseSet(QDialog,Ui_BaseSettings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget_BraundMaurWindows.setWordWrap(True)
        self.listWidget_BraundMaurWindows.setWordWrap(True)
        self.listWidget_DefNotifications.setWordWrap(True)
        self.IncreaseFrame = 275
        self.DefolfSizeFrame = 224
        self.pushButtonAntivitusWindowsInfo.enterEvent = self.AntivitusWindowsInfo
        self.pushButtonAntivitusWindowsInfo.leaveEvent = self.ResetAntivitusWindowsInfo
        self.pushButtonBraundMaurWindows.enterEvent = self.BraundMaurWindowsInfo
        self.pushButtonBraundMaurWindows.leaveEvent = self.ResetBraundMaurWindowsInfo
        self.pushButtonWindowsUpdate.enterEvent = self.WindowsUpdateInfo
        self.pushButtonWindowsUpdate.leaveEvent = self.ResetWindowsUpdateInfo
        self.pushButtonAcsMouse.enterEvent = self.AcsMouseInfo
        self.pushButtonAcsMouse.leaveEvent = self.ResetAcsMouseInfo
        self.pushButtonUAC.enterEvent = self.UACInfo
        self.pushButtonUAC.leaveEvent = self.ResetUACInfo
        self.pushButtonDefNotifications.enterEvent = self.DefNotificationsInf
        self.pushButtonDefNotifications.leaveEvent = self.ResetDefNotificationsInf
        self.pushButtonAutoUpdateDriversStartWindows.enterEvent = self.AutoUpdateDriversStartWindowsInfo
        self.pushButtonAutoUpdateDriversStartWindows.leaveEvent = self.ResetAutoUpdateDriversStartWindowsInfo


    def set_widget_height(self, frame, list_widget, frame_height, list_widget_height, main_frame_height):
        frame.setFixedHeight(frame_height)
        list_widget.setFixedHeight(list_widget_height)
        self.frame.setFixedHeight(main_frame_height)
    def AntivitusWindowsInfo(self, event):
        self.set_widget_height(self.frame_AntivirusWindows, self.listWidget_AntivirusWindows, 49, 49, self.IncreaseFrame)
    def ResetAntivitusWindowsInfo(self, event):
        self.set_widget_height(self.frame_AntivirusWindows, self.listWidget_AntivirusWindows, 32, 25, self.DefolfSizeFrame)
    def BraundMaurWindowsInfo(self, event):
        self.set_widget_height(self.frame_BraundMaurWindows, self.listWidget_BraundMaurWindows, 55, 55, self.IncreaseFrame)
    def ResetBraundMaurWindowsInfo(self, event):
        self.set_widget_height(self.frame_BraundMaurWindows, self.listWidget_BraundMaurWindows, 32, 25, self.DefolfSizeFrame)
    def WindowsUpdateInfo(self, event):
        self.set_widget_height(self.frame_WindowsUpdate, self.listWidget_WindowsUpdate, 49, 49, self.IncreaseFrame)
    def ResetWindowsUpdateInfo(self, event):
        self.set_widget_height(self.frame_WindowsUpdate, self.listWidget_WindowsUpdate, 32, 25, self.DefolfSizeFrame)
    def AcsMouseInfo(self, event):
        self.set_widget_height(self.frame_AcsMouse, self.listWidget_AcsMouse, 60, 60, self.IncreaseFrame)
    def ResetAcsMouseInfo(self, event):
        self.set_widget_height(self.frame_AcsMouse, self.listWidget_AcsMouse, 32, 25, self.DefolfSizeFrame)
    def UACInfo(self, event):
        self.set_widget_height(self.frame_UAC, self.listWidget_UAC, 60, 60, self.IncreaseFrame)
    def ResetUACInfo(self, event):
        self.set_widget_height(self.frame_UAC, self.listWidget_UAC, 32, 25, self.DefolfSizeFrame)
    def DefNotificationsInf(self, event):
        self.set_widget_height(self.frame_DefNotifications,self.listWidget_DefNotifications, 60, 60, self.IncreaseFrame)
    def ResetDefNotificationsInf(self, event):
        self.set_widget_height(self.frame_DefNotifications,self.listWidget_DefNotifications, 32, 25, self.DefolfSizeFrame)
    def AutoUpdateDriversStartWindowsInfo(self, event):
        self.set_widget_height(self.frame_AutoUpdateDriversStartWindows, self.listWidget_AutoUpdateDriversStartWindows, 100, 100, self.IncreaseFrame)
    def ResetAutoUpdateDriversStartWindowsInfo(self, event):
        self.set_widget_height(self.frame_AutoUpdateDriversStartWindows, self.listWidget_AutoUpdateDriversStartWindows, 32, 25, self.DefolfSizeFrame)





           


if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_set = BaseSet()
    base_set.show()
    sys.exit(app.exec())