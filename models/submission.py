from models.common import *
from models.test import Test
from models import sql
from models.team import Team


class Submission:
    """
    Class of students submission.
    """

    submission_list = []

    def __init__(self, student_idx, assignment_idx, date_of_submission, link, grade=None, mentor_id=None):
        """
        Creates object of Submission class.
        :param student_idx: str (idx of student who wants to make submission)
        :param assignment_idx: str (idx of assignment which will be submitted)
        :param date_of_submission: str (date when submission is made)
        :param link: str (link to repo)
        :param grade: None (if not graded)/ str (if graded)
        :param mentor_id: None/int (id of mentor, who graded submission)
        """
        self.student_idx = student_idx
        self.assignment_idx = assignment_idx
        self.date_of_submission = date_of_submission
        self.link = link
        self.grade = grade
        self.mentor_id = mentor_id

    @classmethod
    def list_from_sql(cls):
        submission_list = []
        query = "SELECT * FROM `Sumbissions`;"
        list_from_sql = sql.query(query)
        if list_from_sql:
            for item in list_from_sql:

                student_idx = item['ID_STUDENT']
                assignment_idx = item['ID_ASSIGMENT']
                mentor_id = item['ID_MENTOR']
                grade = item['GRADE']
                date = item['DATE']
                link = item['LINK']
                if Test.is_date_correct(date):
                    date_of_submission = Common.make_corect_date(date)
                    if grade != 0:
                        submission_list.append(cls(student_idx, assignment_idx, date_of_submission, link, grade, mentor_id))
                    else:
                        submission_list.append(cls(student_idx, assignment_idx, date_of_submission, link))
        return submission_list

    @classmethod
    def create_submission_list(cls):
        """
        Create list containing object of submission of all students. Validates if data is correct.
        :return: None
        """
        list_from_csv = Common.read_file('csv/submission.csv')
        for item in list_from_csv:
            student_idx = item[0]
            assignment_idx = item[1]
            if Test.is_date_correct(item[2]):
                date_of_submission = Common.make_corect_date(item[2])
                link = item[3]
                if item[4] != 'None':
                    grade = item[4]
                    cls.submission_list.append(cls(student_idx, assignment_idx, date_of_submission, link, grade))
                else:
                    cls.submission_list.append(cls(student_idx, assignment_idx, date_of_submission, link))

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
        # new_submission = cls(student_idx, assignment_idx, date_of_submission, link)
        # if cls.submission_list:
        #     cls.submission_list.append(new_submission)
        if group == 0:
            members = [student_idx]
        else:
            members = cls.get_team_users(student_idx)

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

        # else:
        #     cls.group_submission(student_idx, assignment_idx, link, comment)

    @classmethod
    def group_submission(cls, student_idx, assignment_idx, link, comment):
        pass

    @staticmethod
    def get_team_users(student_idx):
        team_id = Team.find_student_team(student_idx)
        team_members = Team.get_team_members(team_id)
        clean_list = []
        for item in team_members:
            clean_list.append(item[0])
        return clean_list


    @classmethod
    def pass_submission_for_student(cls, student):
        """
        EEeee nie wiem w sumie po co to miało być.
        Może mnie potem oswieci.
        :param student:
        :return:
        """
        submission_for_student = []
        for submission in cls.submission_list:
            if submission.student_idx == student.idx:
                submission_for_student.append(submission)
        return submission_for_student

    @classmethod
    def find_submission(cls, student, assignment):
        """
        :param student: student object for whom we searching submitted assignment
        :param assignment: assignment object for which checking submission
        :return: submission object / False
        """
        submissions_list = cls.list_from_sql()
        for submission in submissions_list:
            if submission.student_idx == student.idx:
                if submission.assignment_idx == assignment.idx:
                    return submission
        return False

    @staticmethod
    def find_submission_sql(assignment_id, student_id):
        """
        :param student_id: logged student id
        :param assignment_id: assignment id
        :return: submission object / False
        """
        query = 'SELECT grade, `date` FROM sumbissions WHERE id_assigment=? AND id_student=?'
        params = [assignment_id, student_id]
        if sql.query(query, params):
            if sql.query(query, params)[0][0] == -1:
                grade = 'Not graded'
            else:
                grade = sql.query(query, params)[0][0]
            return [grade, sql.query(query, params)[0][1]]
        return False

    def change_grade(self, grade, mentor_id, student_id, assignment_id):
        """
        Changes grade of submission. Then saves to file.
        :param grade: int
        :return: None
        """
        self.grade = grade
        self.mentor_id = mentor_id
        #Common.save_file('csv/submission.csv', Submission.create_list_to_save())
        query = "UPDATE `Sumbissions` SET GRADE=?, ID_MENTOR=? WHERE ID_ASSIGMENT=? AND ID_STUDENT=?;"
        values_list = [int(grade), mentor_id, assignment_id, student_id]
        sql.query(query, values_list)