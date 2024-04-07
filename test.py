import sys
import shutil
import os
import psutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtCore import QRect, Qt, QPoint

class DiskUsageWidget(QWidget):
    def __init__(self, disk_label):
        super().__init__()
        self.disk_label = disk_label  # Надпись диска
        self.disk_usage = self.get_disk_usage()
        self.setWindowTitle(f"Disk Usage for {disk_label}")
        self.setGeometry(100, 100, 300, 50)

    def get_disk_usage(self):
        # Получаем информацию о использовании диска
        total, used, free = shutil.disk_usage(f"{self.disk_label}/")
        return (used / total) * 100

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Рисуем надпись диска
        painter.setPen(QColor("red"))
        disk_label_font_size = 14
        painter.setFont(QFont("Arial", disk_label_font_size))
        painter.drawText(QRect(10, 10, 50, 30), Qt.AlignmentFlag.AlignLeft, self.disk_label + ":")

        # Рисуем серую линию (100%)
        painter.setPen(QPen(QColor("#E6E6E6"), 10))
        painter.drawLine(QPoint(60, 25), QPoint(280, 25))

        # Рисуем синюю линию (использование диска)
        painter.setPen(QPen(QColor("#26A0DA"), 10))
        usage_length = 220 * (self.disk_usage / 100)  # Длина синей линии в зависимости от использования
        painter.drawLine(QPoint(60, 25), QPoint(60 + usage_length, 25))

        # Добавляем текст с процентом использования
        usage_label_font_size = 10
        painter.setFont(QFont("Arial", usage_label_font_size))
        painter.setPen(QColor("#26A0DA"))
        painter.drawText(QRect(60, 30, 220, 20), Qt.AlignmentFlag.AlignRight, f"{self.disk_usage:.2f}%")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Disk Usage for All Drives")
        self.setGeometry(100, 100, 320, 200)
        layout = QVBoxLayout(self)

        # Определение доступных дисков и создание виджетов для каждого
        for disk in self.get_available_disks():
            disk_widget = DiskUsageWidget(disk)
            layout.addWidget(disk_widget)

    def get_available_disks(self):
        # Получаем список всех дисков
        disks = []
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':  # Для Windows
                if 'fixed' in part.opts or 'removable' in part.opts:
                    disks.append(part.device.rstrip('\\'))
        return disks

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())