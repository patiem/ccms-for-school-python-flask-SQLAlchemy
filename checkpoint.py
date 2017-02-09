from ui import Ui
from common import Common
import sql
import datetime


class Checkpoint:

    @staticmethod
    def add_checkpoint(user_object):

        Ui.clear()

        Ui.print_head('Add new checkpoint', 'header')

        title = Ui.get_input('Subject of checkpoint')
        start_date = Common.make_corect_date(Ui.get_input('start date(YYYY-MM-DD)'))
        today = datetime.date.today()

        query = "INSERT INTO Checkpoints ('ID_USER', 'TITLE', 'START_DATE') VALUES (?, ?, ?)"
        sql.query(query, [user_object.idx, title, start_date])

    @staticmethod
    def select_checkpoint_id_from_list(user_object):

        checkpoint_ids = Checkpoint.show_checkpoints(user_object)
        choose = 0

        while int(choose) not in checkpoint_ids:
            choose = Ui.get_input('Select checkpoint (ID)')

        return choose

    @staticmethod
    def select_mentor_id_from_list():

        Ui.print_head('Select second mentor', '')
        query = "SELECT * FROM Users WHERE `TYPE` = 'Mentor'"
        mentors = []
        ids = []
        for mentor in sql.query(query):
            mentors.append([mentor['ID'], mentor['SURNAME'], mentor['NAME'], ])
            ids.append(mentor['ID'])

        Ui.print_table(mentors, ['ID', 'Surname', 'Name'])

        choose = 0
        while int(choose) not in ids:
            choose = Ui.get_input('Second mentor (ID)')

        return choose

    @staticmethod
    def select_student_id_from_list():

        Ui.print_head('Select student to checkpoint', '')
        query = "SELECT * FROM Users WHERE `TYPE` = 'Student'"
        students = []
        ids = []
        for student in sql.query(query):
            students.append([student['ID'], student['SURNAME'], student['NAME'], ])
            ids.append(student['ID'])

        Ui.print_table(students, ['ID', 'Surname', 'Name'])
        choose = 0
        while int(choose) not in ids:
            choose = Ui.get_input('Select student (ID)')

        return choose

    @staticmethod
    def make_checkpoint(user_object):

        Ui.clear()
        Ui.print_head('Make checkpoint', 'header')

        today = datetime.date.today()
        first_mentor_id = user_object.idx

        checkpoint_id = Checkpoint.select_checkpoint_id_from_list(user_object)
        second_mentor_id = Checkpoint.select_mentor_id_from_list()
        student_id = Checkpoint.select_student_id_from_list()

        input()


    @staticmethod
    def show_checkpoints(user_object):
        Ui.clear()

        Ui.print_head('Created checkpoints', 'header')

        query = "SELECT * FROM Checkpoints, Users WHERE Checkpoints.ID_USER == Users.ID"
        titles = ['ID', 'Subject', 'Created by', 'Start date']
        checkpoints = []
        sql_query_result =  sql.query(query)
        ids = []
        if isinstance(sql_query_result, list):
            for checkpoint in sql_query_result:
                checkpoints.append([checkpoint['ID'], checkpoint['TITLE'], checkpoint['NAME'] + checkpoint['SURNAME'], checkpoint['START_DATE']])
                ids.append(checkpoint["ID"])
            Ui.print_table(checkpoints, titles)
        else:
            Ui.print_text('\n Create checkpoints first! \n')

        return ids

    @staticmethod
    def show_checkpoint_by_id(ID):

        pass


