from user import *
from common import *

class Student(User):
    """
    Class represent student
    """
    students_list = []



    def __init__(self, id, name, last_name, mail, telephone):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.mail = mail
        self.telephone = telephone




    def edit_student(self, name_of_attribute, new_value):
        if name_of_attribute == 'Name':
            self.name = new_value
        elif name_of_attribute == 'Last Name':
            self.last_name = new_value
        elif name_of_attribute == 'mail':
            self.mail = new_value
        elif name_of_attribute == 'telephone':
            self.telephone = new_value

    @classmethod
    def add_student(cls, name, last_name, mail, telephone):
        new_id = 5
        new_student = Student(new_id ,name, last_name, mail, telephone)
        Student.students_list.append(new_student)

    @classmethod
    def remove_student(cls, id):
        for student in Student.students_list:
            if student.id == id:
                Student.students_list.remove(student)

    @classmethod
    def add_attendance(cls, attandance_list):
        i = 0
        for student in Student.students_list:
            student.attendance_list.append(attandance_list[i])

    @classmethod
    def create_student_list(cls):
        list_from_csv = Common.read_file('csv/students.csv')
        for person in list_from_csv:
            Student.students_list.append(Student(person[0], person[1], person[2], person[3], person[4]))

    def __str__(self):
        return 'ID: {} Name: {} Last Name: {}'.format(self.id, self.name, self.last_name)





