from models.ui import Ui
from models.ui import Color
from models.common import Common
from models import sql
import datetime
from models.student import Student


class Checkpoint:

    @staticmethod
    def add_checkpoint(user_object):

        Ui.clear()

        Ui.print_head('Add new checkpoint', 'header')

        title = Ui.get_input('Subject of checkpoint')
        while True:
            try:
                start_date = Common.make_corect_date(Ui.get_input('start date(YYYY-MM-DD)'))
                break
            except (IndexError, ValueError, UnboundLocalError):
                print('Wrong date format, try one more time.')

        query = "INSERT INTO Checkpoints ('ID_USER', 'TITLE', 'START_DATE') VALUES (?, ?, ?)"
        sql.query(query, [user_object.idx, title, start_date])

    @staticmethod
    def select_mentors_not_in_checkpoint(checkpoint_id):

        query = "SELECT * FROM Users WHERE `TYPE` = 'Mentor' AND `ID` NOT IN (SELECT ID_USER FROM Checkpoints WHERE ID={})".format(checkpoint_id)
        sql_result = sql.query(query)

        return sql_result

    @staticmethod
    def select_student_id_from_list(checkpoint_id):

        Ui.clear()
        Ui.print_head('Select student to checkpoint (not graded yet)', 'header')
        query = "SELECT * FROM Users  WHERE type='Student' and (SELECT count(ID) FROM Users_checkpoints " \
                "WHERE ID_STUDENT = Users.ID AND ID_CHECKPOINT = {}) = 0".format(checkpoint_id)

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
    def grade(student):

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

        checkpoint_id = Checkpoint.show_checkpoints()

        if checkpoint_id != 0:
            second_mentor_id = Checkpoint.select_mentor_id_from_list(user_object)

            while True:
                if second_mentor_id == None:
                    break
                student = Checkpoint.select_student_id_from_list(checkpoint_id)
                if student == None:
                    break

                student = Student.return_by_id(int(student))

                grade = Checkpoint.grade(student)

                if grade == 0:
                    break

                query = "INSERT INTO Users_checkpoints " \
                        "(ID_CHECKPOINT, DATE, GRADE, ID_STUDENT, ID_MENTOR_1, ID_MENTOR_2)" \
                        " VALUES (?, ?, ?, ?, ?, ?)"
                params = [checkpoint_id, today, grade, int(student.idx), int(user_object.idx), int(second_mentor_id)]
                sql.query(query, params)

                Ui.clear()
                Ui.print_head('Checkpoint', 'header')

                options = 'Select:\n\n' \
                          '\t1: Grade next student\n' \
                          '\t0: Exit Checkpoint '

                user_choice = Ui.get_menu(options, 0, 1)

                if user_choice == '0':
                    break

                if user_choice == '1':
                    pass

    @staticmethod
    def show_checkpoints():

        query = "SELECT * FROM Checkpoints, Users WHERE Checkpoints.ID_USER = Users.ID"
        titles = ['ID', 'Subject', 'Created by', 'Start date']

        sql_query_result = sql.query(query)
        return sql_query_result


    @staticmethod
    def show_checkpoint_results(checkpoint_id):
        if checkpoint_id != 0:
            Ui.clear()
            query = "SELECT TITLE, ID_CHECKPOINT, DATE, GRADE, student.Name as student_name,  " \
                    "student.Surname as student_surname , mentor.Name as mentor_name,  " \
                    "mentor.Surname as mentor_surname , mentor2.Name as mentor2_name,  " \
                    "mentor2.Surname as mentor2_surname " \
                    "FROM Users_checkpoints LEFT JOIN Users  student ON Users_checkpoints.ID_STUDENT = student.ID " \
                    "LEFT JOIN Users  mentor ON Users_checkpoints.ID_MENTOR_1 = mentor.ID " \
                    "LEFT JOIN Users  mentor2 ON Users_checkpoints.ID_MENTOR_2 = mentor2.ID " \
                    "LEFT JOIN Checkpoints ON Users_checkpoints.ID_CHECKPOINT = Checkpoints.ID " \
                    "WHERE ID_CHECKPOINT  = {}".format(checkpoint_id)

            table = []
            titles = ['Student', 'First mentor ', 'Second mentor', 'Date', Color.Yellow +'Grade       ' + Color.End]
            sql_query_result = sql.query(query)

            if isinstance(sql_query_result, list):

                for checkpoint in sql_query_result:
                    if checkpoint['grade'] == 'Yellow':
                        color = Color.Yellow
                    elif  checkpoint['grade'] == 'Red':
                        color = Color.Red
                    elif checkpoint['grade'] == 'Green':
                        color = Color.Green
                    table.append([checkpoint['student_name'] + ' '+  checkpoint['student_surname'],
                                  checkpoint['mentor_name'] + ' '+ checkpoint['mentor_surname'],
                                  checkpoint['mentor2_name'] + ' '+ checkpoint['mentor2_surname'],
                                  checkpoint['DATE'],
                                  color + checkpoint['grade'] + Color.End,

                                  ])

                Ui.print_head('Checkpoint title: {} (Date: {})'.format(sql_query_result[0]['TITLE'], sql_query_result[0]['DATE']))
                Ui.print_table(table, titles, 7)
                Ui.press_any_key_input()

            else:

                Ui.print_text('\n No results for this checkpoint yet! \n')

                Ui.press_any_key_input()

    @staticmethod

    def show_statistics_for_mentor_cards(id_mentor):

        query = "SELECT *, COUNT(GRADE) as cards FROM Users_checkpoints WHERE ID_MENTOR_1 = {} OR ID_MENTOR_2 = {} " \
                "GROUP BY grade".format(id_mentor, id_mentor)

        sql_query_result = sql.query(query)

        table = list()
        title = ['Grades', 'Amount']

        if isinstance(sql_query_result, list):
            for row in sql_query_result:
                table.append([row['GRADE'], row['cards']])
        else:
            table.append(['0', '0'])
        Ui.print_table(table, title)

    @staticmethod
    def show_statistics_for_mentor_checkpoints(id_mentor):

        query = "SELECT *FROM Checkpoints WHERE ID_USER = {} ORDER BY START_DATE ASC".format(
            id_mentor, id_mentor)

        sql_query_result = sql.query(query)

        table = list()
        title = ['My checkpoints', 'Date of creation']
        if isinstance(sql_query_result, list):
            for row in sql_query_result:
                table.append([row['TITLE'], row['START_DATE']])
            no = [str(len(sql_query_result))]
        else:
            table.append(['', ''])
            no = str(0)

        Ui.print_table(no, ['No of created checkpoints'])
        Ui.print_table(table, title)

    @staticmethod
    def show_statistics_for_mentor(id_mentor):

        Ui.print_head('Statistics of mentor', 'header')
        Checkpoint.show_statistics_for_mentor_cards(id_mentor)
        Checkpoint.show_statistics_for_mentor_checkpoints(id_mentor)
        Ui.press_any_key_input()

    def student_checkpoint(user_object):
        query = "SELECT * FROM USERS_CHECKPOINT WHERE ID_STUDENT=?"
        titles = ['Title', 'Grade', 'Date', 'Mentor_1', 'Mentor_2']
        values = [user_object.idx]
        user_checkpoints = []
        query_results = sql.query(query, values)
        if isinstance(query_results, list):
            for line in query_results:
                query = "SELECT title FROM Checkpoints WHERE ID=?"
                value = [line['ID_CHECKPOINT']]
                title = sql.query(query, value)[0][0]
                user_checkpoints.append([title, line['GRADE'], line['DATE'], line['ID_MENTOR_1'],
                                        line['ID_MENTOR_2']])
        Ui.print_table(user_checkpoints, titles)



