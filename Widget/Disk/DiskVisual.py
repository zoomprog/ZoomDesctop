import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtCore import QRect, Qt, QPoint

class DiskUsageWidget(QWidget):
    def __init__(self, disk_label):
        super().__init__()
        self.disk_label = disk_label  # Надпись диска
        self.total_gb, self.used_gb, self.free_gb = self.get_disk_usage()
        self.setWindowTitle(f"Disk Usage for {disk_label}")
        self.setGeometry(100, 100, 400, 100)  # Увеличил высоту, чтобы было место для текста

    def get_disk_usage(self):
        # Получаем информацию о использовании диска в ГБ
        total, used, free = shutil.disk_usage(f"{self.disk_label}/")
        total_gb = total / (1024**3)
        used_gb = used / (1024**3)
        free_gb = free / (1024**3)
        return total_gb, used_gb, free_gb

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Рисуем надпись диска
        painter.setPen(QColor("white"))
        disk_label_font_size = 12
        painter.setFont(QFont("Arial", disk_label_font_size))
        painter.drawText(QRect(60, 0, 300, 30), Qt.AlignmentFlag.AlignLeft, self.disk_label)

        # Рисуем серую линию (100%)
        painter.setPen(QPen(QColor("#E6E6E6"), 10))
        painter.drawLine(QPoint(60, 25), QPoint(280, 25))

        # Рисуем синюю линию (использование диска)
        painter.setPen(QPen(QColor("#26A0DA"), 10))
        usage_length = 220 * (self.used_gb / self.total_gb)
        painter.drawLine(QPoint(60, 25), QPoint(60 + usage_length, 25))

        # Добавляем текст с использованием диска в ГБ после полосы
        usage_label_font_size = 10
        painter.setFont(QFont("Arial", usage_label_font_size))
        painter.setPen(QColor("#26A0DA"))
        text = f"{self.used_gb:.2f} GB из {self.total_gb:.2f} GB"
        text_width = painter.fontMetrics().horizontalAdvance(text)

        # Вычисляем центральную точку виджета для горизонтального позиционирования текста
        center_point = self.width() / 2

        # Позиционируем текст так, чтобы его центр совпадал с центром виджета
        painter.drawText(QRect(center_point - text_width / 2-13, 30, text_width, 20), Qt.AlignmentFlag.AlignCenter, text)