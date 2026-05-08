from PySide6.QtWidgets import QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget
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

        self.add_button = QPushButton('добавить задачу')
        self.add_button.clicked.connect(self.add_task)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)
        
    def add_task(self):
        # self.service.add_task('name', 'priority', 'deadline')
        # self.model.refresh()
        dialog = DialogWindow(self)
        if dialog.exec():
            self.service.add_task(*dialog.get_task())
            self.model.refresh()