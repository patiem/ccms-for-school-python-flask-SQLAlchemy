from common import *

import hashlib
from ui import *

class User:

    def __init__(self, idx, name, last_name, mail, telephone, password):
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
        self.password = password

    def change_value(self, name_of_attribute, new_value):
        if name_of_attribute == 'name':
            self.name = new_value
        elif name_of_attribute == 'last name':
            self.last_name = new_value
        elif name_of_attribute == 'mail':
            self.mail = new_value
        elif name_of_attribute == 'telephone':
            self.telephone = new_value
        elif name_of_attribute == 'password':
            self.password = User.encode(new_value)

    @classmethod
    def edit_user(cls, mail, name_of_attribute, new_value):
        """
        Edit user passed attribute
        :param mail: string (e-mail of user to edit)
        :param object_list: list ( object list contain user)
        :param name_of_attribute: string (what attribute should be edit)
        :param new_value: string (new value for attribute)
        :return: None
        """
        for person in cls.object_list:
            if person.mail == mail:
                person.change_value(name_of_attribute, new_value)





    @classmethod
    def add_user(cls, name, last_name, mail, telephone):
        """
        Add new user object to list
        :param name: string (name of student)
        :param last_name: string (last name)
        :param mail: string (mail of student)
        :param telephone: string (telephone to student)
        :param object_list: list (list of objects to expand)
        :return: None
        """
        new_id = Common.generate_id()
        password = User.encode('1')
        new_student = cls(new_id, name, last_name, mail, telephone, password)
        cls.object_list.append(new_student)

    @classmethod
    def create_object_list(cls, object_list):
        """
        Create list containing objects
        :param object_list: list (class list)
        :return: None
        """
        file = cls.file
        list_from_csv = Common.read_file(file)
        for person in list_from_csv:
            object_list.append(cls(person[0], person[1], person[2], person[3], person[4], person[5]))

    @classmethod
    def remove_object(cls, mail):
        """
        Remove object from list
        :param idx: string ( id of student to remove)
        :return: None or True if object removed
        """
        for person in cls.object_list:
            if person.mail == mail:
                cls.object_list.remove(person)
                return True

    @classmethod
    def create_list_to_save(cls,object_list):
        return_list = []
        for person in object_list:
            person_list = [person.idx, person.name, person.last_name, person.mail, person.telephone, person.password]
            return_list.append(person_list)
        return return_list

    def __str__(self):
        """
        :return: String representation for object
        """
        return 'ID: {} Name: {} Last Name: {}'.format(self.idx, self.name, self.last_name)

    @staticmethod
    def get_id_by_login_and_pass(login, password):

        users_list = Common.aggregation_users()

        for user in users_list:

            if user[1] == login and user[2] == str(password):
                return user

    @classmethod
    def pass_list(cls):
        return cls.object_list

    @staticmethod
    def login():

        Ui.clear()
        Ui.print_head('Authentication', 'header') #displaying header of site

        attempt = 0
        while True:

            inputs = ['Login: ']
            login = Ui.get_inputs(inputs)
            login = login[0]
            encoded_password = User.encode(Ui.get_pass('Password: ')) #get passoword and encode using hash and salt

            if User.get_id_by_login_and_pass(login, encoded_password) is not None:
                Ui.clear()
                return User.get_id_by_login_and_pass(login, encoded_password)

            attempt += 1

            Ui.print_head("Wrong password. It's your {}/3 attempt".format(attempt), 'error')

            if attempt == 3:

                Ui.print_head("Wrong password!!! Exit program", 'error')
                exit(0)
                return None

    @staticmethod
    def encode(password):

        _salt = "Coder"
        encoded_password = hashlib.sha256()
        encoded_password.update(_salt.encode('utf-8') + password.encode('utf-8'))
        encoded_password = encoded_password.digest()

        return str(encoded_password)

