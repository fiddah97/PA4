from tasklists import TaskList,Task
from lists import List,TaskLists

def generate_tasklists(): #define functione to generate tasklist
    my_task_lists= TaskList()

    task1 = Task('learn flask blueprints',3,3,'is very important')
    task2 = Task('learn Python enums',2,2,' important')
    
    my_task_lists.add_task(task1)
    my_task_lists.add_task(task2)
    return my_task_lists

def generate_lists():  #define functione to generate lists
    my_lists= TaskLists()
    list1=List('python list')
    list2=List('home list')

    my_lists.add_list(list1)
    my_lists.add_list(list2)
    
    return my_lists