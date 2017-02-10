from ui import Ui
from common import Common
import sql
import datetime
from student import Student

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

        Ui.clear()
        checkpoint_ids = Checkpoint.show_checkpoints(user_object)

        return Ui.get_id_only_in_list('Select checkpoint (ID): ', checkpoint_ids)

    @staticmethod
    def select_mentor_id_from_list():

        Ui.clear()
        Ui.print_head('Select second mentor', 'header')
        query = "SELECT * FROM Users WHERE `TYPE` = 'Mentor'"
        mentors = []
        mentors_ids = []
        for mentor in sql.query(query):
            mentors.append([mentor['ID'], mentor['SURNAME'], mentor['NAME'], ])
            mentors_ids.append(mentor['ID'])

        Ui.print_table(mentors, ['ID', 'Surname', 'Name'])

        return Ui.get_id_only_in_list('Select second mentor (ID): ', mentors_ids)

    @staticmethod
    def select_student_id_from_list(checkpoint_id):

        Ui.clear()
        Ui.print_head('Select student to checkpoint (not graded yet)', 'header')
        query = "SELECT * FROM Users  WHERE type='Student' and (SELECT count(ID) FROM Users_checkpoints WHERE ID_STUDENT = Users.ID AND ID_CHECKPOINT = {}) = 0".format(checkpoint_id)

        students = []
        students_ids = []

        query_result = sql.query(query)

        if isinstance(query_result, list):
            for student in query_result:
                students.append([student['ID'], student['SURNAME'], student['NAME'], ])
                students_ids.append(student['ID'])

            Ui.print_table(students, ['ID', 'Surname', 'Name'])
            return Ui.get_id_only_in_list('Select student (ID): ', students_ids)

        else:
            Ui.print_text('\n All students are graded in this checkpoint! \n')
            Ui.press_any_key_input()
            return None


    @staticmethod
    def grade(user_object, student):

        Ui.clear()
        Ui.print_head('Grade', 'header')
        Ui.print_head('{} You are grading {} {}'.format('Mentor! ', student.name, student.last_name))
        options = 'Your grade for this student:\n\n' \
                  '\t1: Green card\n' \
                  '\t2: Yellow card\n' \
                  '\t3: Red card\n' \
                  '\t0: Cancel '

        user_choice = Ui.get_menu(options, 0, 3)

        if user_choice == '1':
            return 'Green'
        elif user_choice == '2':
            return 'Yellow'
        elif user_choice == '3':
            return 'Red'
        elif user_choice == '0':
            return 0

    @staticmethod
    def make_checkpoint(user_object):

        Ui.clear()
        Ui.print_head('Make checkpoint', 'header')

        today = datetime.date.today()

        first_mentor_id = user_object.idx

        checkpoint_id = Checkpoint.select_checkpoint_id_from_list(user_object)
        second_mentor_id = Checkpoint.select_mentor_id_from_list()

        while True:

            student = Checkpoint.select_student_id_from_list(checkpoint_id)
            if student == None:
                break

            student = Student.return_by_id(int(student))


            grade = Checkpoint.grade(user_object, student)

            Ui.clear()
            Ui.print_head('Checkpoint', 'header')

            options = 'Select:\n\n' \
                      '\t1: Grade next student\n' \
                      '\t0: Exit Checkpoint '

            user_choice = Ui.get_menu(options, 0, 1)

            if user_choice == '0':
                break

            if user_choice == '1':
                query = "INSERT INTO Users_checkpoints (ID_CHECKPOINT, DATE, GRADE, ID_STUDENT, ID_MENTOR_1, ID_MENTOR_2) VALUES (?, ?, ?, ?, ?, ?)"
                params = [checkpoint_id, today, grade, int(student.idx), int(user_object.idx), int(second_mentor_id)]
                sql.query(query, params)

    @staticmethod
    def show_checkpoints(user_object):
        Ui.clear()

        Ui.print_head('Created checkpoints', 'header')
        query = "SELECT * FROM Checkpoints, Users WHERE Checkpoints.ID_USER == Users.ID"
        titles = ['ID', 'Subject', 'Created by', 'Start date']
        checkpoints = []
        sql_query_result = sql.query(query)
        ids = []
        if isinstance(sql_query_result, list):
            for checkpoint in sql_query_result:
                checkpoints.append([checkpoint['ID'], checkpoint['TITLE'], checkpoint['NAME'] + checkpoint['SURNAME'], checkpoint['START_DATE']])
                ids.append(checkpoint["ID"])
            Ui.print_table(checkpoints, titles)
        else:
            Ui.print_text('\n Create checkpoints first! \n')

        return ids



