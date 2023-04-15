import cgi
import sqlite3
import sys
import webbrowser
import re
import os

import requests
import wget
import subprocess

from PyQt6.QtGui import QMouseEvent, QColor

import login
import menu
import DownloadSoft
from Class.download import *
from PyQt6.QtWidgets import QDialog, QGraphicsColorizeEffect, QPushButton,QApplication,QLabel,QVBoxLayout
from PyQt6 import QtWidgets, QtCore, QtGui
from ui_login import Ui_ImageDialog
from ui_AboutTheProgram import Ui_AboutTheProgram
from ui_Download import Ui_Download
from ui_reg import Ui_Reg
from PyQt6.QtCore import Qt, QPropertyAnimation, QSize, QAbstractAnimation

from PyQt6.QtCore import Qt, QPoint
from Class.download import *




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





        # Кнопки
        self.pushClose.clicked.connect(self.CloseWindow)  # При нажатии на кнопку login перейти на новую страницу
        self.pushUrlYouTube.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.pushUrlDiscord.clicked.connect(lambda: webbrowser.open('https://discord.gg/JWTcSq3Y'))
        self.pushUrlFacebook.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/rrarrkfacit'))
        self.pushUrlGitHub.clicked.connect(lambda: webbrowser.open('https://github.com/'))
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.pushLogin.clicked.connect(self.login)
        self.status = self.label_4
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushReg.clicked.connect(self.WindowReg)
        self.RemoveWindowsMenu()

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
        self.reg = Refistration()
        self.reg.show()
        self.hide()
    def RemoveWindowsMenu(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)




class AboutTheProgram(QDialog, Ui_AboutTheProgram,Ui_ImageDialog):
    def __init__(self):
        super().__init__()

        self.oldPos = None
        self.ui = None
        self.logo_text = None
        self.abouttheprogram = Ui_AboutTheProgram
        self.setupUi(self)
        self.importmainclass = MainWindows
        self.importregclass = Refistration
        self.nameUsers = os.getlogin()
        if os.path.isfile(f'/Users/{self.nameUsers}\Downloads/soft.txt'):
            os.remove(f'/Users/{self.nameUsers}\Downloads/soft.txt')
            print("success")
        else:
            print("File doesn't exists!")

        #Импорт основных методов передвижение окна windows и убарать windows элементы из виджета.
        self.importmainclass.RemoveWindowsMenu(self)
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)#кнопка завершение программы
        self.pushCollapse.clicked.connect(self.showMinimized)#Сворачивание окна
        self.pushExit.clicked.connect(self.PushBack)#кнопка для выхода с аккаунта
        self.pushDownload.clicked.connect(self.download)


        #Достаем логин и email из бд
        db = sqlite3.connect('database\contacts.db')
        coursor = db.cursor()
        coursor.execute(f"SELECT firstname, email FROM LoggedIn")
        results = coursor.fetchone()
        if results is not None:
            self.ProfileLogin = results[0]
            self.ProfileEmail = results[1]
            print('Loggn:'+self.ProfileLogin,'\nPassword:'+ self.ProfileEmail)
        else:
            print('No logged in user found.')
        db.close()

        #Работа с кнопкой профиль
        self.layout = QVBoxLayout()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pushButtonProfile)
        self.setLayout(self.layout)
        self.pushButtonProfile.clicked.connect(self.on_button_clicked)
        self.animation = None
        self.is_expanded = False

    def on_button_clicked(self):
        if not self.animation or self.animation.state() == QAbstractAnimation.State.Stopped:
            if not self.is_expanded:
                #Увеличение кнопки при нажатии
                self.animation = QPropertyAnimation(self.pushButtonProfile, b"minimumSize")
                self.animation.setDuration(600)
                self.animation.setStartValue(QSize(self.pushButtonProfile.width(), 115))
                self.animation.start()
                #Добавление контента внутри кнопки
                self.pushButtonProfile.setText("")
                self.label_ProfileLogo.setStyleSheet('background-color:transparent;color:white;')
                self.label_ProfileName.setStyleSheet('background-color:transparent;color:white;')
                self.label_ProfileEmail.setStyleSheet('background-color:transparent;color:white;')
                self.label_ProfileSub.setStyleSheet('background-color:transparent;color:white;')

                self.label_EnterProfileName.setText(self.ProfileLogin)
                self.label_EnterProfileEmail.setText(self.ProfileEmail)
                self.label_EnterProfileName.setStyleSheet('background-color:transparent;color:white;')
                self.label_EnterProfileEmail.setStyleSheet('background-color:transparent;color:white;')
                print('Увеличилась')
                self.is_expanded = True
            else:
                #Уменьшение кнопки при нажатии
                self.animation = QPropertyAnimation(self.pushButtonProfile, b"maximumSize")
                self.animation.setDuration(600)
                self.animation.setStartValue(QSize(self.pushButtonProfile.width(), 51))
                self.animation.start()
                #Добавление контента внутри кнопки
                self.pushButtonProfile.setText("Profile")
                self.label_ProfileLogo.setStyleSheet('background-color:transparent;color:transparent;')
                self.label_ProfileName.setStyleSheet('background-color:transparent;color:transparent;')
                self.label_ProfileEmail.setStyleSheet('background-color:transparent;color:transparent;')
                self.label_ProfileSub.setStyleSheet('background-color:transparent;color:transparent;')


                self.label_EnterProfileName.setStyleSheet('background-color:transparent;color:transparent;')
                self.label_EnterProfileEmail.setStyleSheet('background-color:transparent;color:transparent;')
                print('Уменьшилась')
                self.is_expanded = False



    def download(self):
        self.ui = Download()
        self.ui.show()
        self.hide()









    def PushBack(self):
        self.ui = MainWindows()
        self.ui.show()
        self.hide()
from pyuac import main_requires_admin




class Refistration(QDialog, Ui_Reg):
    def __init__(self):
        super().__init__()
        self.abouttheprogram = None
        self.oldPos = None
        self.ui = Ui_Reg
        self.setupUi(self)
        self.importmainclass = MainWindows
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)
        self.pushReg.clicked.connect(self.register)
        self.importmainclass.RemoveWindowsMenu(self)
        self.status = self.label_2
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushBack.clicked.connect(self.PushBack)



    def PushBack(self):
        self.ui = MainWindows()
        self.ui.show()
        self.hide()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def register(self):
        db = sqlite3.connect('database\contacts.db')
        coursor = db.cursor()
        firstname = self.FirstName.text()
        lastname = self.LastName.text()
        email = self.Email.text()
        password = self.Password.text()
        confirmpassword = self.ConfirmPassword.text()

        #Проверка пароля
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')#проверка email
        count_digit = 0
        count_upper = 0
        count_spec = 0
        spec_simvol = '!@#$%&'
        for s in password:
            if s.isdigit():
                count_digit += 1
            if s.isupper():
                count_upper += 1
            if s in spec_simvol:
                count_spec += 1

        coursor.execute(f'SELECT * FROM users WHERE firstname like \"{firstname}\" and email like \"{email}\";')
        result_pass = coursor.fetchone()


        if not result_pass:
            if count_digit >= 3 and count_upper > 0 and count_spec > 0 and 6 <= len(password) <= 20 and len(
                    firstname) > 0 and re.fullmatch(regex, email):
                coursor.execute('INSERT INTO  users VALUES(?,?,?,?,?,?);',
                                (firstname, lastname, email, password, confirmpassword, None))
                self.abouttheprogram = AboutTheProgram()
                self.abouttheprogram.show()
                self.hide()
                db.commit()
                db.close()

            else:
                if password != confirmpassword:
                    self.status.setText('Пароли не верны')
                else:
                    if len(password) < 4:
                        self.status.setText('Пароль слишком короткий')
                    else:
                        if len(password) > 20:
                            self.status.setText('Пароль слишком длинный')
                        else:
                            if count_spec == 0:
                                self.status.setText('Нет специальных символов')
                            else:
                                if count_upper == 0:
                                    self.status.setText('Нет заглавных букв')
                                else:
                                    if count_digit < 3:
                                        self.status.setText('Нет строчных букв')
                                    else:
                                        if len(firstname) < 5:
                                            self.status.setText('Ник нейм короткий')
                                        else:
                                            if not re.fullmatch(regex, email):
                                                self.status.setText('Email указан не верно')
                                            else:
                                                self.status.setText('Аккаунт с данными уже был зарегистрирован')




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QStackedWidget()
    maindow = MainWindows()
    maindow.show()
    sys.exit(app.exec())