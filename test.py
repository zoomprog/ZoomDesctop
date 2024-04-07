import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtCore import Qt, QRectF, QRect

class CircularProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 200)
        self.value = 0

    def setValue(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Определение размеров для кругового прогрессбара
        rect = QRectF(10, 10, self.width() - 20, self.height() - 20)
        startAngle = 90 * 16  # Начальный угол в 1/16 градуса
        spanAngle = -360 * 16 * self.value / 100  # Длина дуги в 1/16 градуса

        # Настройка пера для рисования контура
        pen = QPen()
        pen.setWidth(15)
        pen.setColor(Qt.GlobalColor.black)
        painter.setPen(pen)

        # Рисование контура кругового прогрессбара
        painter.drawArc(rect, startAngle, 360 * 16)

        # Настройка пера для рисования заполнения
        pen.setColor(Qt.GlobalColor.green)
        painter.setPen(pen)

        # Рисование заполнения кругового прогрессбара
        painter.drawArc(rect, startAngle, spanAngle)

        # Настройка шрифта для текста
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(48)  # Изменение размера шрифта на 24
        painter.setFont(font)
        painter.setPen(QColor(0, 0, 0))

        # Расчет позиции текста
        text = f"{self.value}%"
        textRect = QRectF(rect)
        painter.drawText(textRect, Qt.AlignmentFlag.AlignCenter, text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircularProgressBar()
    window.setValue(75)  # Установка значения прогресса
    window.show()
    sys.exit(app.exec())