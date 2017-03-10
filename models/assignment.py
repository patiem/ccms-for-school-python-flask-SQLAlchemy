from models.common import *
import datetime
from models.test import Test
from models import sql
from models.submission import Submission
from models.student import Student


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
        assignments_list = []
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
                        assignments_list.append(cls(idx, title, mentor_id, start_date, end_date, file_name, group))
        return assignments_list

    @classmethod
    def add_assignment(cls, title, mentor_id, start_date, end_date, file_name, group='0'):
        """
        Add new student object to list
        :param title: string (assignment name)
        :param mentor_id: int (name of mentor)
        :param start_date: datetime object (date of start)
        :param end_date: datetime object (date of end )pp
        :param file_name: string (file path)
        :param group: bool (group/ind)
        :return: None
        """
        query = "INSERT INTO `Assigments` (TITLE, ID_MENTOR, START_DATA, END_DATA, LINK, `GROUP`)" \
                "VALUES (?, ?, ?, ?, ?, ?);"
        values_list = [title, mentor_id, start_date, end_date, file_name, group]
        sql.query(query, values_list)

    # @classmethod
    # def create_list_to_save(cls):
    #     """
    #     Creates 2d list which can be use for saving process
    #     :return: list_to_save - 2d list ready to be saved in csv file
    #     """
    #     list_to_save = []
    #     for assigment in cls.assigments_list:
    #         list_to_save.append([assigment.idx, assigment.title, assigment.mentor_id,
    #                             assigment.start_date, assigment.end_date, assigment.file_name])
    #     return list_to_save

    @classmethod
    def pass_assign_for_mentor(cls):
        """
        Passes full list of assignments.
        :return: Assignment.assigments_list (list)
        """
        assignments_list = cls.list_from_sql()
        return assignments_list

    @classmethod
    def pass_assign_for_student(cls):
        """
        Passes only past and present assignments, assignments which starts in future are not
        visible for students.
        :return: assignments_for_students (list)
        """
        today = datetime.date.today()
        assignments_for_students = []
        assignments_list = cls.list_from_sql()
        for assignment in assignments_list:
            if assignment.start_date <= today:
                assignments_for_students.append(assignment)
        return assignments_for_students

    def __str__(self):
        """
        :return: String representation for object
        """
        return '{}, start: {}, end: {}'.format(self.title, self.start_date, self.end_date)

    # def assignment_description(self):
    #     """
    #     Creates string from description file of assignment.
    #     :return: text_to_print (str)
    #     """
    #     filename = 'csv/assignments_description/{}'.format(self.file_name)
    #     with open(filename, 'r') as f:
    #         text_to_print = f.read()
    #     return text_to_print

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

    @staticmethod
    def assignment_list_with_grades(user_id):  # IN USE
        """
        Makes list with assignments visible for student with notation if assignment was submitted
        and how it was graded.
        :param user_id: int (logged user id from seesion)
        :return: assignments_list_to_print (list with all available assignments)
        """
        logged_user = Student.make_student(user_id)
        Assignment.list_from_sql()
        assignments_list = Assignment.pass_assign_for_student()
        assignments_list_to_print = []
        for assignment in assignments_list:
            type_of_assignment = 'Individual'
            if assignment.group == '1':
                type_of_assignment = 'Group'
            new_line = [assignment.title, assignment.mentor_id, assignment.start_date, assignment.end_date,
                        type_of_assignment]
            submission = Submission.find_submission(logged_user, assignment)
            if submission:
                new_line.append('submitted')
                if submission.grade:
                    new_line.append(submission.grade)
                else:
                    new_line.append('None')
            else:
                new_line.append('not submitted')
                new_line.append('None')
            new_line.append(assignment.idx)
            assignments_list_to_print.append(new_line)

        return assignments_list_to_print
