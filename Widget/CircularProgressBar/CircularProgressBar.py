from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtCore import Qt, QRectF
import sys

class CircularProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(80, 80)  # Установка фиксированного размера 80x80
        self.value = 0

    def setValue(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        # Отображаемый текст также адаптируется к максимуму в 76
        text = "{:.0f}%".format((self.value / 76) * 100)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = QRectF(5, 5, 70, 70)
        startAngle = 90 * 16
        # Используем 76 в качестве делителя для расчета spanAngle
        spanAngle = int(-360 * 16 * self.value / 76)

        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor(22, 26, 30))
        painter.setPen(pen)

        painter.drawArc(rect, startAngle, 360 * 16)
        if text <= '40':
            pen.setColor(QColor(255, 0, 0))
        elif text < '60':
            pen.setColor(QColor(255, 255, 0))
        elif text >= '60':
            pen.setColor(QColor(38, 160, 218))
        painter.setPen(pen)

        painter.drawArc(rect, startAngle, spanAngle)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))

        textRect = QRectF(rect)
        painter.drawText(textRect, Qt.AlignmentFlag.AlignCenter, text)

