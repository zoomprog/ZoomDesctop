import ctypes,sys
import os
import time
import pathlib
import shutil


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
import win32com.client

class Download(QDialog, Ui_Download):
    def __init__(self):
        super().__init__()
        self.soft_main_windows = None
        self.softs = None
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
        self.pushDelYandex.clicked.connect(self.buttonYandexDel)
        self.pushDelOpera.clicked.connect(self.buttonOperaDel)
        self.pushDelViber.clicked.connect(self.buttonViberDel)
        self.pushDelDS.clicked.connect(self.buttonDSDel)
        self.pushDelTS.clicked.connect(self.buttonTSDEL)
        self.pushDelEpicGames.clicked.connect(self.buttonEpicGamesDel)
        self.pushDelOrigin.clicked.connect(self.buttonOriginDel)
        self.pushDelUplay.clicked.connect(self.buttonUplayDel)
        self.pushDelBattleNet.clicked.connect(self.buttonBattleNetDel)
        self.pushDelXbox.clicked.connect(self.buttonXboxDel)
        self.pushDelWeather.clicked.connect(self.buttonWeatherDel)
        self.pushDelVoiceRec.clicked.connect(self.buttonVoiceRecDel)
        self.pushDelStore.clicked.connect(self.buttonStoreDel)
        self.pushDelPhoto.clicked.connect(self.buttonPhotoDel)
        self.pushDelPeople.clicked.connect(self.buttonPeopleDel)
        self.pushDelOneNote.clicked.connect(self.buttonOneNote)
        self.pushDelNews.clicked.connect(self.buttonNewsDel)
        self.pushDelFilm.clicked.connect(self.buttonFilmDel)
        self.pushDelMSC.clicked.connect(self.buttonMSCDel)
        self.pushDelMap.clicked.connect(self.buttonMapDel)
        self.pushDelGMusic.clicked.connect(self.buttonGMusicDel)
        self.pushDelSkype.clicked.connect(self.buttonSkypeDel)
        self.pushDelOffice.clicked.connect(self.buttonOfficeDel)
        self.pushDelCamera.clicked.connect(self.buttonCameraDel)
        self.pushDelAlarmClock.clicked.connect(self.buttonAlarmClockDel)
        self.pushDelCalendarAndMail.clicked.connect(self.buttonCalendarAndMailDel)
        self.pushDelCalc.clicked.connect(self.buttonCalcDel)
        self.pushDel3dBuilder.clicked.connect(self.button3dBuilder)

        #Кнопки menu
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)
        self.pushBackMenu.clicked.connect(self.TransitionAboutTheProgram)







    def TransitionAboutTheProgram(self):
        self.hide()
        self.abouttheprogram = AboutTheProgram()
        self.abouttheprogram.show()


    def SearchSoftWindows(self):
        #Определение имени windows
        self.nameUsers = os.getlogin()
        self.softs = [
            {"name": "GoogleChrome",
             "path": f"C:/Program Files/Google/Chrome/Application/*exe",
             "button": self.pushDownloadGoogle},
            {"name": "YandexBrowser",
             "path": f"C:/Users/{self.nameUsers}/AppData/Local/Yandex/YandexBrowser/Application/*exe",
             "button": self.pushDownloadYandex},
            {"name": "Opera GX",
             "path": f"C:/Users/{self.nameUsers}/AppData/Local/Programs/Opera GX/launcher.exe",
             "button": self.pushDownloadOpera},
            {"name": "Whats App",
             "path": f"C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop*",
             "button": self.pushDownloadWatsApp},
            {"name": "Telegram",
             "path": f"C:/Users/{self.nameUsers}/AppData/Roaming/Telegram Desktop/*.exe",
             "button": self.pushDownloadTG},
            {"name": "Discord",
             "path": f"C:/Users/{self.nameUsers}/AppData/Local/Discord/*.exe",
             "button": self.pushDownloadDS},
            {"name": "Viber",
             "path": f"C:/Users/{self.nameUsers}/AppData/Roaming/ViberPC",
             "button": self.pushDownloadViber},
            {"name": "TeamSpeak3",
             "path": "C:\Program Files\TeamSpeak 3 Client\*exe",
             "button": self.pushDownloadTS},
            {"name": "Steam",
             "path": "C:\Program Files (x86)\Steam\*exe",
             "button": self.pushDownloadSteam},
            {"name": "EpicGames",
             "path": "C:\Program Files (x86)\Epic Games",
             "button": self.pushDownloadEpicGames},
            {"name": "Origin",
             "path": "C:/Program Files/Electronic Arts/EA Desktop/EA Desktop/*exe",
             "button": self.pushDownloadOrigin},
            {"name": "Battle.net",
             "path": "C:/Program Files (x86)/Battle.net/*exe",
             "button": self.pushDownloadBattleNet},
            {"name": "NVIDIA",
             "path": "C:/Program Files/NVIDIA Corporation",
             "button": self.pushDownloadNvidea},
            {"name": "Ryzen",
             "path": "C:/AMD/RyzenMasterExtract/MSIFiles/Packages/*exe",
             "button": self.pushDownloadRyzen},
            {"name": "Malwarebytes",
             "path": "C:/Program Files/Malwarebytes/Anti-Malware/*exe",
             "button": self.pushDownloadMalwarebytes},
            {"name": "NORD32",
             "path": "C:/Program Files/ESET/ESET Security/*exe",
             "button": self.pushDownloadEset},
        ]
        self.soft_main_windows = [
            {
                "name": 'Name              : Microsoft.BingWeather',
                "command": "Get-AppxPackage Microsoft.BingWeather",
                "button": self.pushDownloadWeather
            },
            {
                "name": "Name              : Microsoft.XboxGamingOverlay",
                "command": "Get-AppxPackage Microsoft.XboxGamingOverlay",
                "button": self.pushDownloadXbox
            },
            {
                "name": "Name              : Microsoft.WindowsSoundRecorder",
                "command": "Get-AppxPackage Microsoft.WindowsSoundRecorder",
                "button": self.pushDownloadVoiceRec
            },
            {
                "name": "Name              : Microsoft.WindowsStore",
                "command": "Get-AppxPackage Microsoft.WindowsStore",
                "button": self.pushDownloadStore
            },
            {
                "name": "Name              : Microsoft.Windows.Photos",
                "command": "Get-AppxPackage Microsoft.Windows.Photos",
                "button": self.pushDownloadPhoto
            },
            {
                "name": "Name              : Microsoft.People",
                "command": "Get-AppxPackage Microsoft.People",
                "button": self.pushDownloadPeople
            },
            {
                "name": "Name              : Microsoft.Office.OneNote",
                "command": "Get-AppxPackage Microsoft.Office.OneNote",
                "button": self.pushDownloadOneNote
            },
            {
                "name": "Name              : Microsoft.BingNews",
                "command": "Get-AppxPackage Microsoft.BingNews",
                "button": self.pushDownloadNews
            },
            {
                "name": "Name              : Microsoft.ZuneVideo",
                "command": "Get-AppxPackage Microsoft.ZuneVideo",
                "button": self.pushDownloadFilm
            },
            {
                "name": "Name              : Microsoft.MicrosoftSolitaireCollection",
                "command": "Get-AppxPackage Microsoft.MicrosoftSolitaireCollection",
                "button": self.pushDownloadMSC
            },
            {
                "name": "Name              : Microsoft.WindowsMaps",
                "command": "Get-AppxPackage Microsoft.WindowsMaps",
                "button": self.pushDownloadMap
            },
            {
                "name": "Name              : Microsoft.ZuneMusic",
                "command": "Get-AppxPackage Microsoft.ZuneMusic",
                "button": self.pushDownloadGMusic
            },
            {
                "name": "Name              : Microsoft.SkypeApp",
                "command": "Get-AppxPackage Microsoft.SkypeApp",
                "button": self.pushDownloadSkype
            },
            {
                "name": "Name              : Microsoft.MicrosoftOfficeHub",
                "command": "Get-AppxPackage Microsoft.MicrosoftOfficeHub",
                "button": self.pushDownloadOffice
            },
            {
                "name": "Name              : Microsoft.WindowsAlarms",
                "command": "Get-AppxPackage Microsoft.WindowsAlarms",
                "button": self.pushDownloadAlarmClock
            },
            {
                "name": "Name              : Microsoft.WindowsAlarms",
                "command": "Get-AppxPackage Microsoft.WindowsAlarms",
                "button": self.pushDownloadAlarmClock
            },
            {
                "name": "Name              : Microsoft.windowscommunicationsapps",
                "command": "Get-AppxPackage Microsoft.windowscommunicationsapps",
                "button": self.pushDownloadCalendarAndMail
            },
            {
                "name": "Name              : Microsoft.WindowsCalculator",
                "command": "Get-AppxPackage Microsoft.WindowsCalculator",
                "button": self.pushDownloadCalc
            },
            {
                "name": "Name              : Microsoft.3DBuilder",
                "command": "Get-AppxPackage Microsoft.3DBuilder",
                "button": self.pushDownload3dBuilder
            }
        ]

        for soft in self.soft_main_windows:
            output = subprocess.run(["powershell", soft["command"]], capture_output=True, text=True)
            if soft["name"] in output.stdout:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                               QtGui.QIcon.State.Off)
                soft["button"].setIcon(icon)


        for soft in self.softs:
            if gb.glob(soft["path"]):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
                soft["button"].setIcon(icon1)


#Установка приложений
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
#Удаление приложений
    def delete_file(self, folder, file_name ):
        file_path = os.path.join(self, file_name)
        try:
            os.remove(file_path)
            print(f"{file_name} has been deleted from {folder}")
        except OSError as e:
            print(f"Error deleting {file_name} from {folder}: {e}")

    def buttonWhatsAppDel(self):
        os.system("Class\DelSoft\WhatsAppDel.bat")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                     QtGui.QIcon.State.Off)
        self.pushDownloadWatsApp.setIcon(icon1)

    def buttonGoogleDel(self):
        os.system("Class\DelSoft\GoogleDel.bat")
        self.delete_file("C:\ProgramData\Microsoft\Windows\Start Menu\Programs", "Google")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadGoogle.setIcon(icon1)


    def buttonSteamDel(self):
        steam_folder = r'C:\Program Files (x86)\Steam'
        common_folder = r'C:\Program Files (x86)\Common Files\Steam'
        try:
            shutil.rmtree(steam_folder)
            shutil.rmtree(common_folder)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadSteam.setIcon(icon1)
        except FileNotFoundError:
            print("Steam was not found.")
        except Exception as e:
            print(f"Error uninstalling Steam: {e}")

    def buttonNVIDIADel(self):
        os.system("Class\DelSoft\VideoCard1De.bat")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadGoogle.setIcon(icon1)
    def buttonTGDel(self):
        os.system("Class\DelSoft\TelegramDel.bat")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadTG.setIcon(icon1)
    def buttonYandexDel(self):
        path_to_yandex_browser = f"C:/Users/{self.nameUsers}/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"
        try:
            shutil.rmtree(os.path.dirname(path_to_yandex_browser), ignore_errors=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadYandex.setIcon(icon1)
        except FileNotFoundError:
            print("YandexBrowser was not found.")
    def buttonOperaDel(self):
        path_to_operagx_browser=f"C:/Users/{self.nameUsers}/AppData/Local/Programs/Opera GX/opera.exe"
        try:
            shutil.rmtree(os.path.dirname(path_to_operagx_browser), ignore_errors=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadOpera.setIcon(icon1)
        except FileNotFoundError:
            print("OperaGX was not found.")
    def buttonViberDel(self):
        os.system('wmic product where "name like \'%Viber%\'" call uninstall /nointeractive')
        time.sleep(5)  # нужно подождать чтоб удалилась нужно добавить экран ожидания выполнения
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadViber.setIcon(icon1)

    def get_appdata_path(self):#находим дискорд в папке roaming
        command = '$env:APPDATA'
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        path = result.stdout.strip() + "\discord"
        return path

    def get_localappdata_path(self):#находим дискорд в папке local
        command = '$env:LOCALAPPDATA'
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        path = result.stdout.strip() + "\Discord"
        return path

    def delete_folder(self,path):#удаляем папки
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Папка {path} удалена")
            return True
        else:
            print(f"Папка {path} не найдена")
            return False

    def buttonDSDel(self):#Удаление дискорд
        path1 = self.get_localappdata_path()
        path2 = self.get_appdata_path()
        print(f"Path to LocalAppData: {path1}")
        print(f"Path to AppData: {path2}")

        if self.delete_folder(path1) and self.delete_folder(path2):
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadDS.setIcon(icon1)

    def buttonTSDEL(self):
        try:
            shutil.rmtree('C:/Program Files/TeamSpeak 3 Client')
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.pushDownloadTS.setIcon(icon1)
        except FileNotFoundError:
            print("TeamSpeak was not found.")
    def buttonEpicGamesDel(self):
        try:
            os.system('wmic product where "name like \'%Epic Games%\'" call uninstall /nointeractive')
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
            self.pushDownloadEpicGames.setIcon(icon1)
        except FileNotFoundError:
            print("EpicGames was not found")

    def buttonOriginDel(self):
        try:
            os.system('wmic product where "name like \'%EA%\'" call uninstall /nointeractive')
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
            self.pushDownloadOrigin.setIcon(icon1)
        except FileNotFoundError:
            print("Origin in nor found")
    def buttonUplayDel(self):
        try:
            os.system('wmic product where "name like \'%Uplay%\'" call uninstall /nointeractive')
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadUplay.setIcon(icon1)
        except FileNotFoundError:
            print("Uplay is not found")
    def buttonBattleNetDel(self):
        try:
            shutil.rmtree('C:/Program Files (x86)/Battle.net')
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadBattleNet.setIcon(icon1)
        except FileNotFoundError:
            print("Battle net is not found")

    def buttonXboxDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *xboxapp* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadXbox.setIcon(icon1)
        except FileNotFoundError:
            pass


    def buttonWeatherDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *bingweather* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadWeather.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonVoiceRecDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *soundrecorder* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadVoiceRec.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonStoreDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *windowsstore* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadStore.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonPhotoDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage Microsoft.Windows.Photos | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadPhoto.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonPeopleDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *люди* | Remove-AppxPackage | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadPeople.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonOneNote(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *onenote* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadOneNote.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonNewsDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *bingnews* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadNews.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonFilmDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *zunevideo* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadFilm.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonMSCDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *solitairecollection* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadMSC.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonMapDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *windowsmaps* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadMap.setIcon(icon1)
        except FileNotFoundError:
            pass
    def buttonGMusicDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *zunemusic* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadGMusic.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonSkypeDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *skypeapp* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadSkype.setIcon(icon1)
        except FileNotFoundError:
            pass
    def buttonOfficeDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *officehub* | Remove-AppxPackage"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadOffice.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonCameraDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *windowscamera* | Remove-AppxPackage"], capture_output=True,
                           text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadCamera.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonAlarmClockDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *windowsalarms* | Remove-AppxPackage"], capture_output=True,
                           text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadAlarmClock.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonCalendarAndMailDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage"], capture_output=True,
                           text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadCalendarAndMail.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonCalcDel(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage *windowscalculator* | Remove-AppxPackage"], capture_output=True,
                           text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadCalc.setIcon(icon1)
        except FileNotFoundError:
            pass

    def button3dBuilder(self):
        try:
            subprocess.run(["powershell", "Get-AppxPackage * 3dbuilder * | Remove-AppxPackage"], capture_output=True,
                           text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownload3dBuilder.setIcon(icon1)
        except FileNotFoundError:
            pass

