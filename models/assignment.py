from models.common import *
import datetime
from models.test import Test
from models import sql


class Assignment:
    """
    Class of assignments.
    """

    assigments_list = []

    def __init__(self, idx, title, mentor_id, start_date, end_date, file_name, group='0'):
        """
        Creates object of Assignment class.
        :param idx: str (unique randomly created id)
        :param title: str (title of assignmnet)
        :param mentor_id: int (id of author)
        :param start_date: datetime object (date of assignment"s start)
        :param end_date: datetime object (date of assignment's end)
        :param file_name: str (link to assignments txt file with description)
        :param group: int (if assignment is for group = 1, else 0)

        """
        self.idx = idx
        self.title = title
        self.mentor_id = mentor_id
        self.start_date = start_date
        self.end_date = end_date
        self.file_name = file_name
        self.group = group

    @classmethod
    def list_from_sql(cls):
        cls.assigments_list = []
        query = "SELECT * FROM `Assigments`;"
        list_from_sql = sql.query(query)
        if list_from_sql:
            for item in list_from_sql:
                idx = item['ID']
                title = item['TITLE']
                mentor_id = item['ID_MENTOR']
                if Test.is_date_correct(item['START_DATA']):
                    start_date = Common.make_corect_date(item['START_DATA'])
                    if Test.is_date_correct(item['END_DATA']):
                        end_date = Common.make_corect_date(item['END_DATA'])
                        file_name = item['LINK']
                        group = item['GROUP']
                        cls.assigments_list.append(cls(idx, title, mentor_id, start_date, end_date, file_name, group))

    @classmethod
    def add_assignment(cls, title, mentor_id, start_date, end_date, file_name, group='0'):
        """
        Add new student object to list
        :param title: string (assignment name)
        :param mentor_id: int (name of mentor)
        :param start_date: datetime object (date of start)
        :param end_date: datetime object (date of end )
        :param file_name: string (file path)
        :param group: bool (group/ind)
        :return: None
        """
        query = "INSERT INTO `Assigments` (TITLE, ID_MENTOR, START_DATA, END_DATA, LINK, `GROUP`) VALUES (?, ?, ?, ?, ?, ?);"
        values_list = [title, mentor_id, start_date, end_date, file_name, group]
        sql.query(query, values_list)
        query_2 = "SELECT MAX(`ID`) FROM `Assigments`;"
        new_id = sql.query(query_2)[0]
        new_assignment = cls(new_id, title, mentor_id, start_date, end_date, file_name, group)
        if cls.assigments_list:
            cls.assigments_list.append(new_assignment)

    @classmethod
    def create_list_to_save(cls):
        """
        Creates 2d list which can be use for saving process
        :return: list_to_save - 2d list ready to be saved in csv file
        """
        list_to_save = []
        for assigment in cls.assigments_list:
            list_to_save.append([assigment.idx, assigment.title, assigment.mentor_id,
                                assigment.start_date, assigment.end_date, assigment.file_name])
        return list_to_save

    @classmethod
    def pass_assign_for_mentor(cls):
        """
        Passes full list of assignments.
        :return: Assignment.assigments_list (list)
        """
        cls.assigments_list = []
        cls.list_from_sql()
        return cls.assigments_list

    @classmethod
    def pass_assign_for_student(cls):
        """
        Passes only past and present assignments, assignments which starts in future are not
        visible for students.
        :return: assignments_for_students (list)
        """
        today = datetime.date.today()
        assignments_for_students = []
        for assignment in cls.assigments_list:
            if assignment.start_date <= today:
                assignments_for_students.append(assignment)
                """if assignment.end_date >= today:
                    assignments_for_students.append(assignment)"""
        return assignments_for_students

    def __str__(self):
        """
        :return: String representation for object
        """
        return '{}, start: {}, end: {}'.format(self.title, self.start_date, self.end_date)


    def assignment_description(self):
        """
        Creates string from description file of assignment.
        :return: text_to_print (str)
        """
        filename = 'csv/assignments_description/{}'.format(self.file_name)
        with open(filename, 'r') as f:
            text_to_print = f.read()
        return text_to_print

    # @classmethod
    # def get_by_id(cls, assignment_idx):
    #     for assignment in cls.assigments_list:
    #         if assignment.idx == assignment_idx:
    #             return assignment

    @classmethod
    def get_by_id(cls, assignment_idx):
        query = "SELECT * FROM `assigments` WHERE id=?"
        params = [assignment_idx]
        assignment = sql.query(query, params)[0]
        print(assignment)
        return assignment
