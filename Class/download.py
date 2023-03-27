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
import winreg

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

        subprocess.call([r'C:\Users\rrarr\OneDrive\Рабочий стол\ZoomDesctop\Class\SoftPC\SearchSoft.bat'])

    def TransitionAboutTheProgram(self):
        self.hide()
        self.abouttheprogram = AboutTheProgram()
        self.abouttheprogram.show()


    def SearchSoftWindows(self):
        #Определение имени windows
        self.nameUsers = os.getlogin()
        softs = [
            {"name": "GoogleChrome", "path": f"C:/Program Files/Google/Chrome/Application/*exe",
             "button": self.pushDownloadGoogle},
            {"name": "YandexBrowser",
             "path": f"C:/Users/{self.nameUsers}/AppData/Local/Yandex/YandexBrowser/Application/*exe",
             "button": self.pushDownloadYandex},
            {"name": "Opera GX", "path": f"C:/Users/{self.nameUsers}/AppData/Local/Programs/Opera GX/launcher.exe",
             "button": self.pushDownloadOpera},
            {"name": "Whats App", "path": f"C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop*",
             "button": self.pushDownloadWatsApp},
            {"name": "Telegram", "path": f"C:/Users/{self.nameUsers}/AppData/Roaming/Telegram Desktop/*.exe",
             "button": self.pushDownloadTG},
            {"name": "Discord", "path": f"C:/Users/{self.nameUsers}/AppData/Local/Discord/*.exe",
             "button": self.pushDownloadDS},
            {"name": "Viber", "path": f"C:/Users/{self.nameUsers}/AppData/Roaming/ViberPC",
             "button": self.pushDownloadViber},
            {"name": "TeamSpeak3", "path": "C:\Program Files\TeamSpeak 3 Client\*exe", "button": self.pushDownloadTS},
            {"name": "Steam", "path": "C:\Program Files (x86)\Steam\*exe", "button": self.pushDownloadSteam},
            {"name": "EpicGames", "path": "C:\Program Files (x86)\Epic Games", "button": self.pushDownloadEpicGames},
            {"name": "Origin", "path": "C:/Program Files/Electronic Arts/EA Desktop/EA Desktop/*exe",
             "button": self.pushDownloadOrigin},
            {"name": "Battle.net", "path": "C:/Program Files (x86)/Battle.net/*exe",
             "button": self.pushDownloadBattleNet},
            {"name": "NVIDIA", "path": "C:/Program Files/NVIDIA Corporation", "button": self.pushDownloadNvidea},
            {"name": "Ryzen", "path": "C:/AMD/RyzenMasterExtract/MSIFiles/Packages/*exe",
             "button": self.pushDownloadRyzen},
            {"name": "Malwarebytes", "path": "C:/Program Files/Malwarebytes/Anti-Malware/*exe", "button": self.pushDownloadMalwarebytes},
            {"name": "NORD32", "path": "C:/Program Files/ESET/ESET Security/*exe", "button": self.pushDownloadEset}
        ]

        for soft in softs:
            if gb.glob(soft["path"]):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
                soft["button"].setIcon(icon1)















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




