# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(1568, 926)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMaximumSize(QtCore.QSize(241, 377))
        self.scrollArea_2.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: black;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: #34373b;\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(119, 122, 126);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(119, 122, 126);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:black;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: black;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"*\n"
"{\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -173, 209, 550))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 550))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButtonPowerSupply = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
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
        self.verticalLayout_4.addWidget(self.pushButtonPowerSupply)
        self.pushButtonInterrupts = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButtonInterrupts.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInterrupts.setFont(font)
        self.pushButtonInterrupts.setStyleSheet("QPushButton#pushButtonInterrupts{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonInterrupts.setObjectName("pushButtonInterrupts")
        self.verticalLayout_4.addWidget(self.pushButtonInterrupts)
        self.pushButtonRegisryTweaks = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButtonRegisryTweaks.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRegisryTweaks.setFont(font)
        self.pushButtonRegisryTweaks.setStyleSheet("QPushButton#pushButtonRegisryTweaks{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonRegisryTweaks.setObjectName("pushButtonRegisryTweaks")
        self.verticalLayout_4.addWidget(self.pushButtonRegisryTweaks)
        self.pushButtonServise = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
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
        self.verticalLayout_4.addWidget(self.pushButtonServise)
        self.pushButtonMaster = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButtonMaster.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMaster.setFont(font)
        self.pushButtonMaster.setStyleSheet("QPushButton#pushButtonMaster{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonMaster.setObjectName("pushButtonMaster")
        self.verticalLayout_4.addWidget(self.pushButtonMaster)
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
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
        self.verticalLayout_4.addWidget(self.pushButtonClear)
        self.pushButtonAutoLoad = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButtonAutoLoad.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAutoLoad.setFont(font)
        self.pushButtonAutoLoad.setStyleSheet("QPushButton#pushButtonAutoLoad{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #161A1E;\n"
"    border-radius:25;\n"
"}")
        self.pushButtonAutoLoad.setObjectName("pushButtonAutoLoad")
        self.verticalLayout_4.addWidget(self.pushButtonAutoLoad)
        self.pushButtonDefoltSettings = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
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
        self.verticalLayout_4.addWidget(self.pushButtonDefoltSettings)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_2)
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
        self.pushButtonPowerSupply.setText(_translate("Settings", "Электропитание"))
        self.pushButtonInterrupts.setText(_translate("Settings", "Прерывания"))
        self.pushButtonRegisryTweaks.setText(_translate("Settings", "Твики реестра"))
        self.pushButtonServise.setText(_translate("Settings", "Службы"))
        self.pushButtonMaster.setText(_translate("Settings", "Мастер"))
        self.pushButtonClear.setText(_translate("Settings", "Очистка"))
        self.pushButtonAutoLoad.setText(_translate("Settings", "Автозагрузки"))
        self.pushButtonDefoltSettings.setText(_translate("Settings", "Базовые настройки"))
