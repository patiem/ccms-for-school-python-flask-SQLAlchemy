from common import *
import datetime

class Submission:
    """
    Class
    """

    submission_list = []

    def __init__(self, student_idx, assignment_idx, date_of_submission, link, grade=None):
        self.student_idx = student_idx
        self.assignment_idx = assignment_idx
        self.date_of_submission = date_of_submission
        self.link = link
        self.grade = grade

    @classmethod
    def create_submission_list(cls):
        """
        Create list containing object of assignments
        :return: None
        """
        list_from_csv = Common.read_file('csv/submission.csv')
        for item in list_from_csv:
            student_idx = item[0]
            assignment_idx = item[1]
            if Common.is_date_correct(item[2]):
                date_of_submission = Common.make_corect_date(item[2])
                link = item[3]
                if item[4] != 'None':
                    grade = item[4]
                    cls.submission_list.append(cls(student_idx, assignment_idx, date_of_submission, link, grade))
                else:
                    cls.submission_list.append(cls(student_idx, assignment_idx, date_of_submission, link))

    @classmethod
    def add_submission(cls, student_idx, assignment_idx, date_of_submission):
        """
        Add new student object to list
        :param student_idx: string
        :param assignment_idx: string
        :param date_of_submission: string
        :return: None
        """
        new_submission = cls(student_idx, assignment_idx, date_of_submission)
        cls.submission_list.append(new_submission)

    @classmethod
    def create_list_to_save(cls):
        list_to_save = []
        for submission in cls.submission_list:
            list_to_save.append([submission.student_idx, submission.assignment_idx, submission.date_of_submission,
                                 str(submission.grade)])
        return list_to_save

    @classmethod
    def pass_submission_for_student(cls, student):
        submission_for_student = []
        for submission in cls.submission_list:
            if submission[0] == student.idx:
                submission_for_student.append(submission)
        return submission_for_student