from PySide6.QtWidgets import QDialog, Qt, QLineEdit, QComboBox, QDateEdit, QDate, QPushButton

class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('добавление задачи')
        self.setWindowModality(Qt.WindowModality.WindowModal)
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('название задачи')

        self.choice_priority = QComboBox()
        self.choice_priority.addItems(['высокий', 'средний', 'низкий'])

        self.choice_date = QDateEdit()
        self.choice_date.setDate(QDate.currentDate())

        self.add_button = QPushButton('добавить')
        self.add_button.clicked.connect(self.on_accept)

        self.cancel_button = QPushButton('отмена')
        self.cancel_button.clicked.connect(self.reject)

        # 1. Найти информацию о QLabel 
        # 2. Создать Layoutы для полей и кнопок(отдельные)
        # 3. С помощью метода addWidget добавить кнопки и заголовки в layout