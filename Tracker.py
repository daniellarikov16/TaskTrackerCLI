import json
class Task:
    def __init__(self, id = 0, description='',status='',createdAT='',updatedAT=''):
        self.id = id
        self.description = description
        self.status = status
        self.createdAT = createdAT
        self.updatedAT = updatedAT
    def createTask(self):
        getter = vars(self)
        with open('data.json', 'w') as file:
            json.dump(getter,file)
        print("Данные успешно загружены в базу данных")

new_task = Task()
new_task.id = 1
new_task.description = 'Полить цветы'
new_task.createTask()