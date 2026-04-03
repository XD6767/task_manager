from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

class TableModel(QAbstractTableModel):
    def __init__(self, service):
        super().__init__()
        self._service = service
        self._titles = ('name', 'priority', 'deadline')
        self.tasks = self._service.get_all_tasks()

    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self._titles)
    
    def headerData(self, index, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._titles[index]
        return None
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            task = self.tasks[index.row()]
            column = index.column()
            if column == 0:
                return task.name
            elif column == 1:
                return task.priority
            elif column == 2:
                return task.deadline
        return None
    
    def refresh(self):
        self.beginResetModel()
        self.tasks = self._service.get_all_tasks()
        self.endResetModel()