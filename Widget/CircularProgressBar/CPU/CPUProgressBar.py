from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtCore import Qt, QRectF
import sys

class CircularProgressBarCPU(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(80, 80)  # Установка фиксированного размера 80x80
        self.value = 0

    def setValue(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        # Исправленный расчет процентного значения
        percentage = (self.value / 100) * 100  # Предполагаем, что максимальное значение - 100
        text = "{:.0f}%".format(percentage)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = QRectF(5, 5, 70, 70)
        startAngle = 90 * 16
        # Исправленный расчет spanAngle
        spanAngle = -360 * 16 * self.value / 100  # Предполагаем, что максимальное значение - 100

        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor(22, 26, 30))
        painter.setPen(pen)

        painter.drawArc(rect, startAngle, 360 * 16)

        # Исправленные условия для изменения цвета
        if percentage <= 40:
            pen.setColor(QColor(255, 0, 0))
        elif percentage <= 60:
            pen.setColor(QColor(255, 255, 0))
        else:
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

