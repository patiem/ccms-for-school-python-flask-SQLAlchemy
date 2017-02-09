from user import *
from common import *
import sql

class Employee(User):
    object_list = []
    file = 'csv/employees.csv'

    def __init__(self, idx, name, last_name, mail, telephone, password):
        """
        Create Employee object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        """
        User.__init__(self, idx, name, last_name, mail, telephone, password)

    @classmethod
    def create_object_list(cls):
        query = """
                  SELECT ID, Name, Surname, `E-mail`, Telephone, Password
                  FROM Users
                  WHERE Type = 'Employee'"""
        data = sql.query(query)
        for row in data:
            new_object = cls(row[0], row[1], row[2], row[3], row[4], row[5])
            cls.object_list.append(new_object)

    @classmethod
    def save_sql(cls, data):
        """
        Save data to sql
        :param data: list (FORMAT : NAME, SURNAME, E-MAIL, TELEPHONE, PASSWORD)
        :return:
        """
        query = """
                    INSERT INTO Users (Name, Surname, `E-mail`, Telephone, Password, Type)
                    VALUES (?, ?, ?, ?, ?, 'Employee')"""
        sql.query(query, data)