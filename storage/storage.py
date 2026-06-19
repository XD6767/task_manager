import sqlite3
from models.task import Task

class Storage:
    def __init__(self, filename):
        self.filename = filename
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.filename) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    deadline TEXT NOT NULL
                )
            """)

            conn.commit()

    def load(self) -> list[Task]:
        with sqlite3.connect(self.filename) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id, name, priority, deadline
                FROM tasks
            """)

            rows = cursor.fetchall()

        return [
            Task(
                name=row[1],
                priority=row[2],
                deadline=row[3],
                id=row[0]
            )
            for row in rows
        ]

    def save(self, tasks: list[Task]):
        with sqlite3.connect(self.filename) as conn:
            cursor = conn.cursor()

            cursor.execute("DELETE FROM tasks")

            cursor.executemany(
                """
                INSERT INTO tasks (id, name, priority, deadline)
                VALUES (?, ?, ?, ?)
                """,
                [
                    (
                        task.id,
                        task.name,
                        task.priority,
                        task.deadline
                    )
                    for task in tasks
                ]
            )

            conn.commit()


# import json
# from models.task import Task

# class Storage:
#     def __init__(self, filename):
#         self.filename = filename

#     def load(self) -> list[Task]:
#         try:
#             with open(self.filename, 'r', encoding='utf-8') as file:
#                 data = json.load(file)
#                 return [Task.from_dict(dict) for dict in data]
#         except(FileNotFoundError, json.JSONDecodeError):
#             return []

#     def save(self, tasks: list[Task]):
#         with open(self.filename, 'w', encoding='utf-8') as file:
#             json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
