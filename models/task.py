class Task:
    def __init__(self, name: str, priority: str, deadline: str):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'priority': self.priority,
            'deadline': self.deadline
        }

    @staticmethod
    def from_dict(dict_task: dict) -> 'Task':
        return Task(
            name=dict_task['name'],
            priority=dict_task['priority'],
            deadline=dict_task['deadline']
        )

# task = Task('сьесть шоколадку', 'очень важно', 'сейчас')
# print(task)
# task = task.to_dict()
# task['name']='сьесть банан'
# print(task)
# new_object = Task.from_dict(task)
# print(new_object)