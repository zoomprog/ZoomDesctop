import psutil

import main
import Class.MainWindows
from main import *
from ui_AboutTheProgram import Ui_AboutTheProgram
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
import Class.download
import Class.Settings
from PyQt6.QtWidgets import QWidget, QDialog
from PyQt6.QtGui import QMouseEvent
from database.DB import db, coll, collLoggedIn
from database import *
from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QVBoxLayout
from Widget.Disk.DiskVisual import DiskUsageWidget


class AboutTheProgram(QDialog, Ui_AboutTheProgram):
    def __init__(self, id_Profile, settings):
        super().__init__()

        self.dialog = None
        self.offset = None
        self.oldPos = None
        self.ui = None
        self.logo_text = None
        self.abouttheprogram = Ui_AboutTheProgram
        self.setupUi(self)
        RemoveWindowsMenu(self)  # Убирает windows форму
        self.connect_signals_text()

        self.id_Profile = id_Profile
        self.settings = settings

        self.importmainclass = main.MainWindows
        self.importregclass = main.Refistration
        self.nameUsers = os.getlogin()
        if os.path.isfile(f'/Users/{self.nameUsers}\Downloads/soft.txt'):
            os.remove(f'/Users/{self.nameUsers}\Downloads/soft.txt')
            print("success")
        else:
            print("File doesn't exists!")

        #Импорт основных методов передвижение окна windows и убарать windows элементы из виджета.
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)  #кнопка завершение программы
        self.pushCollapse.clicked.connect(self.showMinimized)  #Сворачивание окна
        self.pushExit.clicked.connect(self.PushBack)  #кнопка для выхода с аккаунта
        self.pushDownload.clicked.connect(self.download)
        self.pushSetting.clicked.connect(self.ButtonSettings)

        #Достаем логин и email из бд для Profile
        Profile = coll.find_one({"_id": self.id_Profile})
        self.ProfileLogin = Profile.get("firstname")
        self.ProfileEmail = Profile.get("email")
        if Profile:
            print("login", self.ProfileLogin)
            print("Email", self.ProfileEmail)
        else:
            print("User not dound")

        #Перенос окна по используя frame в методах mouse press and event
        self.header_frame.move(0, 0)
        self.header_frame.show()

        #Работа с кнопкой профиль
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pushButtonProfile)
        self.setLayout(self.layout)
        self.pushButtonProfile.clicked.connect(self.on_button_clicked)

        self.animation = QPropertyAnimation(self.pushButtonProfile, b"size")
        self.animation.setDuration(600)

        self.is_expanded = False

        # Создаем layout для frame_Disk
        self.diskLayout = QVBoxLayout(self.frame_Disk)
        self.diskLayout.setContentsMargins(0, 0, 0, 10)

        # Определение доступных дисков и создание виджетов для каждого
        for disk in self.get_available_disks():
            disk_widget = DiskUsageWidget(disk)
            self.diskLayout.addWidget(disk_widget)

        # Устанавливаем layout в frame_Disk
        self.frame_Disk.setLayout(self.diskLayout)

    @staticmethod
    def get_available_disks():
        # Получаем список всех дисков
        disks = []
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':  # Для Windows
                if 'fixed' in part.opts or 'removable' in part.opts:
                    disks.append(part.device.rstrip('\\'))
        return disks

    def on_button_clicked(self):
        if self.animation.state() == QAbstractAnimation.State.Stopped:
            if not self.is_expanded:
                # Увеличение кнопки при нажатии
                self.animation.setStartValue(QSize(self.pushButtonProfile.width(), 51))
                self.animation.setEndValue(QSize(self.pushButtonProfile.width(), 115))
                self.animation.start()

                self.pushButtonProfile.setText("")
                timer = QTimer()
                timer.singleShot(500, self.AppealProfileLabelVisibility)
                print('Увеличилась')
                self.is_expanded = True
            else:
                # Уменьшение кнопки при нажатии
                self.animation.setStartValue(QSize(self.pushButtonProfile.width(), 115))
                self.animation.setEndValue(QSize(self.pushButtonProfile.width(), 51))
                self.animation.start()

                # Добавление контента внутри кнопки
                timer = QTimer()
                timer.singleShot(0, self.AppealProfileLabelHide)

                print('Уменьшилась')
                self.is_expanded = False

    def AppealProfileLabelVisibility(self):
        self.label_ProfileLogo.setStyleSheet('background-color:transparent;color:white;')
        self.label_ProfileName.setStyleSheet('background-color:transparent;color:white;')
        self.label_ProfileEmail.setStyleSheet('background-color:transparent;color:white;')
        self.label_ProfileSub.setStyleSheet('background-color:transparent;color:white;')

        self.label_EnterProfileName.setText(self.ProfileLogin)
        self.label_EnterProfileEmail.setText(self.ProfileEmail)
        self.label_EnterProfileName.setStyleSheet('background-color:transparent;color:white;')
        self.label_EnterProfileEmail.setStyleSheet('background-color:transparent;color:white;')
        self.pushButtonSubPrmium.setStyleSheet('background-color:transparent;color:white;')

    def AppealProfileLabelHide(self):
        self.pushButtonProfile.setText("Profile")

        self.label_ProfileLogo.setStyleSheet('background-color:transparent;color:transparent;')
        self.label_ProfileName.setStyleSheet('background-color:transparent;color:transparent;')
        self.label_ProfileEmail.setStyleSheet('background-color:transparent;color:transparent;')
        self.label_ProfileSub.setStyleSheet('background-color:transparent;color:transparent;')

        self.label_EnterProfileName.setText("")
        self.label_EnterProfileEmail.setText("")
        self.label_EnterProfileName.setStyleSheet('background-color:transparent;color:transparent;')
        self.label_EnterProfileEmail.setStyleSheet('background-color:transparent;color:transparent;')
        self.pushButtonSubPrmium.setStyleSheet('background-color:transparent;color:transparent;')

    def download(self):
        self.ui = Class.download.Download(self.id_Profile, self.settings)
        self.ui.show()
        self.hide()

    def PushBack(self):
        self.settings.clear()
        self.frame_12.close()
        self.ui = main.MainWindows()
        self.ui.show()
        self.close()
        self.deleteLater()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self.header_frame.underMouse():
            self.offset = event.pos()
        else:
            self.offset = None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton and self.header_frame.underMouse():
            self.move(self.mapToGlobal(event.pos() - self.offset))
        else:
            self.offset = None

    def ButtonSettings(self):
        self.ui = Class.Settings.Setings()
        self.ui.show()
        self.hide()

    def connect_signals_text(self):
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pushDownload.setFont(font)
        self.pushDownload.setText("SOFT")
        self.pushSetting.setFont(font)
        self.pushSetting.setText("SETTINGS")
        self.pushActivate.setFont(font)
        self.pushActivate.setText("ACTIVATE")
        self.pushButtonProfile.setFont(font)
        self.pushButtonProfile.setText("Profile")
        self.pushDownloadUpdate.setFont(font)
        self.pushDownloadUpdate.setText("Скачать")
