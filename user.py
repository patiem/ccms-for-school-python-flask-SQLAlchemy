from common import *
import hashlib
from ui import *

class User:

    _salt = "Coder"
    _users_csv = 'csv/users.csv'  # database with users

    def __init__(self, id, name, last_name, mail, telephone):
        """
        Create object
        :param id: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        self.id = id
        self.name = name
        self.last_name = last_name
        self.mail = mail
        self.telephone = telephone

    def edit_user(self, name_of_attribute, new_value):
        """
        Edit user passed attribute
        :param name_of_attribute: string (what attribute should be edit)
        :param new_value: string (new value for attribute)
        :return: None
        """
        if name_of_attribute == 'Name':
            self.name = new_value
        elif name_of_attribute == 'Last Name':
            self.last_name = new_value
        elif name_of_attribute == 'mail':
            self.mail = new_value
        elif name_of_attribute == 'telephone':
            self.telephone = new_value

    @classmethod
    def add_user(cls, name, last_name, mail, telephone, object_list):
        """
        Add new user object to list
        :param name: string (name of student)
        :param last_name: string (last name)
        :param mail: string (mail of student)
        :param telephone: string (telephone to student)
        :param object_list: list (list of objects to expand)
        :return: None
        """
        if Common.is_email_correct(mail):
            if Common.is_phone_correct(telephone):
                new_id = Common.generate_id(object_list)
                new_student = cls(new_id, name, last_name, mail, telephone)
                object_list.append(new_student)
            else:
                raise ValueError('Wrong number')
        else:
            raise ValueError('Wrong e-mail')

    @classmethod
    def create_object_list(cls, file, object_list):
        """
        Create list containing objects
        :param file : string (path to file with data)
        :param object_list: list (class list)
        :return: None
        """
        list_from_csv = Common.read_file(file)
        for person in list_from_csv:
            object_list.append(cls(person[0], person[1], person[2], person[3], person[4]))

    @classmethod
    def remove_object(cls, id, object_list):
        """
        Remove object from list
        :param id: string ( id of student to remove)
        :return: None
        """
        for person in object_list:
            if person.id == id:
                object_list.remove(person)
                break

    def __str__(self):
        """
        :return: String representation for object
        """
        return 'ID: {} Name: {} Last Name: {}'.format(self.id, self.name, self.last_name)

    @classmethod
    def get_id_by_login_and_pass(cls, login, password):

        users_list = Common.read_file(cls._users_csv)

        for user in users_list:
            print(user)
            print(password)
            if user[2] == login and user[3] == str(password):
                return user

    @classmethod
    def login(cls):

        Ui.clear()
        Ui.print_head('Authentication', 'header') #displaying header of site
        inputs = ['Login: ']
        login = Ui.get_inputs(inputs)
        login = login[0]
        encoded_password = User.encode(Ui.get_pass('Password: ')) #get passoword and encode using hash and salt

        if User.get_id_by_login_and_pass(login, encoded_password) is not None:
            Ui.clear()
            return User.get_id_by_login_and_pass(login, encoded_password)
        else:
            return None

    @classmethod
    def encode(cls, password):

        encoded_password = hashlib.sha256()
        encoded_password.update(cls._salt.encode('utf-8') + password.encode('utf-8'))
        encoded_password = encoded_password.digest()

        return str(encoded_password)


