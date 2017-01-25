from user import *
from common import *

class Manager(User):
    managers_list = []
    file = 'csv/managers.csv'
    
    def __init__(self, idx, name, last_name, mail, telephone):
        """
        Create Manager object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        User.__init__(self, idx, name, last_name, mail, telephone)

    @classmethod
    def pass_list(cls):
        return cls.managers_list
