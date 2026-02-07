import json
from models.task import Task

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load(self) -> list[Task]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Task.from_dict(data) for i in data]
        except(FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, tasks: list[Task]):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
