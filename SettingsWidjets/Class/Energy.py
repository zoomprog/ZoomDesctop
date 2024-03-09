import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QDialog, QApplication, QMenu
from SettingsWidjets.EnergyPower import Ui_Energy

from Functions.Energy.Preset.Balanced import Balance_Preset
from Functions.Energy.Preset.HightPerformance import Hight_Performance_Preset
from Functions.Energy.Preset.PowerSaver import PowerSaver_Preset


class EnergyWindows(QDialog, Ui_Energy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(1)
        self.pushEnergy_Preset.clicked.connect(self.showMenu)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    energy_window = EnergyWindows()
    energy_window.show()
    sys.exit(app.exec())
