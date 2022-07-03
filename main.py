import json


DATA_PATH = "Data.json"
LIST_TASKS_PROP = "tasks"
LIST_NAME_PROP = "name"


def main():
    lists = start_app()
    while True:
        show_start_menu(lists)


def start_app():
    lists = []
    with open(DATA_PATH, "r", encoding ="utf-8") as data_file:
        lists = json.load(data_file)
        
    return lists


def show_start_menu(lists: list):
    print("Введите номер действия:")
    print("1 Cоздать список")
    print("2 Удалить список")
    print("3 Вывести все списки")
    print("4 Открыть список")
    print("5 Выйти из приложения")
    action_number = input("Номер действия: ")
    print()
    
    try:
        if action_number == "1":
            show_list_create_menu(lists)
            return
        if action_number == "2":
            show_list_delete_menu(lists)
            return
        if action_number == "3":
            show_all_lists(lists)
            return 
        if action_number == "4":
            show_open_list_menu(lists)
            return
    except:
        print("Что-то пошло не так!\n")
        return
        
    if action_number == "5":
        close_app(lists)
         
    input("По человечески же написанно от 1 до 5!!! (Нажмите Enter для выхода:)\n")


def show_list_create_menu(lists: list):
    list_name = input("Введите название списка:\n")
    print()
    create_list(lists, list_name)


def create_list(lists: list, list_name:str):
    task_list = {
        LIST_NAME_PROP: list_name,
        LIST_TASKS_PROP: []
    }
    lists.append(task_list)


def show_list_delete_menu(lists:list):
    print("Введите номер задачи для удаления: ")
    for index in range(len(lists)):
        print(f"{index} {lists[index][LIST_NAME_PROP]}")
    print(f"{len(lists)} Назад")
    
    index = int(input("Номер задачи: "))
    if index == len(lists):
        print()
        return
    delete_list(lists , index)
    print()


def delete_list(lists: list, index:int):
    if index < 0:
        raise Exception("Индекс не должен быть отрицательным")
    lists.pop(index)


def show_all_lists(lists: list):
    if len(lists) == 0:
        print("Списков нет!\n")
        return
    print("Все списки (нажмите Enter для выхода): ")
    for task_list in lists:
        print(f"- {task_list[LIST_NAME_PROP]}")
    input("")


def show_open_list_menu(lists:list):
    print("Введите номер списка, который нужно открыть: ")
    for index in range(len(lists)):
        print(f"{index} {lists[index][LIST_NAME_PROP]}")
    print(f"{len(lists)} Назад")
    
    index = int(input("Номер списка: "))
    if index == len(lists):
        print()
        return
    
    if index < 0 or index > len(lists):
        print ("Списка с таким номером нет!")
        return
    print()
    show_list_menu(lists[index])


def show_list_menu(list: dict):
    while True:
        print("Введите номер действия:")
        print("1 Cоздать задачу")
        print("2 Удалить задачу")
        print("3 Вывести все задачи")
        print("4 Назад")
        action_number = input("Номер действия: ")
        print()
        
        try:
            if action_number == "1":
                show_task_create_menu(list[LIST_TASKS_PROP])
                continue
            if action_number == "2":
                show_task_delete_menu(list[LIST_TASKS_PROP])
                continue
            if action_number == "3":
                show_all_tasks(list[LIST_TASKS_PROP])
                continue 
        except:
            print("Что-то пошло не так!\n")
            continue
            
        if action_number == "4":
            break
            
        input("По человечески же написанно от 1 до 4!!! (Нажмите Enter для выхода:)\n")


def show_task_create_menu(tasks: list):
    task_description = input("Введите описание задачи:\n")
    print()
    create_task(tasks, task_description)


def create_task(tasks: list, task_description: str):
    tasks.append(task_description)
    

def show_task_delete_menu(tasks: list):
    print("Введите номер задачи для удаления: ")
    for index in range(len(tasks)):
        print(f"{index} {tasks[index]}")
    print(f"{len(tasks)} Назад")
    
    index = int(input("Номер задачи: "))
    if index == len(tasks):
        print()
        return
    delete_task(tasks , index)
    print()


def delete_task (tasks: list, index: int):
    if index < 0:
        raise Exception("Индекс не должен быть отрицательным")
    tasks.pop(index)


def show_all_tasks(tasks: list):
    if len(tasks) == 0:
        print("Задач нет!\n")
        return
    print("Все задачи (нажмите Enter для выхода): ")
    for task in tasks:
        print(f"- {task}")
    input("")
    

def close_app(tasks: list):
    with open(DATA_PATH, "w", encoding ="utf-8") as data_file:
        json.dump(tasks, data_file, )
    exit(0)


main()