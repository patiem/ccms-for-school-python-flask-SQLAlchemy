from user import *
from common import *

class Student(User):
    """
    Class represent student
    """
    students_list = []
    file = 'csv/students.csv'

    def __init__(self, idx, name, last_name, mail, telephone):
        """
        Create Student object
        :param id: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        User.__init__(self, idx, name, last_name, mail, telephone)

    @classmethod
    def pass_list(cls):
        return cls.students_list



Student.create_object_list('csv/students.csv', Student.students_list)
new = Student.create_list_to_save(Student.students_list)
print(new)