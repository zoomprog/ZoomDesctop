from main import *


def RemoveWindowsMenu(self):
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
