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
    
    def edit_task(self, index, new_name, new_priority, new_deadline):
        if index >= 0 and index < len(self.tasks):
            task = self.tasks[index]
            if new_name:
                task.name = new_name
            if new_priority:
                task.priority = new_priority
            if new_deadline:
                task.deadline = new_deadline
            self.storage.save(self.tasks)
            return True
        return False
    
    def get_all_tasks(self) -> list[Task]:
        return self.tasks