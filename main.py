import json

def load_tasks():
    with open('./task.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    task_list = load_tasks()
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
            add_task(task_list)
        elif choice_user == '5':
            show_task(task_list)
        elif choice_user == '2':
            delete_task(task_list)
        elif choice_user == '4':
            search_task(task_list)
        elif choice_user == '3':
            edit_task(task_list)
        elif choice_user == '0':
            break

def add_task(task_list):
    name = input('введите название задачи: ')
    priority = input('введите приоритет задачи: ')
    deadline = input('введите дедлайн: ')

    data_of_task = {
        "имя": name,
        "приоритет": priority,
        "дедлайн": deadline
    }
    task_list.append(data_of_task)
    save_tasks(task_list)

def save_tasks(task_list):
    with open('./task.json', 'w', encoding='utf-8') as file:
        json.dump(task_list, file, ensure_ascii=False)

def show_task(task_list):
    if len(task_list) > 0:
        for index, task in enumerate(task_list, start=1):
            print(f'{index}. Название: {task["имя"]} | Приоритет: {task["приоритет"]} | Дедлайн: {task["дедлайн"]}')
    else:
        print('нет задач')

def delete_task(task_list):
    show_task(task_list)
    task_number = int(input('введите номер задачи: '))-1
    if task_number >= 0 and task_number < len(task_list):
        task_pop = task_list.pop(task_number)
        show_task(task_list)
        save_tasks(task_list)
        print(f'была удалена задача: {task_pop["имя"]}')
    else:
        print('такой задачи нет')

def search_task(task_list):
    print('поиск задачи')
    key_word = input('введите имя задачи: ').lower()
    founded_list = []
    for task in task_list:
        if key_word in task["имя"].lower():
            founded_list.append(task)
    show_task(founded_list)

def edit_task(task_list):
    show_task(task_list)
    task_num = int(input('введите номер задачи: ')) - 1
    if task_num >= 0 and task_num < len(task_list):
        new_name = input('введите имя задачи: ')
        new_priority = input('введите приоритет задачи: ')
        new_deadline = input('введите дедлайн задачи: ')
        data_task = {
            "имя": new_name,
            "приоритет": new_priority,
            "дедлайн": new_deadline
        }
        task_list[task_num] = data_task
        save_tasks(task_list)
main()