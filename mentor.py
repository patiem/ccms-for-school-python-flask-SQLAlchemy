from user import *

class Mentor(User):
    
    def __init__(self, name, last_name, mail, telephone):
        self.name = name
        self.last_name = last_name
        self.main = mail
        self.telephone = telephone

    def edit_mentor(self):
        pass

    @classmethod
    def add_mentor(cls):
        pass

    @classmethod
    def remove_mentor(cls):
        pass