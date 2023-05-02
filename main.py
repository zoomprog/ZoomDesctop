import sqlite3
import sys
import webbrowser
import re
import os
import menu, login, DownloadSoft
from PyQt6.QtWidgets import QDialog, QVBoxLayout
from PyQt6 import QtWidgets, QtCore, QtGui
from ui_login import Ui_ImageDialog
from ui_AboutTheProgram import Ui_AboutTheProgram
from ui_reg import Ui_Ui_Reg
from Settings import Ui_Settings

from PyQt6.QtCore import QPropertyAnimation, QSize, QAbstractAnimation, QTimer
from PyQt6.QtCore import Qt, QPoint

from Class.download import *
from Class.Registration import *
from Class.AboutTheProgram import *
from Class.MainWindows import *




from Functions.RemoveWindowsMenu import RemoveWindowsMenu






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    maindow = MainWindows()
    maindow.show()
    sys.exit(app.exec())
