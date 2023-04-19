
import main
import Class.MainWindows
from main import *
from ui_AboutTheProgram import Ui_AboutTheProgram
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
import Class.download
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QMouseEvent
from database.DB import db, coll,collLoggedIn
from database import *
from PyQt6.QtCore import QSettings


class AboutTheProgram(QDialog, Ui_AboutTheProgram,Ui_ImageDialog):
    def __init__(self,id_Profile,settings):
        super().__init__()

        self.offset = None
        self.oldPos = None
        self.ui = None
        self.logo_text = None
        self.abouttheprogram = Ui_AboutTheProgram
        self.setupUi(self)
        RemoveWindowsMenu(self)  # Убирает windows форму
        self.id_Profile = id_Profile
        print(self.id_Profile)
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
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)#кнопка завершение программы
        self.pushCollapse.clicked.connect(self.showMinimized)#Сворачивание окна
        self.pushExit.clicked.connect(self.PushBack)#кнопка для выхода с аккаунта
        self.pushDownload.clicked.connect(self.download)


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

    def download(self):
        self.ui = Class.download.Download()
        self.ui.show()
        self.hide()

    def PushBack(self):
        self.settings.clear()
        self.frame_12.close()
        self.ui = main.MainWindows()
        self.ui.show()


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



