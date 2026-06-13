from PySide6.QtWidgets import QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QHeaderView, QAbstractItemView, QMessageBox
from storage.storage import Storage
from service.service import TaskService
from ui.dialog_window import DialogWindow
from ui.table_model import TableModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('Менеджер задач')

        self.filename = './task.json'
        self.storage = Storage(self.filename)
        self.service = TaskService(self.storage)
        self.model = TableModel(self.service)
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setStyleSheet('''
            QTableView::item:selected {
                color: #506CE0;
                background-color: #CCE2F2
            }
                                 
            '''          
        )
        

        self.search_element = QLineEdit()
        self.search_element.setPlaceholderText('Поиск')
        self.search_element.textChanged.connect(self.search_task)
        self.search_element.setStyleSheet('''
            QLineEdit {
                border: 2px solid #88DFF;
                background-color: #CCE2F2;
                color: #2A4FD6
            }

            '''
        )

        self.add_button = QPushButton('добавить задачу')
        self.add_button.clicked.connect(self.add_task)
        self.add_button.setStyleSheet(
            '''
            QPushButton {
                border: 2px solid #9AFF99;
                background-color: #E0F9E0;
                color: #266825
            }

            '''
        )
        
        self.delete_button = QPushButton('удалить задачу')
        self.delete_button.clicked.connect(self.delete_task)
        self.delete_button.setStyleSheet(
            '''
            QPushButton {
                border: 2px solid #FF9293;
                background-color: #F9D8D9;
                color: #68252E
            }

            '''
        )

        self.edit_button = QPushButton('редактировать задачу')
        self.edit_button.clicked.connect(self.edit_task)
        self.edit_button.setStyleSheet(
            '''
            QPushButton {
                border: 2px solid #FFC681;
                background-color: #F7EBDC;
                color: #873F00
            }

            '''
        )

        elements_control_wrapper = QVBoxLayout()
        elements_control_wrapper.addWidget(self.add_button)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.search_element)
        main_layout.addWidget(self.table)
        main_layout.addLayout(elements_control_wrapper)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)
        
    def add_task(self):
        dialog = DialogWindow(self)
        if dialog.exec():
            self.service.add_task(*dialog.get_task())
            self.model.refresh()

    def delete_task(self):
        try:
            current_row = self.table.selectionModel().selectedRows()
            row = current_row[0].row()
            task = self.model.tasks[row]

            is_remove = QMessageBox().question(self, 'Удаление задачи', f'Вы подтверждаете удаление задачи: {task.name}?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if is_remove == QMessageBox.Yes:
                self.service.remove_task(task.id)
                self.model.refresh()
        except:
            QMessageBox().warning(self, 'Ошибка', 'Выберите задачу')
            return
        
    def edit_task(self):
        current_row = self.table.selectionModel().selectedRows()
        row = current_row[0].row()
        task = self.model.tasks[row]
        dialog = DialogWindow(self, task)
        if dialog.exec():
            self.service.edit_task(*dialog.get_task(), task.id)
            self.model.refresh()

    def search_task(self, user_text):
        tasks = self.service.search_tasks(user_text)
        self.model.set_tasks(tasks)