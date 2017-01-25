from user import *
from common import *

class Mentor(User):
    mentors_list = []
    
    def __init__(self, id, name, last_name, mail, telephone):
        """
        Create Mentor object
        :param id: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        self.name = name
        self.last_name = last_name
        self.main = mail
        self.telephone = telephone
        self.id = id

    def edit_mentor(self, name_of_attribute, new_value):
        """
        Edit metor passed attribute
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
    def add_mentor(cls, name, last_name, mail, telephone):
        """
        Add new mentor object to list
        :param name: string (name of student)
        :param last_name: string (last name)
        :param mail: string (mail of student)
        :param telephone: string (telephone to student)
        :return: None
        """
        if Common.is_email_correct(mail):
            if Common.is_phone_correct(telephone):
                new_id = Common.generate_id(Mentor.mentors_list)
                new_mentor = Mentor(new_id ,name, last_name, mail, telephone)
                Mentor.mentors_list.append(new_mentor)
            else:
                raise ValueError('Wrong number')
        else:
            raise ValueError('Wrong e-mail')

    @classmethod
    def remove_mentor(cls, id):
        """
        Remove mentor from list of mentors
        :param id: string ( id of student to remove)
        :return: None
        """
        for mentor in Mentor.mentors_list:
            if mentor.id == id:
                Mentor.mentors_list.remove(mentor)

    @classmethod
    def create_mentor_list(cls):
        """
        Create list containing objects of mentors
        :return: None
        """
        list_from_csv = Common.read_file('csv/mentors.csv')
        for person in list_from_csv:
            Mentor.mentors_list.append(Mentor(person[0], person[1], person[2], person[3], person[4]))