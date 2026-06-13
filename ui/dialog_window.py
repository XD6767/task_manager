from PySide6.QtWidgets import QDialog, QLineEdit, QComboBox, QDateEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QDate

class DialogWindow(QDialog):
    def __init__(self, parent=None, task=None):
        super().__init__()
        self.resize(300, 300)
        if task:
            self.setWindowTitle('редактирование задачи')
        else:
            self.setWindowTitle('добавление задачи')
        self.setWindowModality(Qt.WindowModality.WindowModal)

        control_elements_layout = QVBoxLayout()
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('название задачи')

        self.choice_priority = QComboBox()
        self.choice_priority.addItems(['высокий', 'средний', 'низкий'])

        self.choice_date = QDateEdit()
        self.choice_date.setDate(QDate.currentDate())
        self.choice_date.setCalendarPopup(True)

        name_label = QLabel('Название')
        priority_label = QLabel('Приоритет')
        date_label = QLabel('Дата')

        control_elements_layout.addWidget(name_label)
        control_elements_layout.addWidget(self.line_edit)
        control_elements_layout.addWidget(priority_label)
        control_elements_layout.addWidget(self.choice_priority)
        control_elements_layout.addWidget(date_label)
        control_elements_layout.addWidget(self.choice_date)

        if task:
            self.add_button = QPushButton('изменить')
            self.add_button.setStyleSheet(
            '''
            QPushButton {
                border: 2px solid #FFC681;
                background-color: #F7EBDC
            }

            '''
        )
        else:
            self.add_button = QPushButton('добавить')
        self.add_button.clicked.connect(self.accept, )
        self.add_button.setAutoDefault(False)
        self.add_button.setStyleSheet(
            '''
            QPushButton {
                border: 2px solid #9AFF99;
                background-color: #E0F9E0
            }

            '''
        )

        self.cancel_button = QPushButton('отмена')
        self.cancel_button.clicked.connect(self.reject)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setStyleSheet(
            '''
            QPushButton {
                border: 2px solid #FF9293;
                background-color: #F9D8D9
            }

            '''
        )

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.cancel_button)
        buttons_layout.addWidget(self.add_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(control_elements_layout)
        main_layout.addLayout(buttons_layout)

        if task:
            self.line_edit.setText(task.name)
            self.choice_priority.setCurrentText(task.priority)
            self.choice_date.setDate(QDate.fromString(task.deadline, 'dd-MM-yyyy'))

        self.setLayout(main_layout)

    def get_task(self):
        user_text = self.line_edit.text()
        user_priority = self.choice_priority.currentText()
        user_date = self.choice_date.date().toString('dd-MM-yyyy')
        return user_text, user_priority, user_date