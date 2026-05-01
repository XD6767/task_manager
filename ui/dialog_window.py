from PySide6.QtWidgets import QDialog, QLineEdit, QComboBox, QDateEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt, QDate

class DialogWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('добавление задачи')
        self.setWindowModality(Qt.WindowModality.WindowModal)

        control_elements_layout = QVBoxLayout()
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('название задачи')

        self.choice_priority = QComboBox()
        self.choice_priority.addItems(['высокий', 'средний', 'низкий'])

        self.choice_date = QDateEdit()
        self.choice_date.setDate(QDate.currentDate())

        control_elements_layout.addWidget(self.line_edit)
        control_elements_layout.addWidget(self.choice_priority)
        control_elements_layout.addWidget(self.choice_date)

        self.add_button = QPushButton('добавить')
        self.add_button.clicked.connect(self.accept)

        self.cancel_button = QPushButton('отмена')
        self.cancel_button.clicked.connect(self.reject)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(control_elements_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

        # def on_accept()

        # 1. Найти информацию о QLabel 
        # 2. Создать Layoutы для полей и кнопок(отдельные)
        # 3. С помощью метода addWidget добавить кнопки и заголовки в layout