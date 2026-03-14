from models.task import Task

class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self.tasks: list[Task] = self.storage.load()
        self._next_id = max((task.id for task in self.tasks), default=0)+1

    def increment_id(self):
        self._next_id+=1

    def add_task(self, name, priority, deadline):
        task = Task(name,priority,deadline,self._next_id)
        self.tasks.append(task)
        self.storage.save(self.tasks)
        self.increment_id()
        return task

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

    def search_tasks(self, name : str):
        found_notes = []
        for note in self.tasks:
            if name in note.name.lower():
                found_notes.append(note)
        return found_notes

    def get_all_tasks(self) -> list[Task]:
        return self.tasks