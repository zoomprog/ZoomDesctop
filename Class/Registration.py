import re
import sqlite3

from PyQt6.QtWidgets import QDialog
from main import *
import main
import Class.MainWindows
from ui_reg import Ui_Ui_Reg
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
from PyQt6.QtGui import QMouseEvent
from database.DB import db, coll, collLoggedIn


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

        firstname = self.FirstName.text()
        lastname = self.LastName.text()
        email = self.Email.text()
        password = self.Password.text()
        confirmpassword = self.ConfirmPassword.text()

        # Проверка пароля
        regex = re.compile(r'[A-Za-z0-9]+([._-][A-Za-z0-9]+)*@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
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
        result_count = coll.users.count_documents({"firstname": firstname, "email": email})

        if result_count == 0 and count_digit >= 3 and count_upper > 0 and count_spec > 0 and 6 <= len(password) <= 20 and len(firstname) > 0 and re.fullmatch(regex, email):
            coll.insert_one({
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "password": password,
                "confirmpassword": confirmpassword
            })
            xxx = db.users.find_one({'firstname': firstname, 'password': password})
            self.id_Profile = xxx['_id']  # запомнить id пользователя после логина
            self.abouttheprogram = main.MainWindows()  # Replace 'settings' with the appropriate argument

            self.abouttheprogram.show()
            self.hide()

        else:
            if password != confirmpassword:
                self.status.setText('Пароли не совпадают')
            elif len(password) < 6:
                self.status.setText('Пароль слишком короткий')
            elif len(password) > 20:
                self.status.setText('Пароль слишком длинный')
            elif count_spec == 0:
                self.status.setText('Пароль должен содержать хотя бы один специальный символ (!@#$%&)')
            elif count_upper == 0:
                self.status.setText('Пароль должен содержать хотя бы одну заглавную букву')
            elif count_digit < 3:
                self.status.setText('Пароль должен содержать хотя бы три цифры')
            elif len(firstname) < 5:
                self.status.setText('Имя пользователя должно быть не менее 5 символов')
            elif not re.fullmatch(regex, email):
                self.status.setText('Email указан неверно')
            else:
                self.status.setText('Аккаунт с данными уже был зарегистрирован')

