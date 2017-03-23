
from app import db
from app.modules import sql
from app.modules.common import *
from app.modules.mod_student.student import Student
from app.modules.mod_submission.submission import Submission
from app.modules.test import Test


class Assignment(db.Model):
    """
    Class of assignments.
    """

    # assigments_list = []
    __tablename__ = 'Assigments'
    ID = db.Column(db.Integer, primary_key=True)
    ID_MENTOR = db.Column(db.Integer)
    TITLE = db.Column(db.String)
    START_DATA = db.Column(db.String)
    END_DATA = db.Column(db.String)
    LINK = db.Column(db.String)
    GROUP = db.Column(db.String)

    def __init__(self, title, mentor_id, start_date, end_date, file_name, group='0'):
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
        self.ID_MENTOR = mentor_id
        self.TITLE = title
        self.START_DATA = start_date
        self.END_DATA = end_date
        self.LINK = file_name
        self.GROUP = group

    @classmethod
    def list_from_sql(cls):
        assignments_list = cls.query.all()
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
        new = Assignment(mentor_id, title, start_date, end_date, file_name, group)
        db.session.add(new)
        db.session.commit()

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
        assignments_list = Assignment.query.filter(Assignment.START_DATA <= today).all()
        return assignments_list

    def __str__(self):
        """
        :return: String representation for object
        """
        return '{}, start: {}, end: {}'.format(self.title, self.start_date, self.end_date)


    @classmethod
    def get_by_id(cls, assignment_idx):
        assignment = Assignment.query.filter_by(ID=assignment_idx).first()
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
            if assignment.GROUP == '1':
                type_of_assignment = 'Group'
            new_line = [assignment.TITLE, assignment.ID_MENTOR, assignment.START_DATA, assignment.END_DATA,
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
            new_line.append(assignment.ID)
            assignments_list_to_print.append(new_line)

        return assignments_list_to_print