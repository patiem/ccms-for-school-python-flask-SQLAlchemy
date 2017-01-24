from user import *

class Student(User):
    """
    Class represent student
    """
    students_list = []



    def __init__(self, name, last_name, mail, telephone, attendance_list = None, assignment_list = None):
        self.name = name
        self.last_name = last_name
        self.mail = mail
        self.telephone = telephone
        if attendance_list == None:
            self.attendance_list = []
        else:
            self.attendance_list = attendance_list
        if assignment_list == None:
            self.assignment_list = []
        else:
            self.assignment_list =assignment_list



    def edit_student(self, name_of_attribute, new_value, data = None):
        if name_of_attribute == 'Name':
            self.name = new_value
        elif name_of_attribute == 'Last Name':
            self.last_name = new_value
        elif name_of_attribute == 'mail':
            self.mail = new_value
        elif name_of_attribute == 'telephone':
            self.telephone = new_value
        elif name_of_attribute == 'attendance':
            self.attendance_list = self.change_attendance(self.attendance_list, data, new_value)



    def change_attendance(self, attandance_list, data, new_value):
        for item in attandance_list:
            if item[0] == data:
                item[1] = new_value
        return attandance_list


    @classmethod
    def add_student(cls):
        pass

    @classmethod
    def remove_student(cls):

        pass