import shutil
import time

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent

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
        self.settings = Ui_Settings
        self.setupUi(self)
        RemoveWindowsMenu(self)
        self.header_frame.setStyleSheet('background-color:white')
