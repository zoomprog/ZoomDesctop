from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class CustomMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 300)
        self.upbar = QWidget(self)
        self.upbar.setFixedSize(400, 50)
        self.upbar.move(0, 0)
        self.upbar.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.upbar.underMouse():
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'offset') and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.offset)


if __name__ == '__main__':
    app = QApplication([])
    window = CustomMainWindow()
    window.show()
    app.exec()