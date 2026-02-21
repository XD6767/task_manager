from models.task import Task

class Ui:
    def __init__(self, service):
        self.service = service
    
    def run(self):
        while True:
            print('меню: ')
            print('1-добавить задачу')
            print('2-удалить задачу')
            print('3-редактировать задачу')
            print('4-поиск задач')
            print('5-список задач')
            print('0-выход')

            choice_user = input('введите номер задачи: ')
            if choice_user == '1':
                self.add_task()
            elif choice_user == '5':
                self.show_task()
            elif choice_user == '2':
                self.delete_task()
            elif choice_user == '4':
                self.search_task()
            elif choice_user == '3':
                self.edit_task()
            elif choice_user == '0':
                break

    def add_task(self):
        name = input('введите название задачи: ')
        priority = input('введите приоритет задачи: ')
        deadline = input('введите дедлайн: ')

        task = Task(name,priority,deadline)
        self.service.add_task(task)

        print(f'добавлена задача: {name}')

    def show_task(self):
        task_list = self.service.get_all_tasks()
        if len(task_list) > 0:
            for index, task in enumerate(task_list, start=1):
                print(f'{index}. Название: {task["name"]} | Приоритет: {task["priority"]} | Дедлайн: {task["deadline"]}')
        else:
            print('нет задач')

    def remove_task(self):
        self.show_task()
        task_number = int(input('введите номер задачи: '))-1
        is_note = self.service.remove_task(task_number)
        if is_note:
            print(f'была удалена задача: {is_note.name}')
        else:
            print('такой задачи нет')

    def edit_task(self):
        task_num = int(input('введите номер задачи: ')) - 1
        new_name = input('введите имя задачи: ')
        new_priority = input('введите приоритет задачи: ')
        new_deadline = input('введите дедлайн задачи: ')
        if self.service.edit_task(task_num, new_name, new_priority, new_deadline):
            print('задача успешно изменена')
        else:
            print('такой задачи нет')

    def search_tasks(self):
        print('поиск задачи')
        name = input('введите имя задачи: ').lower()
        notes = self.service.search_tasks(name)
        if notes:
            for index, task in enumerate(notes, start=1):
                print(f'{index}. Название: {task["name"]} | Приоритет: {task["priority"]} | Дедлайн: {task["deadline"]}')
        else:
            print('нет задач')