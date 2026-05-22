from PySide6.QtWidgets import QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QHeaderView, QAbstractItemView
from storage.storage import Storage
from service.service import TaskService
from ui.dialog_window import DialogWindow
from ui.table_model import TableModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('task manager')

        self.filename = './task.json'
        self.storage = Storage(self.filename)
        self.service = TaskService(self.storage)
        self.model = TableModel(self.service)
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.search_element = QLineEdit()
        self.search_element.setPlaceholderText('Поиск')

        self.add_button = QPushButton('добавить задачу')
        self.add_button.clicked.connect(self.add_task)

        self.delete_button = QPushButton('удалить задачу')
        self.delete_button.clicked.connect(self.delete_task)


        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.search_element)
        main_layout.addWidget(self.table)
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
        current_row = self.table.selectionModel().selectedRows()
        row = current_row[0].row()
        task = self.model.tasks[row]
        self.service.remove_task(task.id)
        self.model.refresh()
