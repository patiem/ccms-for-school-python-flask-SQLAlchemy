from common import *

class User:

    _users_csv = 'csv/users.csv'  # database with users

    def __init__(self, idx, name, last_name, mail, telephone):
        """
        Create object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        self.idx = idx
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
    def remove_object(cls, idx, object_list):
        """
        Remove object from list
        :param idx: string ( id of student to remove)
        :return: None
        """
        for person in object_list:
            if person.idx == idx:
                object_list.remove(person)
                break

    @classmethod
    def create_list_to_save(cls,object_list):
        return_list = []
        for person in object_list:
            person_list = [person.idx, person.name, person.last_name, person.mail, person.telephone]
            return_list.append(person_list)
        return return_list

    def __str__(self):
        """
        :return: String representation for object
        """
        return 'ID: {} Name: {} Last Name: {}'.format(self.idx, self.name, self.last_name)

    @classmethod
    def login(cls, login, password):


        Logged = True

        Logged = False

        return Logged
