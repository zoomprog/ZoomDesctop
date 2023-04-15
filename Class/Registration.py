import re
import sqlite3

from PyQt6.QtWidgets import QDialog
from main import *
import main
from ui_reg import Ui_Reg
from Functions.RemoveWindowsMenu import RemoveWindowsMenu

class Refistration(QDialog, Ui_Reg):
    def __init__(self):
        super().__init__()
        self.abouttheprogram = None
        self.oldPos = None
        self.ui = Ui_Reg
        self.setupUi(self)
        RemoveWindowsMenu(self)



        # self.importmainclass = MainWindows()
        # self.pushClose.clicked.connect(self.importmainclass.CloseWindow)
        self.pushReg.clicked.connect(self.register)
        # self.RemoveWindowsMenu()
        self.status = self.label_2
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushBack.clicked.connect(self.PushBack)

    def PushBack(self):
        self.ui = main.MainWindows()
        self.ui.show()
        self.hide()
    # def RemoveWindowsMenu(self):
    #     self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    #     self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
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

        # Проверка пароля
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  # проверка email
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
                self.abouttheprogram = main.AboutTheProgram()
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
