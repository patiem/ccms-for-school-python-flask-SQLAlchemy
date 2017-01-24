from user import *
from common import *

class Mentor(User):
    mentors_list = []
    
    def __init__(self, id, name, last_name, mail, telephone):
        self.name = name
        self.last_name = last_name
        self.main = mail
        self.telephone = telephone
        self.id = id

    def edit_mentor(self, name_of_attribute, new_value):
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
        new_id = Common.generate_id(Mentor.mentors_list)
        new_mentor = Mentor(new_id ,name, last_name, mail, telephone)
        Mentor.mentors_list.append(new_mentor)

    @classmethod
    def remove_mentor(cls, id):
        for mentor in Mentor.mentors_list:
            if mentor.id == id:
                Mentor.mentors_list.remove(mentor)

    @classmethod
    def create_mentor_list(cls):
        list_from_csv = Common.read_file('csv/mentors.csv')
        for person in list_from_csv:
            Mentor.mentors_list.append(Mentor(person[0], person[1], person[2], person[3], person[4]))