import os
from datetime import datetime
from Task_class import *
if not os.path.exists('data.json'):
               with open('data.json', 'w') as file:
                    json.dump([], file)
while True:
    ans = int(input('Меню:\n 1 - Добавить задачу\n '
                    '2 - Обновить описание задачи\n '
                    '3 - Удалить задачу\n '
                    '4 - Изменить статус задачи ("Готова к выполнению", "Выполняется", "Выполнено")\n '
                    '5 - Перечислить задачи (Все, "Готовые к выполнению", "В процессе выполнения", "Выполненные"\n '
                    '0 - Завершить работу\n\n '
                    'Ваш выбор: '))
    if ans == 0:
        print('До свидания!')
        break
    elif ans == 1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        task_description = str(input('Введите описание задачи: '))
        new_task = Task(task_description, current_time)
        new_task.create_task()
    elif ans == 2:
        while True:
            try:
                id_update = int(input('Введите id задачи: '))
                break
            except ValueError:
                print('Ошибка: Вы ввели не целое число, попробуйте снова.')
        text = str(input('Введите новое описание задачи: '))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        update_description(id_update, text, current_time)
    elif ans == 3:
        while True:
            try:
                id_delete = int(input('Введите id задачи: '))
                break
            except ValueError:
                print('Ошибка: Вы ввели не целое число, попробуйте снова.')
        delete_task(id_delete)
    elif ans == 4:
        change_id = int(input('Введите номер задачи статус, которой хотите изменить: '))
        while True:
            try:
                change_ans = int(input('Какой статус хотите выбрать:\n '
                                       '1 - Готова к выполнению\n '
                                       '2 - Выполняется\n '
                                       '3 - Выполнено\n'
                                       'Ваш выбор: '))
                break
            except ValueError:
                print('Ошибка: Вы ввели не целое число, попробуйте снова.')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if change_ans == 1:
            update_status(change_id, 'Готова к выполнению', current_time)
        elif change_ans == 2:
            update_status(change_id, 'Выполняется', current_time)
        elif change_ans == 3:
            update_status(change_id, 'Выполнено', current_time)
        else:
            print('Вы ввели неправильную команду')
    elif ans == 5:
        while True:
            try:
                get_tasks_ans = int(input('Какие задачи желаете посмотреть:\n '
                                          '1 - Все задачи\n '
                                          '2 - Готова к выполнению\n '
                                          '3 - Выполняется\n '
                                          '4 - Выполнена\n '
                                          'Ваш выбор: '))
                break
            except ValueError:
                print('Ошибка: Вы ввели не целое число, попробуйте снова.')
        if get_tasks_ans == 1:
            get_all_task()
        elif get_tasks_ans == 2:
            get_todo_tasks()
        elif get_tasks_ans == 3:
            get_in_progress_tasks()
        elif get_tasks_ans == 4:
            get_done_tasks()
        else:
            print('Вы ввели неправильную команду.')
    else:
        print('Вы ввели неправильную команду.')