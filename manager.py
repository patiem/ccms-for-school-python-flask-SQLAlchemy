from user import *
from common import *

class Manager(User):
    managers_list = []
    
    def __init__(self, id, name, last_name, mail, telephone):
        self.name = name
        self.last_name = last_name
        self.main = mail
        self.telephone = telephone
        self.id = id

    def edit_manager(self, name_of_attribute, new_value):
        if name_of_attribute == 'Name':
            self.name = new_value
        elif name_of_attribute == 'Last Name':
            self.last_name = new_value
        elif name_of_attribute == 'mail':
            self.mail = new_value
        elif name_of_attribute == 'telephone':
            self.telephone = new_value

    @classmethod
    def add_manager(cls, name, last_name, mail, telephone):
        new_id = Common.generate_id(Manager.managers_list)
        new_manager = Manager(new_id ,name, last_name, mail, telephone)
        Manager.managers_list.append(new_manager)

    @classmethod
    def remove_manager(cls, id):
        for manager in Manager.managers_list:
            if manager.id == id:
                Manager.managers_list.remove(manager)



    @classmethod
    def create_manager_list(cls):
        list_from_csv = Common.read_file('csv/managers.csv')
        for person in list_from_csv:
            Manager.managers_list.append(Manager(person[0], person[1], person[2], person[3], person[4]))