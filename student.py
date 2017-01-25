from user import *
from common import *

class Student(User):
    """
    Class represent student
    """
    students_list = []



    def __init__(self, id, name, last_name, mail, telephone):
        """
        Create Student object
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




    def edit_student(self, name_of_attribute, new_value):
        """
        Edit student passed attribute
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
    def add_student(cls, name, last_name, mail, telephone):
        """
        Add new student object to list
        :param name: string (name of student)
        :param last_name: string (last name)
        :param mail: string (mail of student)
        :param telephone: string (telephone to student)
        :return: None
        """
        if Common.is_email_correct(mail):
            if Common.is_phone_correct(telephone):
                new_id = Common.generate_id(Student.students_list)
                new_student = Student(new_id ,name, last_name, mail, telephone)
                Student.students_list.append(new_student)
            else:
                raise ValueError('Wrong number')
        else:
            raise ValueError('Wrong e-mail')

    @classmethod
    def remove_student(cls, id):
        """
        Remove student from list of students
        :param id: string ( id of student to remove)
        :return: None
        """
        for student in Student.students_list:
            if student.id == id:
                Student.students_list.remove(student)


    @classmethod
    def create_student_list(cls):
        """
        Create list containing object of students
        :return: None
        """
        list_from_csv = Common.read_file('csv/students.csv')
        for person in list_from_csv:
            Student.students_list.append(Student(person[0], person[1], person[2], person[3], person[4]))

    def __str__(self):
        """
        :return: String representation for object
        """
        return 'ID: {} Name: {} Last Name: {}'.format(self.id, self.name, self.last_name)



