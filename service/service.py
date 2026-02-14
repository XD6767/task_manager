from models.task import Task

class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self.tasks: list[Task] = self.storage.load()

    def add_task(self, object_task):
        self.tasks.append(object_task)
        self.storage.save(self.tasks)

    def remove_task(self, index: int):
        if index >= 0 and index < len(self.tasks):
            return self.tasks.pop(index)
        return False
