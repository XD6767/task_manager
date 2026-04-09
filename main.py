
from ui.window_view import MainWindow

import sys
from PySide6.QtWidgets import QMainWindow, QTableView, QApplication

def runner():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    runner()