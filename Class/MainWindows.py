from PyQt6.QtWidgets import QDialog

import Class.Registration
from ui_login import Ui_ImageDialog
import main
from main import *
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
from Class.AboutTheProgram import *
from Class.download import *
from Class.Registration import *


class MainWindows(QDialog, Ui_ImageDialog):
    homeAction = None

    oldPos = QPoint()

    def __init__(self):
        super().__init__()
        self.username = None
        self.dragPos = None
        self.reg = None
        self.abouttheprogram = None
        self.MainMenu = Ui_ImageDialog
        self.setupUi(self)
        self.setWindowTitle('ZoomApp')
        self.setWindowIcon(QtGui.QIcon('image/icon/logo.png'))

        RemoveWindowsMenu(self)#Убирает windows форму


        # Кнопки
        self.pushClose.clicked.connect(self.CloseWindow)  # При нажатии на кнопку login перейти на новую страницу
        self.pushUrlYouTube.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.pushUrlDiscord.clicked.connect(lambda: webbrowser.open('https://discord.gg/JWTcSq3Y'))
        self.pushUrlFacebook.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/rrarrkfacit'))
        self.pushUrlGitHub.clicked.connect(lambda: webbrowser.open('https://github.com/'))
        self.pushLogin.clicked.connect(self.login)
        self.status = self.label_4
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushReg.clicked.connect(self.WindowReg)


    def center(self):
        qr = self.UpBar()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def login(self):
        # создание бд и проверка ввода логина и пароля
        db = sqlite3.connect('database\contacts.db')
        coursor = db.cursor()
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        coursor.execute(f'SELECT * FROM users WHERE firstname like \"{self.username}\" and password like \"{self.password}\";')
        result_pass = coursor.fetchone()
        db.close()
        # проверка ввода
        if len(self.username) == 0 or len(self.password) == 0:
            self.status.setText('Данные не введены')
        else:
            if not result_pass:
                self.status.setText('Логин или пароль указаны не верно')
            else:
                db = sqlite3.connect('database\contacts.db')
                coursor = db.cursor()
                coursor.execute(f"SELECT id FROM users WHERE firstname = '{self.username}' AND password = '{self.password}'")
                result = coursor.fetchone()

                if result is not None:
                    user_id = result[0]

                    # Get the user's details
                    coursor.execute(f"SELECT firstname, password, email FROM users WHERE id = {user_id}")
                    result = coursor.fetchone()

                    if result is not None:
                        firstname, password, email = result

                        # Insert the user's details into the LoggedIn table
                        coursor.execute(f"INSERT INTO LoggedIn (firstname, password, email) VALUES (?, ?, ?)", (firstname, password, email))
                        db.commit()

                        print("User logged in successfully!")
                    else:
                        print("User details not found!")
                else:
                    print("User not found!")

                db.close()
                self.TransitionAboutTheProgram()


    @staticmethod
    def CloseWindow():
        db = sqlite3.connect('database\contacts.db')
        coursor = db.cursor()
        coursor.execute(f"DELETE FROM LoggedIn;")
        db.commit()
        db.close()
        print('Данные очищены')
        sys.exit()



    def TransitionAboutTheProgram(self):
        self.hide()
        self.abouttheprogram = AboutTheProgram()
        self.abouttheprogram.show()



    def WindowReg(self):
        self.reg = Class.Registration.Refistration()
        self.reg.show()
        self.hide()