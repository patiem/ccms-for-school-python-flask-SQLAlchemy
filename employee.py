from user import *
from common import *

class Employee(User):
    employees_list = []

    def __init__(self, idx, name, last_name, mail, telephone):
        """
        Create Employee object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        """
        User.__init__(self, idx, name, last_name, mail, telephone)

    @classmethod
    def pass_list(cls):
        return cls.employees_list