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

    def remove_task(self, id: int):
        task = self.get_task(id)
        if task:
            self.tasks.remove(task)
            self.storage.save(self.tasks)
            return True
        return False

    def edit_task(self, new_name: str, new_priority: str, new_deadline: str, id: int):
        task = self.get_task(id)
        if task:
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
    
    def get_task(self, id):
        for task in self.tasks:
            if id == task.id:
                return task
        return None