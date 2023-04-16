import Class.Registration
from main import *
from Functions.RemoveWindowsMenu import RemoveWindowsMenu
from Class.AboutTheProgram import *
from Class.download import *
from Class.Registration import *
from Functions.BD.ClearDBLoggedIn.ClearDBLoggedIn import ClearDBLoggedIn
from Functions.BD.TransferringData.FromUsersToLogedIn import FromUsersToLoggedIn


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
                FromUsersToLoggedIn(self.username, self.password)#модуль добавляет зарегистрированного пользователя в бд LoggedIn
                self.TransitionAboutTheProgram()


    @staticmethod
    def CloseWindow():
        ClearDBLoggedIn()
        sys.exit()



    def TransitionAboutTheProgram(self):
        self.hide()
        self.abouttheprogram = AboutTheProgram()
        self.abouttheprogram.show()



    def WindowReg(self):
        self.reg = Class.Registration.Refistration()
        self.reg.show()
        self.hide()