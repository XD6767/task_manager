from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

class TableModel(QAbstractTableModel):
    def __init__(self, service):
        super().__init__()
        self._service = service
        self._titles = ('name', 'priority', 'deadline')

    def rowCount(self, parent=QModelIndex()):
        return len(self._service.get_all_tasks())
    
    def columnCount(self, parent=QModelIndex()):
        return len(self._titles)
    
    def headerData(self, index, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._titles[index]
        return None