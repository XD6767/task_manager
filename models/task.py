class Task:
    def __init__(self, name: str, priority: str, deadline: str, id: int):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.id = id

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'priority': self.priority,
            'deadline': self.deadline,
            'id': self.id
        }

    @staticmethod
    def from_dict(dict_task: dict) -> 'Task':
        return Task(
            name=dict_task['name'],
            priority=dict_task['priority'],
            deadline=dict_task['deadline'],
            id=dict_task['id']
        )

