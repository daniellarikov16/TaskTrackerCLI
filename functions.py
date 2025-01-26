import json
def get_data():
    try:
        with open('data.json', 'r') as file:
            all_tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
          print('ошибка: файл не найден или данные неверные')
          return
    return all_tasks
def update_description(id_task, text, upd_time):
    all_tasks = get_data()
    for task in all_tasks:
        if task['id'] == id_task:
            task['description'] = text
            task['updatedAT'] = upd_time
            break
    else:
        print(f'Задача с ID {id_task} не найдена.')
        return
    with open('data.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)
    print('Данные успешно обновлены в базе данных')

def update_status(id_task, status, upd_time):
    all_tasks = get_data()

    for task in all_tasks:
        if task['id'] == id_task:
            task['status'] = status
            task['updatedAT'] = upd_time
            break
    else:
        print(f'Задача с ID {id_task} не найдена.')
        return
    with open('data.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)
    print('Статус успешно обновлен в базе данных')
def delete_task(id_task):
    all_tasks = get_data()
    flag = False
    if id_task == len(all_tasks):
        flag = True
    all_tasks.pop(id_task-1)
    if not(flag):
        for task in all_tasks:
            if task['id'] > id_task:
                task['id'] -= 1
    with open('data.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)
    print('Запись успешно удалена из базы данны')

def get_all_task():
    all_tasks = get_data()
    for task in all_tasks:
        for key, value in task.items():
            print(f"{key}: {value}")
        print ('-'* 20)

def get_done_tasks():
    all_tasks = get_data()
    done_tasks = []
    for task in all_tasks:
        if task['status'] == 'Выполнено':
            done_tasks.append(task)
    if done_tasks:
        for done_task in done_tasks:
            for key, value in done_task.items():
                print(f"{key}: {value}")
            print('-' * 20)
    else:
        return 'Выполненных задач нет'
def get_in_progress_tasks():
    all_tasks = get_data()
    inprogress_tasks = []
    for task in all_tasks:
        if task['status'] == 'Выполняется':
            inprogress_tasks.append(task)
    if inprogress_tasks:
        for inprogress_task in inprogress_tasks:
            for key, value in inprogress_task.items():
                print(f"{key}: {value}")
            print('-' * 20)
    else:
        return 'Выполняемых задач нет'
def get_todo_tasks():
    all_tasks = get_data()
    todo_tasks = []
    for task in all_tasks:
        if task['status'] == 'Готова к выполнению':
            todo_tasks.append(task)
    if todo_tasks:
        for todo_task in todo_tasks:
            for key, value in todo_task.items():
                print(f"{key}: {value}")
            print('-' * 20)
    else:
        return 'Готовых к выполнению задач нет'

