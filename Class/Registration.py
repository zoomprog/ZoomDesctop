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

    def is_valid_password(self, password):
        count_digit = sum(c.isdigit() for c in password)
        count_upper = sum(c.isupper() for c in password)
        count_spec = sum(c in '!@#$%&' for c in password)

        return count_digit >= 3 and count_upper > 0 and count_spec > 0 and 6 <= len(password) <= 20

    def is_valid_email(self, email):
        regex = re.compile(r'[A-Za-z0-9]+([._-][A-Za-z0-9]+)*@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
        return re.fullmatch(regex, email)

    def register(self):
        firstname = self.FirstName.text()
        lastname = self.LastName.text()
        email = self.Email.text()
        password = self.Password.text()
        confirmpassword = self.ConfirmPassword.text()

        existing_user = coll.users.find_one({"email": email})

        if existing_user is not None:
            # Пользователь существует, выводим сообщение об ошибке
            self.status.setText('Аккаунт с данными уже был зарегистрирован')
        elif password != confirmpassword:
            self.status.setText('Пароли не совпадают')
        elif len(password) < 6:
            self.status.setText('Пароль слишком короткий')
        elif len(password) > 20:
            self.status.setText('Пароль слишком длинный')
        elif not self.is_valid_password(password):
            self.status.setText('Некорректный формат пароля')
        elif len(firstname) < 5:
            self.status.setText('Имя пользователя должно быть не менее 5 символов')
        elif not self.is_valid_email(email):
            self.status.setText('Email указан неверно')
        else:
            # Пользователя нет, производим регистрацию
            insert_result = coll.users.insert_one({
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "password": password,
                "confirmpassword": confirmpassword
            })

            if insert_result.inserted_id:
                self.id_Profile = insert_result.inserted_id
                # Ваши дальнейшие действия с id_Profile
                self.abouttheprogram = main.MainWindows()
                self.abouttheprogram.show()
                self.hide()
            else:
                # Обработка ситуации, когда не удалось получить _id после регистрации
                self.status.setText('Ошибка при логине. Проверьте правильность введенных данных.')

