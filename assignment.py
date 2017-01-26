from common import *
import datetime

class Assignment:
    """
    Class
    """

    assigments_list = []

    def __init__(self, idx, title, author, start_date, end_date, file_name):
        self.idx = idx
        self.title = title
        self.author = author
        self.start_date = start_date
        self.end_date = end_date
        self.file_name = file_name

    @classmethod
    def create_assignment_list(cls):
        """
        Create list containing object of assignments
        :return: None
        """
        list_from_csv = Common.read_file('csv/assignments.csv')
        for item in list_from_csv:
            idx = item[0]
            title = item[1]
            author = item[2]
            if Common.is_date_correct(item[3]):
                start_date = Common.make_corect_date(item[3])
                if Common.is_date_correct(item[4]):
                    end_date = Common.make_corect_date(item[4])
                    if Common.does_file_exist('csv/assignments_description/' + item[5]):
                        file_name = item[5]
                        cls.assigments_list.append(cls(idx, title, author, start_date, end_date, file_name))

    @classmethod
    def add_assignment(cls, title, author, start_date, end_date, file_name):
        """
        Add new student object to list
        :param title: string (assignment name)
        :param author: string (name of mentor)
        :param start_date: datetime object (date of start)
        :param end_date: datetime object (date of end )
        :param file_name: string (file path)
        :return: None
        """
        new_id = Common.generate_id()
        new_assignment = cls(new_id, title, author, start_date, end_date, file_name)
        cls.assigments_list.append(new_assignment)
        Common.save_file('csv/assignments.csv', cls.create_list_to_save())

    @classmethod
    def create_list_to_save(cls):
        list_to_save = []
        for assigment in cls.assigments_list:
            list_to_save.append([assigment.idx, assigment.title, assigment.author,
                                assigment.start_date, assigment.end_date, assigment.file_name])
        return list_to_save

    @classmethod
    def pass_assign_for_mentor(cls):
        return cls.assigments_list

    @classmethod
    def pass_assign_for_student(cls):
        today = datetime.date.today()
        assignments_for_students =[]
        for assignment in cls.assigments_list:
            if assignment.start_date <= today:
                assignments_for_students.append(assignment)
                """if assignment.end_date >= today:
                    assignments_for_students.append(assignment)"""
        return assignments_for_students

    def __str__(self):
        return '{}, start: {}, end: {}'.format(self.title, self.start_date, self.end_date)

# """Assignment.create_assignment_list()
# print(Assignment.assigments_list)
# #Assignment.add_assignment('dupa', 'Gargamel', '1234.05.23', '1234.05.30', 'ass_3.txt')
# #print(Assignment.assigments_list)
# Common.save_file('csv/assignments.csv', Assignment.create_list_to_save())
# lista = Assignment.pass_assign_for_student()
# for item in lista:
#     print(item)"""