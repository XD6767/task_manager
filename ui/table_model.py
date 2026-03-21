from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

class TableModel(QAbstractTableModel):
    def __init__(self, service):
        super().__init__()
        self._service = service
        self._titles = ('name', 'priority', 'deadline')