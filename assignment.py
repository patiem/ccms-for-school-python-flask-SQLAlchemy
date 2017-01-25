from common import *


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
        list_from_csv = Common.read_file('csv/assigments.csv')
        for item in list_from_csv:
            idx = item[0]
            title = item[1]
            author = item[2]
            if Common.is_date_correct(item[3]):
                start_date = Common.make_corect_date(item[3])
                if Common.is_date_correct(item[4]):
                    end_date = Common.make_corect_date(item[4])
                    if Common.does_file_exist(item[5]):
                        file_name = item[5]
                        cls.assigments_list.append(cls(idx, title, author, start_date, end_date, file_name))

    @classmethod
    def add_assignment(cls, title, author, start_date, end_date, file_name):
        """
        Add new student object to list
        :param title: string (name of student)
        :param author: string (last name)
        :param start_date: string (mail of student)
        :param end_date: string (telephone to student)
        :param file_name: string (telephone to student)
        :return: None
        """
        new_id = Common.generate_id(cls.assigments_list)
        new_assignment = cls(new_id, title, author, start_date, end_date, file_name)
        cls.assigments_list.append(new_assignment)
