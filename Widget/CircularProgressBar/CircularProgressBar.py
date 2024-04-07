from PyQt6.QtWidgets import QWidget, QApplication
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
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Адаптация размеров для кругового прогрессбара под новый размер виджета
        rect = QRectF(5, 5, 70, 70)  # Адаптированный размер прямоугольника под 80x80 виджет
        startAngle = 90 * 16
        spanAngle = -360 * 16 * self.value / 100

        # Адаптация толщины пера
        pen = QPen()
        pen.setWidth(10)  # Увеличенная толщина пера
        pen.setColor(QColor(22, 26, 30))
        painter.setPen(pen)

        painter.drawArc(rect, startAngle, 360 * 16)
        pen.setColor(QColor(38, 160, 218))
        painter.setPen(pen)

        painter.drawArc(rect, startAngle, spanAngle)

        # Адаптация размера шрифта
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)  # Адаптированный размер шрифта
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))

        text = f"{self.value}%"
        textRect = QRectF(rect)
        painter.drawText(textRect, Qt.AlignmentFlag.AlignCenter, text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    progressBar = CircularProgressBar()
    progressBar.setValue(100)  # Пример установки значения
    progressBar.show()
    sys.exit(app.exec())