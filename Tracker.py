import json
class Task:
    def __init__(self, id = 0, description='',status='',createdAT='',updatedAT=''):
        self.id = id
        self.description = description
        self.status = status
        self.createdAT = createdAT
        self.updatedAT = updatedAT
    def createTask(self):
        all_tasks = {'tasks': []}
        with open('data.json', 'r') as file:
            data = json.load(file)
        all_tasks['tasks'].extend(data['tasks'])
        all_tasks['tasks'].append(self.__dict__)
        with open('data.json', 'w') as file:
            json.dump(all_tasks, file, indent=4)  # Записываем весь словарь (все задачи) в файл
        print("Данные успешно загружены в базу данных")
new_task = Task()
new_task.id = 2
new_task.description = 'Полоть цветы'
new_task.createTask()
