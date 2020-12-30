from status import Status      
from priority import Priority
from enum import Enum



class TaskList: #class TaskList contain the group of tasks
    def __init__(self):
        self.taskslists=dict()

    def add_task(self,task):
        self.taskslists[task.id]= task

    def get_task_by_id(self,id):
        return self.taskslists.get(id)

    def remove_task(self,id):
        self.taskslists.pop(id,None)

    def get_taskslists(self):
        return self.taskslists



class Task:
    def __init__(self,name,status,priority,description):
        self.name=name
        self.status=Status(status)
        self.priority=Priority(priority)
        self.description=description
        self.id = id(self)
     

    def set_task_name(self,name):
        self.name=name

    def get_name_of_task(self):
        return self.name

    def set_status(self,status):
        self.status=Status(status)
    
    def get_status(self):
        return self.status
    
    def set_priority(self,priority):
        self.priority=Priority(priority)

    def get_priority(self):
        return self.priority

    def set_description(self,description):
        self.description=description

    def get_description(self):
        return self.description







