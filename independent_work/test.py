# показывает что в списке
def full_tasks():
    for i in task_list:
                print(i)
# удалеет то что напишет юзер
def delete_tasks():
    delete =input('Что нужно удалить? : ')
    task_list.remove(delete)
# добавляет то что напишет юзер
def add_task():
    task_new= input('Уведите задачу :')
    task_list.append(task_new) 
# создает (если не) , через фор перебирает наш список и вписывает то что в списке в файл
def save_tasks():
    with open('task_list.txt', 'w', encoding='utf-8') as file:
        for i in task_list:
               file.write(i+'\n')
# открывает файл перебирает что есть в файле и вписывает в список то что в файле                
def read_file():
    try:
        with open('task_list.txt', 'r', encoding='utf-8') as file:
            for i in file:
              task_list.append(i.strip())          
    except FileNotFoundError:
        pass
task_list=[]
read_file()
while True:
    try:
        task = input('Уведите 1(Добавить),2 (Показать), 3 (Удалить), 4 (Остановить програму ) ')

        if task == '2':
            full_tasks()
        elif task == '1':
            add_task()
            save_tasks()
        elif task == '3':
            delete_tasks()
            save_tasks()
        elif task == '4':
            break
        else:
            print('Ошибка уведите еще раз')
    except ValueError:
        print('Такого нет в списке')

    



