import json
from models.task import Task

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load(self) -> list[Task]:
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # добавить обработку ошибок при попытке открытия файла, если файл не найден или битый возвращать пустой список
            return [Task.from_dict(data) for i in data]