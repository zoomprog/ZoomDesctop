from PyQt6.QtCore import Qt, QPropertyAnimation, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Profile")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.on_button_clicked)
        self.animation = None
        self.is_expanded = False

    def on_button_clicked(self):
        if self.animation and self.animation.state() == QPropertyAnimation.State.Running:
            return

        if not self.is_expanded:
            self.animation = QPropertyAnimation(self.button, b"minimumSize")
            self.animation.setDuration(300)
            self.animation.setStartValue(QSize(self.button.width(), 31))
            self.animation.setEndValue(QSize(self.button.width(), 172))
            self.animation.start()
            self.is_expanded = True
        else:
            self.animation = QPropertyAnimation(self.button, b"minimumSize")
            self.animation.setDuration(600)
            self.animation.setStartValue(QSize(self.button.width(), 172))
            self.animation.setEndValue(QSize(self.button.width(), 31))
            self.animation.start()

            self.is_expanded = False


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
