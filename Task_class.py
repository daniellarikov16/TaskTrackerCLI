from functions import *

class Task:
    def __init__(self, description='',createdAT=''):
        self.id = Task.get_id(self)
        self.description = description
        self.status = 'Готова к выполнению'
        self.createdAT = createdAT
        self.updatedAT = '-'

    def get_id(self):
        items = get_data()
        if not items:
            return 1
        max_id = max(item['id'] for item in items)
        return max_id + 1

    def create_task(self):
        all_tasks = get_data()
        all_tasks.append(self.__dict__)
        with open('data.json', 'w') as file:
            json.dump(all_tasks, file, indent=4)
        print('Данные успешно загружены в базу данных')