from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QPen, QFont, QColor, QPixmap
from PyQt6.QtCore import QRect, Qt, QPoint, QSize
import shutil

class DiskUsageWidget(QWidget):
    def __init__(self, disk_label):
        super().__init__()
        self.disk_label = disk_label  # Надпись диска
        self.total_gb, self.used_gb, self.free_gb = self.get_disk_usage()
        self.setWindowTitle(f"Disk Usage for {disk_label}")
        self.setGeometry(100, 100, 400, 120)  # Увеличил высоту, чтобы было место для текста и бортиков
        self.image = QPixmap("image/Widget/icons8-disk-usage-48.png")

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
        painter.drawPixmap(QPoint(10, 30), self.image)
        # Рисуем надпись диска
        painter.setPen(QColor("white"))
        disk_label_font_size = 12
        painter.setFont(QFont("Arial", disk_label_font_size))
        painter.drawText(QRect(70, 20, 300, 30), Qt.AlignmentFlag.AlignLeft, self.disk_label)

        # Рисуем серый фоновый прямоугольник (100%)
        painter.setBrush(QColor("#E6E6E6"))  # Задаем цвет заливки
        painter.setPen(Qt.PenStyle.NoPen)  # Убираем контур
        painter.drawRoundedRect(QRect(60, 40, 220, 20), 10, 10)  # Рисуем прямоугольник с закругленными углами

        # Рисуем синий прямоугольник (использование диска)
        usage_length = 220 * (self.used_gb / self.total_gb)
        painter.setBrush(QColor("#26A0DA"))  # Задаем цвет заливки
        painter.drawRoundedRect(QRect(60, 40, int(usage_length), 20), 10, 10)  # Рисуем прямоугольник с закругленными углами

        # Добавляем текст с использованием диска в ГБ после полосы
        usage_label_font_size = 12
        painter.setFont(QFont("Arial", usage_label_font_size))
        painter.setPen(QColor("#26A0DA"))
        text = f"{self.used_gb:.2f} GB из {self.total_gb:.2f} GB"
        text_width = painter.fontMetrics().horizontalAdvance(text)
        center_point = self.width() / 2
        painter.drawText(QRect(center_point - text_width / 2 - 20, 65, text_width, 20), Qt.AlignmentFlag.AlignCenter, text)
