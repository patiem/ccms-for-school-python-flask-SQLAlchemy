from app.modules.user import *
from app.modules import sql


class Employee(User):

    def __init__(self, idx, name, last_name, mail, telephone, password):
        """
        Create Employee object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        """
        User.__init__(self, idx, name, last_name, mail, telephone, password)
    #
    # @classmethod
    # def create_object_list(cls):
    #     """
    #     Create objects of class Employee
    #     :return: None
    #     """
    #     query = """
    #               SELECT ID, Name, Surname, `E-mail`, Telephone, Password
    #               FROM Users
    #               WHERE Type = 'Employee'"""
    #     data = sql.query(query)
    #     if data:
    #         for row in data:
    #             new_object = cls(row[0], row[1], row[2], row[3], row[4], row[5])
    #             cls.object_list.append(new_object)

    # @classmethod
    # def save_sql(cls, data):
    #     """
    #     Save data to sql
    #     :param data: list (FORMAT : NAME, SURNAME, E-MAIL, TELEPHONE, PASSWORD)
    #     :return:
    #     """
    #     query = """
    #                 INSERT INTO Users (Name, Surname, `E-mail`, Telephone, Password, Type)
    #                 VALUES (?, ?, ?, ?, ?, 'Employee')"""
    #     sql.query(query, data)
    #
    # @staticmethod
    # def update_sql(edit_list):
    #     """
    #     :param edit_list: (FORMAT: E-MAIL, ATTRIBUTE, NEW VALUE)
    #     :return:
    #     """
    #
    #     query = """
    #               UPDATE Users
    #               SET `{}` = ?
    #               WHERE `E-mail` = ?
    #               AND Type = 'Employee'""".format(edit_list[1])
    #     sql.query(query, [edit_list[2], edit_list[0]])