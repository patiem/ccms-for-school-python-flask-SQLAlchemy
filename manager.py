from user import *
from common import *

class Manager(User):
    managers_list = []
    
    def __init__(self, id, name, last_name, mail, telephone):
        """
        Create Manager object
        :param id: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        self.name = name
        self.last_name = last_name
        self.main = mail
        self.telephone = telephone
        self.id = id

    def edit_manager(self, name_of_attribute, new_value):
        """
        Edit manager passed attribute
        :param name_of_attribute: string (what attribute should be edit)
        :param new_value: string (new value for attribute)
        :return: None
        """
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
        """
        Add new manager object to list
        :param name: string (name of student)
        :param last_name: string (last name)
        :param mail: string (mail of student)
        :param telephone: string (telephone to student)
        :return: None
        """
        if Common.is_email_correct(mail):
            if Common.is_phone_correct(telephone):
                new_id = Common.generate_id(Manager.managers_list)
                new_manager = Manager(new_id ,name, last_name, mail, telephone)
                Manager.managers_list.append(new_manager)
            else:
                raise ValueError('Wrong number')
        else:
            raise ValueError('Wrong e-mail')

    @classmethod
    def remove_manager(cls, id):
        """
        Remove manager from list of managers
        :param id: string ( id of student to remove)
        :return: None
        """
        for manager in Manager.managers_list:
            if manager.id == id:
                Manager.managers_list.remove(manager)



    @classmethod
    def create_manager_list(cls):
        """
        Create list containing object of managers
        :return: None
        """
        list_from_csv = Common.read_file('csv/managers.csv')
        for person in list_from_csv:
            Manager.managers_list.append(Manager(person[0], person[1], person[2], person[3], person[4]))