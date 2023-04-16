import re
import sqlite3

from PyQt6.QtWidgets import QDialog
from main import *
import main
import Class.MainWindows
from ui_reg import Ui_Ui_Reg
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
from PyQt6.QtGui import QMouseEvent

class Refistration(QDialog, Ui_Ui_Reg):
    def __init__(self):
        super().__init__()
        self.offset = None
        self.abouttheprogram = None
        self.oldPos = None
        self.ui = Ui_Ui_Reg
        self.setupUi(self)
        RemoveWindowsMenu(self)

        self.MainClass = Class.MainWindows.MainWindows()  # Методы из MainWindows

        self.pushClose.clicked.connect(self.MainClass.CloseWindow)
        self.pushReg.clicked.connect(self.register)
        # self.RemoveWindowsMenu()
        self.status = self.label_2
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushBack.clicked.connect(self.PushBack)

        # Перемещение окна UpBar
        self.UpBar.move(80, 35)
        self.UpBar.setFixedHeight(50)
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



    def PushBack(self):
        self.ui = main.MainWindows()
        self.ui.show()
        self.hide()

    #

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
