import shutil
import time

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent

from main import *
#from main import MainWindows
import Class.MainWindows
from ui_Download import Ui_Download
import subprocess
import glob as gb
from selenium import webdriver
from selenium.webdriver.common.by import By
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
import Class.AboutTheProgram

class Download(QDialog, Ui_Download):
    def __init__(self,id_Profile, settings):
        super().__init__()
        self.offset = None
        self.soft_main_windows = None
        self.softs = None
        self.abouttheprogram = None
        self.nameUsers = None
        self.oldPos = None
        self.ui = Ui_Download
        self.setupUi(self)
        self.importmainclass = MainWindows
        RemoveWindowsMenu(self)

        self.id_Profile = id_Profile
        self.settings = settings

        # Перенос окна по используя frame в методах mouse press and event
        self.frame_4.move(0, 0)
        self.frame_4.show()


        self.SearchSoftWindows()#поиск софта
        #кнопка установить софт
        self.pushDownloadSteam.clicked.connect(self.buttonSteamDownload)
        self.pushDownloadGoogle.clicked.connect(self.buttonGoogleDownload)
        self.pushDownloadYandex.clicked.connect(self.buttonYandexDownload)
        self.pushDownloadOpera.clicked.connect(self.buttonOperaDownload)
        self.pushDownloadWatsApp.clicked.connect(self.buttonWhatsAppDownload)
        self.pushDownloadTG.clicked.connect(self.buttonTgDownload)
        self.pushDownloadViber.clicked.connect(self.buttonViberDownload)
        self.pushDownloadDS.clicked.connect(self.buttonDSDownload)
        self.pushDownloadTS.clicked.connect(self.buttonTSDownload)
        self.pushDownloadEpicGames.clicked.connect(self.buttonEpicGamesDownload)
        self.pushDownloadOrigin.clicked.connect(self.buttonOriginDownload)
        self.pushDownloadUplay.clicked.connect(self.buttonUplayDownload)
        self.pushDownloadBattleNet.clicked.connect(self.buttonBattleNetDownload)
        self.pushDownloadNvidea.clicked.connect(self.buttonNVIDIADownload)
        self.pushDownloadIntel.clicked.connect(self.buttonIntelDowmload)
        self.pushDownloadRyzen.clicked.connect(self.buttonRyzenDownload)
        self.pushDownloadRadion.clicked.connect(self.buttonRadionDownload)
        self.pushDownloadMalwarebytes.clicked.connect(self.buttonMalwarebytesDownload)
        self.pushDownloadEset.clicked.connect(self.buttonEsetDownload)

        self.pushDownloadXbox.clicked.connect(self.buttonXboxDownload)
        self.pushDownloadWeather.clicked.connect(self.buttonWeatherDownload)
        self.pushDownloadVoiceRec.clicked.connect(self.buttonVoiceRecDownload)
        self.pushDownloadStore.clicked.connect(self.buttonStoreDownload)
        self.pushDownloadPhoto.clicked.connect(self.buttonPhotoDownload)
        self.pushDownloadPeople.clicked.connect(self.buttonPeopleDownload)
        self.pushDownloadOneNote.clicked.connect(self.buttonOneNoteDownload)
        self.pushDownloadNews.clicked.connect(self.buttonNewsDownload)
        self.pushDownloadFilm.clicked.connect(self.buttonFilmDownload)
        self.pushDownloadMSC.clicked.connect(self.buttonMSCDownload)
        self.pushDownloadMap.clicked.connect(self.buttonMapDownload)
        self.pushDownloadGMusic.clicked.connect(self.buttonGMusicDownload)
        self.pushDownloadSkype.clicked.connect(self.buttonSkypeDownload)
        self.pushDownloadOffice.clicked.connect(self.buttonOfficeDownload)
        self.pushDownloadCamera.clicked.connect(self.buttonCameraDownload)
        self.pushDownloadAlarmClock.clicked.connect(self.buttonAlarmClockDownload)
        self.pushDownloadCalendarAndMail.clicked.connect(self.buttonCalendarAndMailDownload)
        self.pushDownloadCalc.clicked.connect(self.buttonCalcDownload)
        self.pushDownload3dBuilder.clicked.connect(self.button3dBuilderDownload)
        #кнопки удалить софт
        self.pushDelSteam.clicked.connect(self.buttonSteamDel)
        self.pushDelGoogle.clicked.connect(self.buttonGoogleDel)
        self.pushDelNvidea.clicked.connect(self.buttonNVIDIADel)
        self.pushDelYandex.clicked.connect(self.buttonYandexDel)
        self.pushDelOpera.clicked.connect(self.buttonOperaDel)
        self.pushDelWatsApp.clicked.connect(self.buttonWhatsAppDel)
        self.pushDelViber.clicked.connect(self.buttonViberDel)
        self.pushDelTG_2.clicked.connect(self.buttonTGDel)
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



    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self.frame_4.underMouse():
            self.offset = event.pos()
        else:
            self.offset = None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton and self.frame_4.underMouse():
            self.move(self.mapToGlobal(event.pos() - self.offset))
        else:
            self.offset = None



    def TransitionAboutTheProgram(self):
        self.ui = Class.AboutTheProgram.AboutTheProgram(self.id_Profile, self.settings)
        self.ui.show()
        self.hide()




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
            {"name": "Uplay",
             "path": "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher",
             "button": self.pushDownloadUplay},
            {"name": "Radeon",
             "path": "директория Radeon драйверов",
             "button": self.pushDownloadRadion}
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
            },
            {
                "name": "Name              : Microsoft.WindowsCamera",
                "command": "Get-AppxPackage *Microsoft.WindowsCamera*",
                "button": self.pushDownloadCamera
            },
            {
                "name": "Name              : Microsoft.WindowsAlarms",
                "command": "Get-AppxPackage *Microsoft.WindowsAlarms*",
                "button": self.pushDownloadAlarmClock
            }
        ]

        for soft in self.soft_main_windows:
            output = subprocess.run(["powershell", soft["command"]], capture_output=True, text=True)
            if soft["name"] in output.stdout:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,QtGui.QIcon.State.Off)
                soft["button"].setIcon(icon)


        for soft in self.softs:
            if gb.glob(soft["path"]):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,QtGui.QIcon.State.Off)
                soft["button"].setIcon(icon1)

#Установка приложений




    def DownloadAndLoadingSoft(self, url, xpath_site, file,  search, button):
        options = webdriver.ChromeOptions()
        prefs = {'safebrowsing.enabled': 'false'}
        options.add_experimental_option("prefs", prefs)

        browser = webdriver.Chrome(options=options)
        browser.get(url)

        xpath = xpath_site
        browser.find_element(By.XPATH, xpath).click()

        file_path = file
        # Не закрывайте браузер, пока файл в папке "Загрузки" не будет полностью загружен.
        while not os.path.isfile(file_path):
            time.sleep(1)
        print("Файл загружен!")
        browser.quit()
        proces = subprocess.Popen(file, shell=True)
        proces.wait()
        if os.path.isdir(search):
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            button.setIcon(icon1)


    def buttonGoogleDownload(self):
        url = 'https://disk.yandex.ru/d/0i6-aA45JOFCuQ'
        xpath_site = '/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]'
        file = f"C:/Users/{self.nameUsers}/Downloads/ChromeSetup.exe"
        search = f"C:/Program Files/Google/Chrome"
        button = self.pushDownloadGoogle
        xpath_coocki = "/html/body/div[1]/div/div/button"
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)

    def buttonOperaDownload(self):
        url = "https://disk.yandex.ru/d/tVuYVDzpaDcSbg"
        xpath_site ="/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/OperaGXSetup.exe"
        search = f"C:/Users/{self.nameUsers}/AppData/Local/Programs/Opera GX"
        button = self.pushDownloadOpera
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonYandexDownload(self):
        url = "https://disk.yandex.ru/d/XMr-W6g3C2ZOJQ"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/Yandex.exe"
        search = f"C:/Users/{self.nameUsers}/AppData/Local/Yandex/YandexBrowser"
        button = self.pushDownloadYandex
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)

    def buttonViberDownload(self):
        url = 'https://disk.yandex.ru/d/GanXehpAmS2AeA'
        xpath_site = '/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]'
        file = f"C:/Users/{self.nameUsers}/Downloads/ViberSetup.exe"
        search = f"C:/Users/{self.nameUsers}/AppData/Roaming/ViberPC"
        button = self.pushDownloadViber
        self.DownloadAndLoadingSoft(url, xpath_site, file,  search, button)

    def buttonDSDownload(self):
        url = 'https://disk.yandex.ru/d/jc0ugd_7swQjRQ'
        xpath_site = '/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]'
        file = f"C:/Users/{self.nameUsers}/Downloads/DiscordSetup.exe"
        search = f"C:/Users/{self.nameUsers}/AppData/Local/Discord"
        button = self.pushDownloadDS
        self.DownloadAndLoadingSoft(url, xpath_site, file,  search, button)

    def buttonTSDownload(self):
        url = 'https://disk.yandex.ru/d/_jvL082R196Jfw'
        xpath_site = '/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]'
        file = f"C:/Users/{self.nameUsers}/Downloads/TeamSpeak3-Client-win64-3.5.6.exe"
        search = "C:/Program Files/TeamSpeak 3 Client"
        button = self.pushDownloadTS
        self.DownloadAndLoadingSoft(url, xpath_site, file,  search, button)

    def buttonTgDownload(self):
        url = 'https://disk.yandex.ru/d/rghCP0xnXDshxw'
        xpath_site = '/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]'
        file = f"C:/Users/{self.nameUsers}/Downloads/tsetup-x64.4.7.1.exe"
        search = f"C:/Users/{self.nameUsers}/AppData/Roaming/Telegram Desktop"
        button = self.pushDownloadTG
        self.DownloadAndLoadingSoft(url, xpath_site, file,  search, button)

    def buttonSteamDownload(self):
        url = "https://disk.yandex.ru/d/uXZYf4SDu7vHGw"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/SteamSetup.exe"
        search = "C:/Program Files (x86)/Steam"
        button = self.pushDownloadSteam
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonEpicGamesDownload(self):
        url = "https://disk.yandex.ru/d/ixbNw_jU7bbyEg"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/EpicInstaller-14.6.2.msi"
        search = "C:/Program Files (x86)/Epic Games"
        button = self.pushDownloadEpicGames
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonOriginDownload(self):
        url = "https://disk.yandex.ru/d/mPDsJnYtL-bPHw"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/EAappInstaller.exe"
        search = "C:/Program Files/Electronic Arts/EA Desktop"
        button = self.pushDownloadOrigin
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonUplayDownload(self):
        url = "https://disk.yandex.ru/d/-pPkBQdgz6aQpg"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/UbisoftConnectInstaller.exe"
        search = "C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher"
        button = self.pushDownloadUplay
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonBattleNetDownload(self):
        url = "https://disk.yandex.ru/d/CIHyveUWjtaC2g"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/Battle.net-Setup.exe"
        search = "C:/Program Files (x86)/Battle.net"
        button = self.pushDownloadBattleNet
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonNVIDIADownload(self):
        url = "https://disk.yandex.ru/d/0HeyDs-WxlLMPA"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/GeForce_Experience_v3.27.0.112.exe"
        search = "C:/Program Files/NVIDIA Corporation"
        button = self.pushDownloadNvidea
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonIntelDowmload(self):
        url = "https://disk.yandex.ru/d/s1fBwbJhW-SvNg"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/Intel-Driver-and-Support-Assistant-Installer.exe"
        search = "C:\Program Files (x86)\Intel\Driver and Support Assistant"
        button = self.pushDownloadIntel
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonRyzenDownload(self):
        url = "https://disk.yandex.ru/d/UutTGYWf7eOpwA"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/amd-ryzen-master.exe"
        search = "C:/AMD/RyzenMasterExtract"
        button = self.pushDownloadRyzen
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonRadionDownload(self):
        url = "https://disk.yandex.ru/d/-1cXaKEtADNQbg"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/amd-software-adrenalin-edition-23.4.1-minimalsetup-230405_web.exe"
        search = "директория Radeon драйверов"
        button = self.pushDownloadRadion
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)
    def buttonEsetDownload(self):
        url = "https://disk.yandex.ru/d/Y1GKxluOyZ6jmQ"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/eset_nod32_antivirus_live_installer.exe"
        search = "C:/Program Files/ESET"
        button = self.pushDownloadRadion
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)

    def buttonMalwarebytesDownload(self):
        url = "https://disk.yandex.ru/d/gIzb4GP6nr4OrA"
        xpath_site = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[2]"
        file = f"C:/Users/{self.nameUsers}/Downloads/MBSetup-9B312069.exe"
        search = "C:/Program Files/Malwarebytes"
        button = self.pushDownloadRadion
        self.DownloadAndLoadingSoft(url, xpath_site, file, search, button)

    def DownloadAndLoading_WindowsSoft(self, productid, softs):
        webbrowser.open_new(productid)
        # До закрытия окна Microsoft Store следует ожидать, чтобы убедиться,
        # что приложение было успешно установлено, прежде чем запускать проверку установленного софта на Windows
        hwnd = win32gui.FindWindow(None, "Microsoft Store")
        while hwnd != 0:
            time.sleep(1)
            hwnd = win32gui.FindWindow(None, "Microsoft Store")
        # "Необходимо выполнить проверку установки приложения WhatsApp в
        # Microsoft Store, чтобы убедиться, что оно успешно установлено на компьютер
        for soft in softs:
            output = subprocess.run(["powershell", soft["command"]], capture_output=True, text=True)
            if soft["name"] in output.stdout:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal,QtGui.QIcon.State.Off)
                soft["button"].setIcon(icon)
    def buttonWhatsAppDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9NKSQGP7F2NH"
        softs = [
            {
                "name": "Name              : 5319275A.WhatsAppDesktop",
                "command": "Get-AppxPackage *WhatsApp*",
                "button": self.pushDownloadWatsApp
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonXboxDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9NZKPSTSNW4P"
        softs = [
            {
                "name": "Name              : Microsoft.XboxGamingOverlay",
                "command": "Get-AppxPackage Microsoft.XboxGamingOverlay",
                "button": self.pushDownloadXbox
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonWeatherDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFJ3Q2"
        softs = [
            {
                "name": 'Name              : Microsoft.BingWeather',
                "command": "Get-AppxPackage Microsoft.BingWeather",
                "button": self.pushDownloadWeather
            }]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonVoiceRecDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFHWKN"
        softs = [
            {
                "name": "Name              : Microsoft.WindowsSoundRecorder",
                "command": "Get-AppxPackage Microsoft.WindowsSoundRecorder",
                "button": self.pushDownloadVoiceRec
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonPhotoDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFHWKN"
        softs = [
            {
                "name": "Name              : Microsoft.Windows.Photos",
                "command": "Get-AppxPackage Microsoft.Windows.Photos",
                "button": self.pushDownloadPhoto
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonPeopleDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9NBLGGH10PG8"
        softs = [
            {
                "name": "Name              : Microsoft.People",
                "command": "Get-AppxPackage Microsoft.People",
                "button": self.pushDownloadPeople
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonOneNoteDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=XPFFZHVGQWWLHB"
        softs = [
            {
                "name": "Name              : Microsoft.Office.OneNote",
                "command": "Get-AppxPackage Microsoft.Office.OneNote",
                "button": self.pushDownloadOneNote
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonNewsDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFHVFW"
        softs = [
            {
                "name": "Name              : Microsoft.BingNews",
                "command": "Get-AppxPackage Microsoft.BingNews",
                "button": self.pushDownloadNews
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonFilmDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFJ3P2"
        softs = [
            {
                "name": "Name              : Microsoft.ZuneVideo",
                "command": "Get-AppxPackage Microsoft.ZuneVideo",
                "button": self.pushDownloadFilm
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonMSCDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9wzdncrfhwd2"
        softs = [
            {
                "name": "Name              : Microsoft.MicrosoftSolitaireCollection",
                "command": "Get-AppxPackage Microsoft.MicrosoftSolitaireCollection",
                "button": self.pushDownloadMSC
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonMapDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRDTBVB"
        softs = [
            {
                "name": "Name              : Microsoft.WindowsMaps",
                "command": "Get-AppxPackage Microsoft.WindowsMaps",
                "button": self.pushDownloadMap
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonGMusicDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFJ3PT"
        softs = [
            {
                "name": "Name              : Microsoft.ZuneMusic",
                "command": "Get-AppxPackage Microsoft.ZuneMusic",
                "button": self.pushDownloadGMusic
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonSkypeDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFJ364"
        softs = [
            {
                "name": "Name              : Microsoft.SkypeApp",
                "command": "Get-AppxPackage Microsoft.SkypeApp",
                "button": self.pushDownloadSkype
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonOfficeDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRD29V9"
        softs = [
            {
                "name": "Name              : Microsoft.MicrosoftOfficeHub",
                "command": "Get-AppxPackage Microsoft.MicrosoftOfficeHub",
                "button": self.pushDownloadOffice
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonCameraDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFJBBG"
        softs = [
            {
                "name": "Name              : Microsoft.WindowsCamera",
                "command": "Get-AppxPackage *Microsoft.WindowsCamera*",
                "button": self.pushDownloadCamera
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonAlarmClockDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFJ3PR"
        softs = [
            {
                "name": "Name              : Microsoft.WindowsAlarms",
                "command": "Get-AppxPackage *Microsoft.WindowsAlarms*",
                "button": self.pushDownloadAlarmClock
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonCalendarAndMailDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFHVQM"
        softs = [
            {
                "name": "Name              : Microsoft.windowscommunicationsapps",
                "command": "Get-AppxPackage Microsoft.windowscommunicationsapps",
                "button": self.pushDownloadCalendarAndMail
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def buttonCalcDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFHVN5"
        softs = [
            {
                "name": "Name              : Microsoft.WindowsCalculator",
                "command": "Get-AppxPackage Microsoft.WindowsCalculator",
                "button": self.pushDownloadCalc
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)
    def button3dBuilderDownload(self):
        productid = r"ms-windows-store://pdp/?ProductId=9WZDNCRFJ3T6"
        softs = [
            {
                "name": "Name              : Microsoft.3DBuilder",
                "command": "Get-AppxPackage Microsoft.3DBuilder",
                "button": self.pushDownload3dBuilder
            }
        ]
        self.DownloadAndLoading_WindowsSoft(productid, softs)

    def buttonStoreDownload(self):
        command = 'powershell -Command "Get-AppxPackage -allusers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\\AppXManifest.xml"}"'
        subprocess.check_call(command)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushDownloadStore.setIcon(icon1)
    #Удаление приложений

    #Не оптимизировано
    def buttonWhatsAppDel(self):
        powershell_command = f"Get-AppxPackage *WhatsAppDesktop* | Remove-AppxPackage"
        subprocess.run(["powershell.exe", "-Command", powershell_command], capture_output=True, text=True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                     QtGui.QIcon.State.Off)
        self.pushDownloadWatsApp.setIcon(icon1)

    def buttonGoogleDel(self):
        path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        subprocess.call([path, '--uninstall', '--multi-install', '--chrome'])
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,QtGui.QIcon.State.Off)
        self.pushDownloadGoogle.setIcon(icon1)

    def buttonYandexDel(self):
        path = f'C:/Users/{self.nameUsers}/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'
        subprocess.call([path, '--uninstall', '--system-level'])

    def buttonOperaDel(self):
        path = f'C:/Users/{self.nameUsers}/AppData/Local/Programs/Opera GX/opera.exe'
        subprocess.run([path, '--uninstall', '--system-level'], stdout=subprocess.PIPE)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushDownloadOpera.setIcon(icon1)





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
        uninstall_path = f"C:/Users/{self.nameUsers}/AppData/Roaming/Telegram Desktop/unins000.exe"
        subprocess.call([uninstall_path, "/S"])
        if os.path.exists(f"C:/Users/{self.nameUsers}/AppData/Roaming/Telegram Desktop"):
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            self.pushDownloadTG.setIcon(icon1)

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
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushDownloadDS.setIcon(icon1)

    def buttonTSDEL(self):
        try:
            shutil.rmtree('C:/Program Files/TeamSpeak 3 Client')
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
##############################################################################################################################
    #Оптимизировано
    def DelMainWindowsSoft(self, command, button):
        try:
            subprocess.run(["powershell", f"{command}"], capture_output=True, text=True)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-download-545759.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
            button.setIcon(icon1)
        except FileNotFoundError:
            pass

    def buttonXboxDel(self):
        command = "Get-AppxPackage *xboxapp* | Remove-AppxPackage"
        button = self.pushDownloadXbox
        self.DelMainWindowsSoft(command, button)
    def buttonWeatherDel(self):
        command = "Get-AppxPackage *bingweather* | Remove-AppxPackage"
        button = self.pushDownloadWeather
        self.DelMainWindowsSoft(command, button)
    def buttonVoiceRecDel(self):
        command = "Get-AppxPackage *soundrecorder* | Remove-AppxPackage"
        button = self.pushDownloadVoiceRec
        self.DelMainWindowsSoft(command, button)
    def buttonStoreDel(self):
        command = "Get-AppxPackage *windowsstore* | Remove-AppxPackage"
        button = self.pushDownloadStore
        self.DelMainWindowsSoft(command, button)
    def buttonPhotoDel(self):
        command = "Get-AppxPackage Microsoft.Windows.Photos | Remove-AppxPackage"
        button = self.pushDownloadPhoto
        self.DelMainWindowsSoft(command, button)
    def buttonPeopleDel(self):
        command = "Get-AppxPackage *люди* | Remove-AppxPackage | Remove-AppxPackage"
        button = self.pushDownloadPeople
        self.DelMainWindowsSoft(command, button)
    def buttonOneNote(self):
        command = "Get-AppxPackage *onenote* | Remove-AppxPackage"
        button = self.pushDownloadOneNote
        self.DelMainWindowsSoft(command, button)
    def buttonNewsDel(self):
        command = "Get-AppxPackage *bingnews* | Remove-AppxPackage"
        button = self.pushDownloadNews
        self.DelMainWindowsSoft(command, button)
    def buttonFilmDel(self):
        command = "Get-AppxPackage *zunevideo* | Remove-AppxPackage"
        button = self.pushDownloadFilm
        self.DelMainWindowsSoft(command, button)
    def buttonMSCDel(self):
        command = "Get-AppxPackage *solitairecollection* | Remove-AppxPackage"
        button = self.pushDownloadMSC
        self.DelMainWindowsSoft(command, button)
    def buttonMapDel(self):
        command = "Get-AppxPackage *windowsmaps* | Remove-AppxPackage"
        button = self.pushDownloadMap
        self.DelMainWindowsSoft(command, button)
    def buttonGMusicDel(self):
        command = "Get-AppxPackage *zunemusic* | Remove-AppxPackage"
        button = self.pushDownloadGMusic
        self.DelMainWindowsSoft(command, button)
    def buttonSkypeDel(self):
        command = "Get-AppxPackage *skypeapp* | Remove-AppxPackage"
        button = self.pushDownloadSkype
        self.DelMainWindowsSoft(command, button)
    def buttonOfficeDel(self):
        command = "Get-AppxPackage *officehub* | Remove-AppxPackage"
        button = self.pushDownloadOffice
        self.DelMainWindowsSoft(command, button)
    def buttonCameraDel(self):
        command = "Get-AppxPackage *windowscamera* | Remove-AppxPackage"
        button = self.pushDownloadCamera
        self.DelMainWindowsSoft(command, button)
    def buttonAlarmClockDel(self):
        command = "Get-AppxPackage *windowsalarms* | Remove-AppxPackage"
        button = self.pushDownloadAlarmClock
        self.DelMainWindowsSoft(command, button)
    def buttonCalendarAndMailDel(self):
        command = "Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage"
        button = self.pushDownloadCalendarAndMail
        self.DelMainWindowsSoft(command, button)
    def buttonCalcDel(self):
        command = "Get-AppxPackage *windowscalculator* | Remove-AppxPackage"
        button = self.pushDownloadCalc
        self.DelMainWindowsSoft(command, button)
    def button3dBuilder(self):
        command = "Get-AppxPackage * 3dbuilder * | Remove-AppxPackage"
        button = self.pushDownload3dBuilder
        self.DelMainWindowsSoft(command, button)