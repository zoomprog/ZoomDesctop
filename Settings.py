# Form implementation generated from reading ui file '.\Settings.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(1568, 922)
        Settings.setMinimumSize(QtCore.QSize(1280, 720))
        Settings.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.frame_2 = QtWidgets.QFrame(parent=Settings)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 1280, 720))
        self.frame_2.setMinimumSize(QtCore.QSize(1280, 720))
        self.frame_2.setStyleSheet("*\n"
"{\n"
"    border: none;\n"
"     background-color:black;\n"
"    border-radius:30;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.UpBar = QtWidgets.QFrame(parent=self.frame_2)
        self.UpBar.setMaximumSize(QtCore.QSize(16777215, 100))
        self.UpBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.UpBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.UpBar.setObjectName("UpBar")
        self.label_3 = QtWidgets.QLabel(parent=self.UpBar)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 200, 50))
        self.label_3.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(85, 255, 255);\n"
"qproperty-alignment: \'AlignCenter\';")
        self.label_3.setObjectName("label_3")
        self.frame_6 = QtWidgets.QFrame(parent=self.UpBar)
        self.frame_6.setGeometry(QtCore.QRect(1120, 20, 128, 66))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonCollaps = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButtonCollaps.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/image/icon/free-icon-minimize-4889317.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCollaps.setIcon(icon)
        self.pushButtonCollaps.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonCollaps.setObjectName("pushButtonCollaps")
        self.horizontalLayout.addWidget(self.pushButtonCollaps)
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButtonClose.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonClose.setIcon(icon1)
        self.pushButtonClose.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout_2.addWidget(self.UpBar)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(1280, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_3.setMinimumSize(QtCore.QSize(241, 602))
        self.frame_3.setMaximumSize(QtCore.QSize(241, 602))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButtonDefoltSettings = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonDefoltSettings.setGeometry(QtCore.QRect(20, 10, 200, 50))
        self.pushButtonDefoltSettings.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDefoltSettings.setFont(font)
        self.pushButtonDefoltSettings.setStyleSheet("QPushButton#pushButtonDefoltSettings{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonDefoltSettings.setObjectName("pushButtonDefoltSettings")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonClear.setGeometry(QtCore.QRect(20, 70, 191, 50))
        self.pushButtonClear.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setStyleSheet("QPushButton#pushButtonClear{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonServise = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonServise.setGeometry(QtCore.QRect(20, 130, 191, 50))
        self.pushButtonServise.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonServise.setFont(font)
        self.pushButtonServise.setStyleSheet("QPushButton#pushButtonServise{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonServise.setObjectName("pushButtonServise")
        self.pushButtonPowerSupply = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonPowerSupply.setGeometry(QtCore.QRect(20, 190, 191, 50))
        self.pushButtonPowerSupply.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPowerSupply.setFont(font)
        self.pushButtonPowerSupply.setStyleSheet("QPushButton#pushButtonPowerSupply{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonPowerSupply.setObjectName("pushButtonPowerSupply")
        self.pushButtonPrivacy = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonPrivacy.setGeometry(QtCore.QRect(20, 250, 191, 50))
        self.pushButtonPrivacy.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPrivacy.setFont(font)
        self.pushButtonPrivacy.setStyleSheet("QPushButton#pushButtonPrivacy{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonPrivacy.setObjectName("pushButtonPrivacy")
        self.pushButtonTasks = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonTasks.setGeometry(QtCore.QRect(20, 310, 191, 50))
        self.pushButtonTasks.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonTasks.setFont(font)
        self.pushButtonTasks.setStyleSheet("QPushButton#pushButtonTasks{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonTasks.setObjectName("pushButtonTasks")
        self.pushBack = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushBack.setGeometry(QtCore.QRect(40, 380, 131, 131))
        self.pushBack.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushBack.setFont(font)
        self.pushBack.setStyleSheet("QPushButton {\n"
"    background-color: #161A1E;\n"
"    color: white;\n"
"    border-radius: 65px; /* Уточним единицы измерения для радиуса */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(115, 128, 142, 255);\n"
"    border: 4px solid #00BFFF;\n"
"}\n"
"")
        self.pushBack.setObjectName("pushBack")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.MainBody = QtWidgets.QFrame(parent=self.frame_4)
        self.MainBody.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MainBody.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MainBody.setObjectName("MainBody")
        self.horizontalLayout_2.addWidget(self.MainBody)
        self.verticalLayout_2.addWidget(self.frame_4)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.label_3.setText(_translate("Settings", "ZoomMod"))
        self.pushButtonDefoltSettings.setText(_translate("Settings", "Базовые настройки"))
        self.pushButtonClear.setText(_translate("Settings", "Очистка"))
        self.pushButtonServise.setText(_translate("Settings", "Службы"))
        self.pushButtonPowerSupply.setText(_translate("Settings", "Электропитание"))
        self.pushButtonPrivacy.setText(_translate("Settings", "Приватность"))
        self.pushButtonTasks.setText(_translate("Settings", "Задачи"))
        self.pushBack.setText(_translate("Settings", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QWidget()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec())
