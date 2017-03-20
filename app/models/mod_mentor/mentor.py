from app.models.mod_user.user import *
from app.models import sql


class Mentor(User):
    
    def __init__(self, idx, name, last_name, mail, telephone):
        """
        Create Mentor object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        """
        User.__init__(self, idx, name, last_name, mail, telephone)

    # @classmethod
    # def create_object_list(cls):
    #     """
    #     Create objects to list in class Mentor
    #     :return: None
    #     """
    #     query = """
    #                SELECT ID, Name, Surname, `E-mail`, Telephone, Password
    #                FROM Users
    #                WHERE Type = 'Mentor'"""
    #     data = sql.query(query)
    #     if data:
    #         for row in data:
    #             new_object = cls(row[0], row[1], row[2], row[3], row[4], row[5])
    #             cls.object_list.append(new_object)

    @staticmethod
    def save_sql(data):
        """
        Save data to sql
        :param data: list (FORMAT : NAME, SURNAME, E-MAIL, TELEPHONE, PASSWORD)
        :return:
        """
        query = """
                    INSERT INTO Users (Name, Surname, `E-mail`, Telephone, Password, Type)
                    VALUES (?, ?, ?, ?, ?, 'Mentor')"""
        sql.query(query, data)

    @staticmethod
    def update_sql(edit_list):
        """
        :param edit_list: (FORMAT:Name, Surname,  E-MAIL, Telephone, ID)
        :return:
        """

        query = """UPDATE USERS
                           SET Name = ?, Surname = ?, `E-mail` = ?, Telephone = ?
                           WHERE ID = ?"""
        sql.query(query, edit_list)

    @classmethod
    def create_mentor_list(cls):
        query = """
                  SELECT ID, Name, Surname, `E-mail`, Telephone, Password
                  FROM Users
                  WHERE Type = 'Mentor'"""
        data = sql.query(query)
        table = []

        if data:
            for row in data:
                table.append([row[0], row[1], row[2], row[3], row[4], row[5]])
        return table

    @staticmethod
    def mentor_exist(id):
        query = "SELECT * FROM users WHERE type='Mentor' AND ID=?"
        result=sql.query(query, [id])
        if result is not None:
            return True
        else:
            return False