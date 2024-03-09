import shutil
import time

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QFrame, QPushButton

import SettingsWidjets.Class.BaseSettings
import SettingsWidjets.Class.WindowsCleaning
import SettingsWidjets.Class.Energy
import main
from main import *
# from main import MainWindows
import Class.MainWindows

import subprocess
import glob as gb
from selenium import webdriver
from selenium.webdriver.common.by import By
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
import Class.AboutTheProgram


class Setings(QDialog, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.aa = None
        self.settings = Ui_Settings
        self.setupUi(self)

        RemoveWindowsMenu(self)
        self.current_menu = None  # Keep track of the currently open menu
        self.frame = QFrame(self)
        self.layout = QVBoxLayout(self.MainBody)
        self.importmainclass = main.MainWindows
        self.connect_signals_text()
        # закрытие программы

        self.pushButtonDefoltSettings.clicked.connect(self.DefoltSettings)
        self.pushButtonClear.clicked.connect(self.Clear)
        self.pushButtonClose.clicked.connect(self.CloseWindow)
        self.pushButtonPowerSupply.clicked.connect(self.PowerEnergy)

    def DefoltSettings(self):
        self.update_menu(SettingsWidjets.Class.BaseSettings.BaseSet())

    def Clear(self):
        self.update_menu(SettingsWidjets.Class.WindowsCleaning.WindowsCleaning())

    def PowerEnergy(self):
        self.update_menu(SettingsWidjets.Class.Energy.EnergyWindows())


    def update_menu(self, new_menu):
        if self.current_menu is not None:
            self.current_menu.close()
            self.layout.removeWidget(self.current_menu)
            self.current_menu.deleteLater()

        self.current_menu = new_menu
        self.layout.addWidget(self.current_menu)
        self.current_menu.show()

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

    def connect_signals_text(self):
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButtonAutoLoad.setFont(font)
        self.pushButtonAutoLoad.setText("Автозагрузки")
        self.pushButtonDefoltSettings.setFont(font)
        self.pushButtonDefoltSettings.setText("Базовые настройки")
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setText("Очистка")
        self.pushButtonServise.setFont(font)
        self.pushButtonServise.setText("Службы")
        self.pushButtonPowerSupply.setFont(font)
        self.pushButtonPowerSupply.setText("Электропитание")
        self.pushButtonPowerSupply.setFont(font)
        self.pushButtonPowerSupply.setText("Электропитание")

    @staticmethod
    def CloseWindow():
        sys.exit()
