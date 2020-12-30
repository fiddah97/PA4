from tasklists import TaskList,Task


def generate_tasklists():
    my_task_lists= TaskList()

    task1 = Task('learn flask blueprints',3,3,'is very important')
    task2 = Task('learn Python enums',2,2,' dfjhsj')
    
    my_task_lists.add_task(task1)
    my_task_lists.add_task(task2)
    return my_task_lists

tasks_list = generate_tasklists()

class TaskLists: #class TaskLists contain the lists
    def __init__(self):
        self.todolist=dict()
        self.value=tasks_list

    def add_list(self,list_):
        self.todolist[list_.id]= list_

    def get_list_by_id(self,id):
        return self.todolist.get(id)

    def remove_list(self,id):
        self.todolist.pop(id,None)

    def get_todolist(self):
        return self.todolist
    
    
    
    def value_of_list(self,id):
        return self.value






class List: 
    def __init__(self,listname):
        self.listname= listname
        self.id = id(self)
        self.value = tasks_list

    
    def value_of_list(self,id):
        return self.value



    def set_listname(self,listname):
        self.listname=listname

    def get_listname(self):
        return self.listname

    


