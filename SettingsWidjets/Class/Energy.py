import sys
import time

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QDialog, QApplication, QMenu
from SettingsWidjets.EnergyPower import Ui_Energy

from Functions.Energy.Preset.Balanced import Balance_Preset
from Functions.Energy.Preset.HightPerformance import Hight_Performance_Preset
from Functions.Energy.Preset.PowerSaver import PowerSaver_Preset
from Functions.Energy.Hibernation.check_hibernation import check_hibernation_PC
from Functions.Energy.Hibernation.hibernation_OnAndOff import hibernation_PC_ON, hibernation_PC_OFF



class EnergyWindows(QDialog, Ui_Energy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(1)
        self.pushEnergy_Preset.clicked.connect(self.showMenu)

        # Изменение навзвание кнопок


        self.updateHibernationButton()
        self.pushHibernation.clicked.connect(self.hibernationButtonClicked)




        # Создаем меню и добавляем дополнительные кнопки
        self.menu = QMenu(self.pushEnergy_Preset)

        # Create QAction instances for each QPushButton
        action1 = QAction(QIcon(), "Balans", self)
        action2 = QAction(QIcon(), "Performance", self)
        action3 = QAction(QIcon(), "Power Saver", self)

        # Connect each action to a slot if needed
        action1.triggered.connect(self.onButton1Clicked)
        action2.triggered.connect(self.onButton2Clicked)
        action3.triggered.connect(self.onButton3Clicked)

        # Add the actions to the menu
        self.menu.addAction(action1)
        self.menu.addAction(action2)
        self.menu.addAction(action3)
        menu_style = """
                    QMenu {
                        background-color: #161A1E;
                        border: 1px solid white;
                        border-radius: 15px;
                        color: white;
                    }

                    QMenu::item {
                        background-color: transparent;
                        padding: 10px 20px;
                        border-radius: 0px;
                    }

                    QMenu::item:selected {
                        background-color: #2C3236;
                        border-radius: 15px;
                    }
                """
        self.menu.setStyleSheet(menu_style)

    def showMenu(self):
        # Показываем меню относительно координат основной кнопки
        self.menu.popup(self.pushEnergy_Preset.mapToGlobal(self.pushEnergy_Preset.rect().bottomLeft()))

    def onButton1Clicked(self):
        Balance_Preset()
        print("Button 1 clicked")

    def onButton2Clicked(self):
        Hight_Performance_Preset()
        print("Button 2 clicked")

    def onButton3Clicked(self):
        PowerSaver_Preset()
        print("Button 3 clicked")

    def updateHibernationButton(self):
        state = check_hibernation_PC()
        self.pushHibernation.setText(state)
        if state == "on":
            self.setStyleForHibernationButton(True)
        else:
            self.setStyleForHibernationButton(False)

    def setStyleForHibernationButton(self, is_on):
        style = self.styleButtonHibernationOn() if is_on else self.styleButtonHibernationOff()
        self.pushHibernation.setStyleSheet(style)

    def hibernationButtonClicked(self):
        if self.pushHibernation.text() == "on":
            hibernation_PC_OFF()
        else:
            hibernation_PC_ON()
        self.updateHibernationButton()

    def styleButtonHibernationOn(self):
        return "QPushButton { color: red;background-color: #161A1E;border-radius: 15px;font-size: 11px;padding: 10px 20px;border: 1px solid white;} QPushButton:hover {background-color: #2C3236; transition: background-color 0.3s ease;}"

    def styleButtonHibernationOff(self):
        return "QPushButton { color: green;background-color: #161A1E;border-radius: 15px;font-size: 11px;padding: 10px 20px;border: 1px solid white;} QPushButton:hover {background-color: #2C3236; transition: background-color 0.3s ease;}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = EnergyWindows()
    energy_window.show()
    sys.exit(app.exec())
