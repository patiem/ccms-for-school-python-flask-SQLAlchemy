from app.modules import sql
from app.modules.common import *
from app.modules.mod_student.student import Student
from app.modules.mod_user.user import User
from app.modules.mod_team.team import UsersTeam
from app import db


class Submission(db.Model):
    """
    Class of students submission.
    """
    __tablename__ = "Sumbissions"

    ID = db.Column(db.Integer, primary_key=True)
    ID_ASSIGMENT = db.Column(db.Integer, nullable=False)
    ID_STUDENT = db.Column(db.Integer, nullable=False)
    GRADE = db.Column(db.Integer)
    DATE = db.Column(db.String, nullable=False)
    LINK = db.Column(db.String, nullable=False)
    ID_MENTOR = db.Column(db.Integer)

    def __init__(self, idx, student_idx, assignment_idx, date_of_submission, link, grade=None, mentor_id=None):
        """
        Creates object of Submission class.
        :param student_idx: str (idx of student who wants to make submission)
        :param assignment_idx: str (idx of assignment which will be submitted)
        :param date_of_submission: str (date when submission is made)
        :param link: str (link to repo)
        :param grade: None (if not graded)/ str (if graded)
        :param mentor_id: None/int (id of mentor, who graded submission)
        """
        self.ID = idx
        self.ID_ASSIGMENT = assignment_idx
        self.ID_STUDENT = student_idx
        self.GRADE = grade
        self.DATE = date_of_submission
        self.LINK = link
        self.ID_MENTOR = mentor_id

    @classmethod
    def list_from_sql(cls):
        """
        Returns list with Submission objects
        :return: list
        """
        try:
            submission_list = Submission.query.all()
            return submission_list
        except:
            return []

    @classmethod
    def subs_to_grade(cls):
        """
        Returns list for mentor to grade submission
        :return: submission(obj), student(ID-int),
                 ass_title(str), mentor_name(str)
        """
        from app.modules.mod_assigment.assignment import Assignment
        sub_list = cls.list_from_sql()
        list_for_mentor = []
        for sub in sub_list:
            if Student.make_student(sub.ID_STUDENT):
                ass_title = Assignment.query.filter_by(ID=sub.ID_ASSIGMENT).first()

                if ass_title:
                    ass_title = ass_title.TITLE
                else:
                    ass_title = None

                if sub.ID_MENTOR:
                    mentor_name = User.query.filter_by(ID=sub.ID_MENTOR).first()
                    if mentor_name:
                        mentor_name = mentor_name.full_name()
                else:
                    mentor_name = 'None'

                student = Student.make_student(sub.ID_STUDENT)
                list_for_mentor.append([sub, student, ass_title, mentor_name])
        return list_for_mentor

    @classmethod  # IN USE
    def add_submission(cls, student_idx, assignment_idx, link, comment, group):
        """
        New submission made by student.
        :param student_idx: string
        :param assignment_idx: string
        :param link: string
        :param comment: str
        :return: None
        """
        date_of_submission = datetime.date.today()
        if group == 0:
            members = [student_idx]
        else:
            members = cls.get_team_users(student_idx)
            if not members:
                members = [student_idx]
        for mem in members:
            query = "INSERT INTO `Sumbissions` (ID_STUDENT, ID_ASSIGMENT, GRADE, DATE, LINK, ID_MENTOR)" \
                    "VALUES (?, ?, ?, ?, ?, ?);"
            values_list = [mem, assignment_idx, -1, date_of_submission, link, 0]
            sql.query(query, values_list)
            query_3 = "SELECT max(id) as max_id FROM Sumbissions;"
            sub_id = sql.query(query_3)[0][0]
            query_3 = "INSERT INTO `comments` (sub_id, comment) VALUES (?, ?);"
            param = [sub_id, comment]
            sql.query(query_3, param)

    @staticmethod
    def get_team_users(student_idx):
        """
        Returns list with students ids
        :param student_idx: int
        :return: list with int
        """
        users_team = UsersTeam.query.filter_by(ID_USER=student_idx).first()
        clean_list = []

        if users_team:
            for student in users_team.team.students.all():
                clean_list.append(student.ID_USER)
        return clean_list

    @classmethod
    def find_submission(cls, student, assignment):
        """
        :param student: student object for whom we searching submitted assignment
        :param assignment: assignment object for which checking submission
        :return: submission object / False
        """
        submissions_list = cls.list_from_sql()
        for submission in submissions_list:
            if submission.ID_STUDENT == student.ID:
                if submission.ID_ASSIGMENT == assignment.ID:
                    return submission
        return False

    @classmethod
    def find_submission_sql(cls, assignment_id, student_id):
        """
        :param student_id: logged student id
        :param assignment_id: assignment id
        :return: submission object / False
        """

        submission = cls.query.filter_by(ID_ASSIGMENT=assignment_id, ID_STUDENT=student_id).first()

        if submission:
            return [submission.GRADE, submission.DATE]
        return False

    @classmethod
    def update_grade(cls, grade, link, mentor_id):
        """
        Sets grade & mentor (id) for submission
        :param grade: int
        :param link: str
        :param mentor_id: int
        """
        for submission in Submission.query.filter_by(LINK=link).all():
            submission.GRADE = grade
            submission.ID_MENTOR = mentor_id
        db.session.commit()
