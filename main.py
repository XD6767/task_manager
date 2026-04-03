from storage.storage import Storage
from service.service import TaskService
from ui.table_model import TableModel

import sys
from Pyside6.QtWidgets import QMainWindow, QTableView, QApplication
filename = './task.json'

def runner():
    app = QApplication([])
    storage = Storage(filename)
    service = TaskService(storage)

    window = QMainWindow()
    table = QTableView()
    model = TableModel(service)
    table.setModel(model)
    
    window.setCentralWidget(table)
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    runner()