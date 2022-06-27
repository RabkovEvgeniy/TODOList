def create_task(tasks: list, task_description: str):
    tasks.append(task_description)
    

def show_create_menu(tasks: list):
    task_description = input("Введите описание задачи:\n")
    print()
    create_task(tasks, task_description)


def show_delete_menu(tasks: list):
    print("введите номер задачи для удаления: ")
    for index in range(len(tasks)):
        print(f"{index} {tasks[index]}")
    index= int(input("введите номер задачи, которую вы хотите удалить"))
    if index > len(tasks) or index < 0:
        print("Введите номер сущетсвующей задачи")
        return 
    delete_task(tasks , index)


def delete_task (tasks: list, index: int):
    tasks.pop(index)



def show_all(tasks: list):
    print("Все задачи: ")
    for index in range(len(tasks)):
        print(f"{index} {tasks[index]}")
    input("Нажмите Enter:\n")
    


def close_app(tasks: list):
    exit()


def show_start_menu(tasks: list):
    print("Введите номер действия:")
    print("1 Cоздать задачу")
    print("2 Удалить задачу")
    print("3 Вывести все задачи")
    print("4 Выйти из приложения")
    action_number = input("Номер действия: ")
    print()
    
    if action_number == "1":
        show_create_menu(tasks)
    elif action_number == "2":
        show_delete_menu(tasks)
    elif action_number == "3":
        show_all(tasks)
    elif action_number == "4":
        close_app(tasks)
    else:
        print("По человечески же написанно от 1 до 4!!!")
        input("Нажмите Enter:\n")
    
    
def main():
    tasks = []
    while True:
        show_start_menu(tasks)


main()