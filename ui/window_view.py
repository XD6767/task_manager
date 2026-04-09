from PySide6.QtWidgets import QMainWindow, QTableView
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
        self.setCentralWidget(self.table)
        