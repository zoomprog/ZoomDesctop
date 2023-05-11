import shutil
import time

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QFrame, QPushButton

import SettingsWidjets.Class.BaseSettings
import main
from main import *
#from main import MainWindows
import Class.MainWindows

import subprocess
import glob as gb
import win32gui
from selenium import webdriver
from selenium.webdriver.common.by import By
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
import Class.AboutTheProgram


class Setings(QDialog,Ui_Settings):
    def __init__(self):
        super().__init__()
        self.aa = None
        self.settings = Ui_Settings
        self.setupUi(self)
        RemoveWindowsMenu(self)
        self.importmainclass = main.MainWindows
        #закрытие программы


        self.pushButtonDefoltSettings.clicked.connect(self.DefoltSettings)






    def DefoltSettings(self):
        self.frame = QFrame(self)
        self.layout = QVBoxLayout(self.MainBody)
        self.aa = SettingsWidjets.Class.BaseSettings.BaseSet()
        self.layout.addWidget(self.aa)


        # self.aa = SettingsWidjets.Class.BaseSettings.BaseSet()
        # self.layout.addWidget(self.aa)
        # self.main_window.setCentralWidget(self.frame)
        # self.main_window.show()




    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self.UpBar.underMouse():
            self.offset = event.pos()
        else:
            self.offset = None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton and self.UpBar.underMouse():
            self.move(self.mapToGlobal(event.pos() - self.offset))
        else:
            self.offset = None
