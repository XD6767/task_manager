class Task:
    def __init__(self, name: str, priority: str, deadline: str):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def to_dict(self):
        return {
            'имя': self.name,
            'приоритет': self.priority,
            'дедлайн': self.deadline
        }