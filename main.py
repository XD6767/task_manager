from storage.storage import Storage
from service.service import TaskService
from ui.ui import Ui
filename = './task.json'

def runner():
    storage = Storage(filename)
    service = TaskService(storage)
    ui = Ui(service)
    ui.run()

if __name__ == '__main__':
    runner()