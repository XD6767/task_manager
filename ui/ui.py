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