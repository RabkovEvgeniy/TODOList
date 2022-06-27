def create_task(tasks: list, task_description: str):
    tasks.append(task_description)
    

def show_create_menu(tasks: list):
    task_description = input("Введите описание задачи:\n")
    print()
    create_task(tasks, task_description)


def show_delete_menu(tasks: list):
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


def show_all(tasks: list):
    print("Все задачи (нажмите Enter для выхода): ")
    for index in range(len(tasks)):
        print(f"{index} {tasks[index]}")
    input("\n")
    

def close_app(tasks: list):
    exit(0)


def show_start_menu(tasks: list):
    print("Введите номер действия:")
    print("1 Cоздать задачу")
    print("2 Удалить задачу")
    print("3 Вывести все задачи")
    print("4 Выйти из приложения")
    action_number = input("Номер действия: ")
    print()
    
    try:
        if action_number == "1":
            show_create_menu(tasks)
            return
        if action_number == "2":
            show_delete_menu(tasks)
            return
        if action_number == "3":
            show_all(tasks)
            return 
    except:
        print("Что-то пошло не так!\n")
        return
        
    if action_number == "4":
        close_app(tasks)
         
    input("По человечески же написанно от 1 до 4!!! (Нажмите Enter для выхода:)\n")
    
    
def main():
    tasks = []
    while True:
        show_start_menu(tasks)


main()