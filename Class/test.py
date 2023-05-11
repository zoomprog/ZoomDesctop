from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

app = QApplication([])

# Создаем виджет-контейнер
widget = QWidget()

# Создаем чекбокс
checkbox = QCheckBox("Мой чекбокс")

# Устанавливаем стили из CSS
checkbox.setStyleSheet("""
    QCheckBox {
        /* Устанавливаем базовые параметры переключателя */
        padding: 0;
        background: none;
        border: none;
        outline: none;
        /* Размер переключателя */
        width: 30px;
        height: 20px;
        /* Устанавливаем форму переключателя в виде овала */
        border-radius: 10px;
        /* Устанавливаем фон для переключателя */
        background-color: rgb(119, 122, 126);
        /* Устанавливаем отступ для индикатора */
        margin-right: 10px;
    }
    QCheckBox::indicator {
        /* Устанавливаем размер и форму индикатора в виде круга */
        width: 16px;
        height: 16px;
        border-radius: 8px;
        /* Устанавливаем цвет индикатора */
        background-color: rgb(255, 0, 0) ;
        color: rgb(255, 0, 0);
        /* Устанавливаем границу для индикатора */
        border: 1px solid  rgb(119, 122, 126);
        /* Устанавливаем отступ для индикатора внутри переключателя */
        margin: 2px;
        /* Добавляем плавный переход при изменении состояния чекбокса */
        transition: transform 2s ease-out;
    }
    QCheckBox::indicator:checked {
        /* Смещаем индикатор на 30% вправо при нажатии на чекбокс */
        position: relative;
        left:30%;
        background-color: #7FFF00;    
    }
    QCheckBox::indicator:pressed {
        /* Добавляем эффект нажатия на индикатор */
        background-color: rgb(204, 204, 204);
    }
""")

# Создаем лейаут и добавляем в него чекбокс
layout = QVBoxLayout()
layout.addWidget(checkbox)

# Устанавливаем лейаут для виджета-контейнера
widget.setLayout(layout)

# Отображаем виджет
widget.show()

app.exec()