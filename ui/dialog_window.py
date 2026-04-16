from PySide6.QtWidgets import QDialog, Qt, QLineEdit

class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('добавление задачи')
        self.setWindowModality(Qt.WindowModality.WindowModal)
        
        line_edit = QLineEdit
        line_edit.setPlaceholderText('название задачи')