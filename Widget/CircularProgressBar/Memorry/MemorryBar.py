from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtCore import Qt, QRectF
import sys
import psutil  # Для получения информации об оперативной памяти

class CircularProgressMemorryBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(80, 80)  # Установка фиксированного размера 80x80
        self.value = 0
        self.total_memory = psutil.virtual_memory().total / (1024**3)  # Общий объем ОЗУ в ГБ
        self.used_memory = 0  # Используемая память, будет установлена позже

    def setValue(self, used_memory_gb):
        self.used_memory = used_memory_gb
        self.value = (self.used_memory / self.total_memory) * 100  # Процент использования
        self.repaint()

    def paintEvent(self, event):
        # Пересчет используемой памяти в мегабайты
        used_memory_mb = self.used_memory * 1024  # Перевод из ГБ в МБ
        text = "{:.0f} MB".format(used_memory_mb)  # Текст для отображения в мегабайтах

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = QRectF(5, 5, 70, 70)
        startAngle = 90 * 16
        spanAngle = int(-360 * 16 * self.value / 100)  # Расчет угла на основе процента использования

        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor(22, 26, 30))
        painter.setPen(pen)

        painter.drawArc(rect, startAngle, 360 * 16)
        if self.value <= 40:
            pen.setColor(QColor(255, 0, 0))
        elif self.value < 60:
            pen.setColor(QColor(255, 255, 0))
        else:
            pen.setColor(QColor(38, 160, 218))
        painter.setPen(pen)

        painter.drawArc(rect, startAngle, spanAngle)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))

        textRect = QRectF(rect)
        painter.drawText(textRect, Qt.AlignmentFlag.AlignCenter, text)

