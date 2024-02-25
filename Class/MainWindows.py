from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QMainWindow, QApplication

import Class.Registration
from main import *
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
from Class.AboutTheProgram import *
from Class.download import *
from Class.Registration import *

from Functions.BD.ClearDBLoggedIn.ClearDBLoggedIn import ClearDBLoggedIn
from Functions.BD.TransferringData.FromUsersToLogedIn import FromUsersToLoggedIn
from database.DB import client, db, coll, collLoggedIn
from ui_login import Ui_ImageDialog

class MainWindows(QDialog, Ui_ImageDialog):
    homeAction = None

    oldPos = QPoint()

    def __init__(self):
        super().__init__()
        self.password = None
        self.offset = None
        self.username = None
        self.dragPos = None
        self.reg = None
        self.abouttheprogram = None
        MainWindows.id_Profile = 6

        self.setupUi(self)

        RemoveWindowsMenu(self)#Убирает windows форму
        #БД
        self.client = client
        self.db = db
        self.coll = coll
        self.collLoggedIn = collLoggedIn
        #Запомнить пользователя
        self.settings = QSettings("ZoomIndistinct", 'AppWise')
        self.lineEdit.setText(self.settings.value("login", ""))
        self.lineEdit_2.setText(self.settings.value("password", ""))
        self.checkBox.setChecked(bool(self.settings.value("remember", "")))

        if self.settings.contains("login") and self.settings.contains("password"):
            self.LoginAutoLog()
        else:
            self.pushLogin.clicked.connect(self.login)



        self.connect_signals_text()


        # Кнопки
        self.pushClose.clicked.connect(self.CloseWindow)  # При нажатии на кнопку login перейти на новую страницу
        self.pushUrlYouTube.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.pushUrlDiscord.clicked.connect(lambda: webbrowser.open('https://discord.gg/JWTcSq3Y'))
        self.pushUrlFacebook.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/rrarrkfacit'))
        self.pushUrlGitHub.clicked.connect(lambda: webbrowser.open('https://github.com/'))
        self.status = self.label_4
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushReg.clicked.connect(self.WindowReg)



        #Перемещение окна UpBar
        self.UpBar.setStyleSheet("border-top-left-radius: 1px; ")
        self.UpBar.move(45, 35)
        self.UpBar.show()

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

    def login(self):

        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if self.checkBox.isChecked():
            self.settings = QSettings("ZoomIndistinct", 'AppWise')
            self.settings.setValue("login", self.username)
            self.settings.setValue("password", self.password)
            self.settings.setValue("remember", self.checkBox.isChecked())
        result_pass = db.users.find_one({'firstname': self.username, 'password': self.password})
        self.id_Profile = result_pass['_id']  # запомнить id пользователя после логина


        if len(self.username) == 0 or len(self.password) == 0:
            self.status.setText('Данные не введены')
        else:
            if not result_pass:
                self.status.setText('Логин или пароль указаны не верно')
            else:
                self.TransitionAboutTheProgram()


    def LoginAutoLog(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        result_pass = db.users.find_one({'firstname': self.username, 'password': self.password})
        self.id_Profile = result_pass['_id']  # запомнить id пользователя после логина
        self.TransitionAboutTheProgram()


    @staticmethod
    def CloseWindow():
        sys.exit()



    def TransitionAboutTheProgram(self):
        self.abouttheprogram = AboutTheProgram(self.id_Profile, self.settings)
        self.abouttheprogram.show()
        self.close()
        self.deleteLater()



    def WindowReg(self):
        self.reg = Class.Registration.Refistration()
        self.reg.show()
        self.hide()

    def connect_signals_text(self):
        self.label_3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:29pt; font-weight:600; color:#ffffff;\">zoomApp</span></p></body></html>")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushReg.setFont(font)
        self.pushReg.setText("Registration")
        self.pushLogin.setFont(font)
        self.pushLogin.setText("Login")
