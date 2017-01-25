from user import *
from common import *

class Employee(User):
    employees_list = []

    def __init__(self, id, name, last_name, mail, telephone, account_type='Employee'):
        """
        Create Employee object
        :param id: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param type: string (type of account)
        """
        User.__init__(self, id, name, last_name, mail, telephone)
        self.account_type = account_type