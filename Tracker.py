import json
from datetime import datetime
class Task:
    def __init__(self, description='',status='',createdAT='',updatedAT=''):
        self.id = Task.get_id(self)
        self.description = description
        self.status = status
        self.createdAT = createdAT
        self.updatedAT = updatedAT
    def get_id(self):
        with open ('data.json', 'r') as file:
            data = json.load(file)
            items = data.get('tasks', [])
        if not items:
            return 1
        max_id = max(item['id'] for item in items)
        return max_id + 1
    def createTask(self):
        all_tasks = {'tasks': []}
        with open('data.json', 'r') as file:
            data = json.load(file)
        all_tasks['tasks'].extend(data['tasks'])
        all_tasks['tasks'].append(self.__dict__)
        with open('data.json', 'w') as file:
            json.dump(all_tasks, file, indent=4)
        print("Данные успешно загружены в базу данных")
def get_all_task():
    with open('data.json', 'r') as file:
        data = json.load(file)
        items = data.get('tasks', [])
    return items
now = datetime.now()
ans = int(input())

while ans != 0:
    current_time = now.strftime("%H:%M:%S")
    new_task = Task('Полоть цветы', 'Выполняется', current_time)
    current_time = now.strftime("%H:%M:%S")
    new_task.createTask()
    ans = int(input())
print(get_all_task())
