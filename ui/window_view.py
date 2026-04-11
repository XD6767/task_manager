from PySide6.QtWidgets import QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget
from storage.storage import Storage
from service.service import TaskService
from ui.table_model import TableModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 800)
        self.setWindowTitle('task manager')

        self.filename = './task.json'
        self.storage = Storage(self.filename)
        self.service = TaskService(self.storage)
        self.model = TableModel(self.service)
        self.table = QTableView()
        self.table.setModel(self.model)

        self.add_button = QPushButton('йцукенгшщз')
        self.add_button.clicked.connect(self.add_task)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)
        
    # создать метод add_task 
    # метод вызывает добавление задачи из сервиса(не забудь передать аргументы)
    # вызвать обновление модели таблицы

    # найти информацию про QVBoxLayout(как работает, зачем нужен)

    def add_task(self):
        self.service.add_task('name', 'priority', 'deadline')
        self.model.refresh()