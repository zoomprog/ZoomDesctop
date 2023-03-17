import ctypes,sys
import os
import pathlib

import winapps
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QWidget
from guidata.utils import is_program_installed
from main import *
from main import MainWindows
from ui_Download import Ui_Download
from main import *
import win32api as w
from pathlib import Path
from subprocess import Popen
import subprocess
from elevate import elevate
from pyuac import main_requires_admin
import glob as gb


class Download(QDialog, Ui_Download):
    def __init__(self):
        super().__init__()
        self.abouttheprogram = None
        self.nameUsers = None
        self.oldPos = None
        self.ui = Ui_Download
        self.setupUi(self)
        self.importmainclass = MainWindows


        # админка


        self.importmainclass.RemoveWindowsMenu(self)
        self.SearchSoftWindows()#поиск софта
        #кнопка установить софт
        self.pushDownloadSteam.clicked.connect(self.buttonSteamDownload)
        self.pushDownloadGoogle.clicked.connect(self.buttonGoogleDownload)
        self.pushDownloadWatsApp.clicked.connect(self.buttonWhatsAppDownload)
        self.pushDownloadNvidea.clicked.connect(self.buttonNVIDIADownload)
        self.pushDownloadTG.clicked.connect(self.buttonTGDownload)
        #кнопки удалить софт
        self.pushDelSteam.clicked.connect(self.buttonSteamDel)
        self.pushDelGoogle.clicked.connect(self.buttonGoogleDel)
        self.pushDelNvidea.clicked.connect(self.buttonNVIDIADel)
        self.pushDelWatsApp.clicked.connect(self.buttonWhatsAppDel)

        #Кнопки menu
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)
        self.pushBackMenu.clicked.connect(self.TransitionAboutTheProgram)





    def TransitionAboutTheProgram(self):
        self.hide()
        self.abouttheprogram = AboutTheProgram()
        self.abouttheprogram.show()


    def SearchSoftWindows(self):

        for _ in winapps.search_installed('Steam'):
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadSteam.setIcon(icon1)

        for _ in winapps.search_installed('NVIDIA'):
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadNvidea.setIcon(icon1)
        for _ in winapps.search_installed('Калькулятор'):
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadCalc.setIcon(icon1)

        self.nameUsers = os.getlogin()
        genVar = gb.glob(f"C:/Users/{self.nameUsers}/AppData/Roaming/Telegram Desktop/*.exe")
        for py in genVar:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadTG.setIcon(icon1)
        genVar = gb.glob(f"C:/Users/{self.nameUsers}/AppData/Local/Discord/*.exe")
        for py in genVar:#Discord проверка установки файла
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadDS.setIcon(icon1)
        genVar = gb.glob(f"C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop_2.2308.6.0_x64__cv1g1gvanyjgm/*exe")
        for py in genVar:#WhatsApp проверка установки файла
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadWatsApp.setIcon(icon1)
        genVar = gb.glob(f"C:/Program Files/Google/Chrome/Application/*exe")
        for py in genVar:#Google проверка установки файла
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadGoogle.setIcon(icon1)








#функции установки
    def buttonSteamDownload(self):
        url = 'https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe'
        path = f'/Users/{self.nameUsers}/Downloads/SteamSetup.exe'
        wget.download(url, path)
        for _ in winapps.search_installed('Steam'):
            os.system(path)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadSteam.setIcon(icon1)
        w.DeleteFile(path)


    def buttonGoogleDownload(self):
        os.system('soft\ChromeSetup.exe')
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadGoogle.setIcon(icon1)
    def buttonNVIDIADownload(self):
        url = "https://ru.download.nvidia.com/GFE/GFEClient/3.27.0.112/GeForce_Experience_v3.27.0.112.exe"
        path = f'/Users/{self.nameUsers}/Downloads/GeForce_Experience_v3.27.0.112.exe'
        wget.download(url, path)
        for _ in winapps.search_installed('NVIDIA'):
            os.system(path)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadNvidea.setIcon(icon1)
    def buttonTGDownload(self):
        url = "https://telegram.org/dl/desktop/win64"
        path = f'/Users/{self.nameUsers}/Downloads/tsetup-x64.4.6.5.exe'
        wget.download(url, path)
        for _ in winapps.search_installed('NVIDIA'):
            genVar = gb.glob(f"C:/Users/{self.nameUsers}/AppData/Roaming/Telegram Desktop/*.exe")
            for py in genVar:
                os.system(path)
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
                self.pushDownloadTG.setIcon(icon1)
    def buttonWhatsAppDownload(self):
        webbrowser.open_new(r"ms-windows-store://pdp/?productid=9NKSQGP7F2NH&mode=mini")
        genVar = gb.glob(f"C:/Program Files/Google/Chrome/Application/*exe")
        for py in genVar:  # Google проверка установки файла
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadWatsApp.setIcon(icon1)

















#функции удаления
    def buttonSteamDel(self):

        for _ in winapps.search_installed('Steam'):
            if ctypes.windll.shell32.IsUserAnAdmin():
                os.system(f"Class/DelSoft/GoogleDel.bat")
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadSteam.setIcon(icon1)

    def buttonGoogleDel(self):
        if ctypes.windll.shell32.IsUserAnAdmin():
            os.system("Class\DelSoft\GoogleDel.bat")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadGoogle.setIcon(icon1)
    def buttonNVIDIADel(self):
        if ctypes.windll.shell32.IsUserAnAdmin():
            os.system("Class\DelSoft\VideoCard1De.bat")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadGoogle.setIcon(icon1)
    def buttonTGDel(self):
        if ctypes.windll.shell32.IsUserAnAdmin():
            os.system("Class\DelSoft\TelegramDel.bat")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadTG.setIcon(icon1)
    def buttonWhatsAppDel(self):
        os.system("Class\DelSoft\WhatsAppDel.bat")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadWatsApp.setIcon(icon1)




