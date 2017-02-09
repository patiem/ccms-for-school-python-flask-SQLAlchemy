from user import *
from common import *
import sql

class Manager(User):
    object_list = []
    file = 'csv/managers.csv'
    
    def __init__(self, idx, name, last_name, mail, telephone, password):
        """
        Create Manager object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        User.__init__(self, idx, name, last_name, mail, telephone, password)


    @classmethod
    def create_object_list(cls):
        query = """
                        SELECT ID, Name, Surname, `E-mail`, Telephone, Password
                        FROM Users
                        WHERE Type = 'Manager'"""
        data = sql.query(query)
        for row in data:
            new_object = cls(row[0], row[1], row[2], row[3], row[4], row[5])
            cls.object_list.append(new_object)

