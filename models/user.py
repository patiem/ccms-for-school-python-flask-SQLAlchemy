import hashlib
from models.ui import *
from models import sql
from abc import ABCMeta


class User(metaclass=ABCMeta):
    object_list = None

    def __init__(self, idx, name, last_name, mail, telephone):
        """
        Create object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        :param password: string (encode password to usser account)
        """
        self.idx = idx
        self.name = name
        self.last_name = last_name
        self.mail = mail
        self.telephone = telephone

    # def change_value(self, name_of_attribute, new_value):
    #     """
    #     change attribute of instance
    #     :param name_of_attribute: string (what attribute should be change)
    #     :param new_value: string (new value of attribute)
    #     :return: None
    #     """
    #     if name_of_attribute == 'Name':
    #         self.name = new_value
    #     elif name_of_attribute == 'Surname':
    #         self.last_name = new_value
    #     elif name_of_attribute == 'E-mail':
    #         self.mail = new_value
    #     elif name_of_attribute == 'Telephone':
    #         self.telephone = new_value
    #     elif name_of_attribute == 'Password':
    #         self.password = User.encode(new_value)
    #
    # @classmethod
    # def edit_user(cls, edit_list):
    #     """
    #     Edit user passed attribute
    #     :param edit_list: (FORMAT: E-MAIL, ATTRIBUTE, NEW VALUE)
    #     :return: None or True if attribute is changed
    #     """
    #     for person in cls.object_list:
    #         if person.mail == edit_list[0]:
    #             person.change_value(edit_list[1], edit_list[2])
    #             cls.update_sql(edit_list)
    #             return True

    @classmethod
    def return_mails(cls):
        query = """ SELECT `E-MAIL` FROM Users"""
        email_list = []
        data_sql = sql.query(query)
        for item in data_sql:
            email_list.append(item[0])
        return email_list

    @classmethod
    def add_user(cls, data):
        """
        :param data: LIST (FORMAT: NAME, SURNAME, E-MAIL, TELEPHONE)
        :return:
        """
        data.append(User.encode('1'))
        cls.save_sql(data)

    # @classmethod
    # def get_id(cls, mail):
    #     """
    #     find student id by mail
    #     :param mail: mail of student to find
    #     :return: idx ( student id)
    #     """
    #     query = """
    #             SELECT ID
    #             FROM Users
    #             WHERE `E-mail` = ?"""
    #     idx = sql.query(query, [mail])
    #     idx = idx[0]['ID']
    #     return idx

    @classmethod
    def return_by_id(cls, idx):
        """
        Return object of passed id
        :param idx: int (id of object)
        :return: object
        """
        sql_query = "SELECT ID, Name, Surname, `E-mail`, Telephone, Password FROM Users WHERE ID = ?"
        user_data = sql.query(sql_query, [idx])[0]
        if user_data:
            new_object = cls(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
            return new_object

    @classmethod
    def create_object_list(cls):
        """
        Create list containing instance of class
        :return: None
        """
        raise NotImplementedError

    # @classmethod
    # def remove_object(cls, idx):
    #     """
    #     Remove object from list
    #     :param mail: string ( mail of user to remove)
    #     :return: None or True if object removed
    #     """
    #     for person in cls.object_list:
    #         if person.mail == idx:
    #             cls.object_list.remove(person)
    #             cls.remove_sql(idx)
    #             return True

    @staticmethod
    def remove_sql(idx):
        query = """
                DELETE FROM Users
                WHERE ID = ?"""
        sql.query(query, [idx])

    # @staticmethod
    # def create_list_to_save(object_list):
    #     """
    #     crate two dimension list from list contain objects
    #     :param object_list: list ( list of objects)
    #     :return:
    #     """
    #     return_list = []
    #     for person in object_list:
    #         person_list = [person.idx, person.name, person.last_name, person.mail, person.telephone, person.password]
    #         return_list.append(person_list)
    #     return return_list

    def __str__(self):
        """
        :return: String representation for object
        """
        return 'ID: {} Name: {} Last Name: {}'.format(self.idx, self.name, self.last_name)

    @staticmethod
    def get_id_by_login_and_pass(login, password):
        """
        Get id of user by login and pass from user list
        :param login:
        :param password:
        :return:
        """

        query = "SELECT * FROM Users WHERE `E-mail` =? and `password`=?"
        params = list([login, password])

        user = sql.query(query, params)

        if user:
            return user[0]

    @staticmethod
    def update_sql(edit_list):
        raise NotImplementedError

    @staticmethod
    def login(user_login, user_pass):
        """
        login method
        :return user_id:
        """

        encoded_password = User.encode(user_pass)  # get passoword and encode using hash and salt

        if User.get_id_by_login_and_pass(user_login, encoded_password) is not None:

            return User.get_id_by_login_and_pass(user_login, encoded_password)

        else:
            return None

    @staticmethod
    def encode(password):
        """Encoding password using salt and hash sha256
        :param password:
        :return encoded_password:
        """
        _salt = "Coder"
        encoded_password = hashlib.sha256()
        encoded_password.update(_salt.encode('utf-8') + password.encode('utf-8'))
        encoded_password = encoded_password.digest()
        return str(encoded_password)