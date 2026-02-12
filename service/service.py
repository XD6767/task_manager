from models.task import Task

class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self.tasks: list[Task] = self.storage.load()