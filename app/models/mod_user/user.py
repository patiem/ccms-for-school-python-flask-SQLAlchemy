import hashlib
from app.models import sql
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

    @classmethod
    def return_by_id(cls, idx):
        """
        Return object of passed id
        :param idx: int (id of object)
        :return: object
        """
        sql_query = "SELECT ID, Name, Surname, `E-mail`, Telephone, Password FROM Users WHERE ID = ?"

        user_data = sql.query(sql_query, [idx])

        if user_data:
            new_object = cls(user_data[0][0], user_data[0][1], user_data[0][2], user_data[0][3], user_data[0][4])
            return new_object
        return False

    @classmethod
    def create_object_list(cls):
        """
        Create list containing instance of class
        :return: None
        """
        raise NotImplementedError

    @staticmethod
    def remove_sql(idx):
        query = """
                DELETE FROM Users
                WHERE ID = ?"""
        sql.query(query, [idx])
        query = """
                    DELETE FROM Attendance
                    WHERE ID_STUDENT = ?"""
        sql.query(query, [idx])

        query = """
                DELETE FROM Attendance
                WHERE ID_STUDENT = ?"""
        sql.query(query, [idx])

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

    def full_name(self):
        return self.name + ' ' + self.last_name