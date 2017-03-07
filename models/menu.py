from models.ui import Ui
from models.user import User
from models.manager import Manager
from models.student import Student
from models.mentor import Mentor
from models.employee import Employee
from models.common import Common
from models.assignment import Assignment
from models.submission import Submission
from models.attandance import Attendance
from datetime import date
from models.test import Test
from models.checkpoint import Checkpoint
from models.team import Team
import models.sql


class Menu:

    @staticmethod
    def add_user(class_name):
        """
        add new user to class
        :param class_name:  string (name of class where new user should be created)
        :return: None
        """
        label_list = ['Name', 'Last Name', 'E-mail', 'Phone Number']
        user_data = Ui.get_inputs(label_list)
        user_data = Test.test_add_arguments(label_list, user_data)
        Menu.where_to_add(class_name, user_data)

    @staticmethod
    def print_user(object_list):
        """
        Display passed list
        :param object_list: list ( list to display)
        :return: None
        """
        Ui.clear()
        print_list = []
        for user in User.create_list_to_save(object_list):
            print_list.append([user[0], user[1], user[2], user[3], user[4]])
        Ui.print_table(print_list,
                       ['Id', 'Name', 'Last Name', 'E-mail', 'Telephone'])
        # Ui.get_inputs(['Enter anything to leave: '])

    @staticmethod
    def edit_user(class_name):
        """My submissions
        Edit user
        :param class_name: string ( name of class where user should be edited)
        :return: None
        """
        edit_arguments_list = Ui.get_inputs(['Mail of user to edit: ',
                                             'What to edit (Name,Surname,E-mail,Telephone,Password): ',
                                             'new value: '])
        while True:
            if Test.is_email_correct(edit_arguments_list[0]):
                break
            else:
                edit_arguments_list[0] = Ui.get_input('Wrong mail format')
        edit_arguments_list[1] = Test.test_edit_user(edit_arguments_list[1])
        edit_arguments_list[2] = Test.check_argument(edit_arguments_list[1], edit_arguments_list[2])
        Menu.where_to_edit(class_name, edit_arguments_list)
        Ui.get_input('ENTER')

    @staticmethod
    def checkpoint(user_object):
        """
        Checkpoint:
        :param None
        :return: None
        """

        while True:
            Ui.clear()
            Menu.logged_as(user_object)
            Ui.print_head('Checkpoints ', 'header')

            options = '\t1: Show checkpoints\n' \
                      '\t2: Add new checkpoint\n' \
                      '\t3: Make checkpoint\n' \
                      '\t0: Previous Menu'

            user_choice = Ui.get_menu(options, 0, 3)

            if user_choice == '1':

                Checkpoint.show_checkpoint_results(Checkpoint.show_checkpoints())

            if user_choice == '2':

                Checkpoint.add_checkpoint(user_object)

            if user_choice == '3':

                Checkpoint.make_checkpoint(user_object)

            if user_choice == '0':
                break

    @staticmethod
    def remove_user(class_name):
        """
        Remove user from list
        :param class_name: string ( name of class where user should be removed)
        :return: None
        """
        mail = Ui.get_inputs(['Enter user\'s e-mail to remove him : '])
        if Menu.where_to_remove(class_name, mail[0]):
            Ui.print_text('User removed')
            Ui.get_inputs(['Enter to continue: '])
        else:
            Ui.print_text('No user of passed mail')
            Ui.get_inputs(['Enter to continue: '])

    @staticmethod
    def where_to_edit(class_name, edit_arguments_list):
        """
        Check which class should edit user
        :param class_name: string (name of class that method should be started)
        :param edit_arguments_list: (FORMAT: E-MAIL, ATTRIBUTE, NEW VALUE)
        :return: None
        """
        if class_name == 'Student':
            if Student.edit_user(edit_arguments_list):
                Ui.print_text('Student edited')
            else:
                Ui.print_text('No user of passed E-mail')
        elif class_name == 'Mentor':
            if Mentor.edit_user(edit_arguments_list):
                Ui.print_text('Mentor edited')
            else:
                Ui.print_text('No user of passed E-mail')
        elif class_name == 'Manager':
            if Manager.edit_user(edit_arguments_list):
                Ui.print_text('Manager edited')
            else:
                Ui.print_text('No user of passed E-mail')
        elif class_name == 'Employee':
            if Employee.edit_user(edit_arguments_list):
                Ui.print_text('Student edited')
            else:
                Ui.print_text('No user of passed E-mail')

    @staticmethod
    def where_to_remove(class_name, mail):
        """
        Check which class should remove user
        :param class_name: string (name of class that method should be started)
        :param mail: string ( mail of user to remove)
        :return: True or None
        """
        if class_name == 'Student':
            return Student.remove_object(mail)
        elif class_name == 'Mentor':
            return Mentor.remove_object(mail)
        elif class_name == 'Manager':
            return Manager.remove_object(mail)
        elif class_name == 'Employee':
            return Employee.remove_object(mail)

    @staticmethod
    def where_to_add(class_name, user_data):
        """
        Check witch class should add user
        :param class_name: string ( name of class that user should be add)
        :param user_data: list ( FORMAT: NAME, SURNAME, E-MAIL, TELEPHONE)
        :return: None
        """
        if class_name == 'Student':
            Student.add_user(user_data)
        elif class_name == 'Mentor':
            Mentor.add_user(user_data)
        elif class_name == 'Manager':
            Manager.add_user(user_data)
        elif class_name == 'Employee':
            Employee.add_user(user_data)

    @staticmethod
    def student_statistic():
        """
        Display  statistics of students
        :return: None
        """
        Ui.clear()
        options = '\t1: AVG GRADE\n' \
                  '\t2: Attendance\n' \
                  '\t0: Back to menu'

        user_choice = Ui.get_menu(options, 0, 2)
        if user_choice == '1':
            Ui.clear()
            title_list = ['Name', 'Surname', 'AVG GRADE']
            Ui.print_table(Student.avg_grade(), title_list)
            Ui.get_inputs(['Enter anything to leave: '])
        if user_choice == '2':
            Ui.clear()
            titles = ['Name', 'Last name', 'Present', 'Late', 'Absent']
            Ui.print_table(Attendance.students_engagement(), titles)
            Ui.get_inputs(['Enter anything to leave: '])
        else:
            pass

    @staticmethod
    def logged_as(logged_user):
        """
        Prints logged user at the top of the window
        :param logged_user:
        :return: None
        """
        Ui.print_head('Logged as {} {}'.format(logged_user.name, logged_user.last_name, 'header'))

    @staticmethod
    def run():
        """
        Starts program. Creates a list with objects.
        It allows the user to log in to the program.
        :return: None
        """

        logged_user = User.login()

        Team.create_teams_list()
        Student.create_object_list()
        Mentor.create_object_list()
        Employee.create_object_list()
        Manager.create_object_list()
        #Assignment.create_assignment_list()
        #Submission.create_submission_list()
        Attendance.create_attendance_list()
        Submission.list_from_sql()
        Assignment.list_from_sql()

        args = [logged_user['ID'], logged_user['Name'], logged_user['Surname'],
                logged_user['E-mail'], logged_user['Telephone'], logged_user['Password']]

        if logged_user['Type'] == 'Student':
            user = Student.return_by_id(logged_user['ID'])
            StudentMenu.print_menu(user)

        if logged_user['Type'] == 'Mentor':
            user = Mentor(*args)
            MentorMenu.print_menu(user)

        if logged_user['Type'] == 'Manager':
            user = Manager(*args)
            ManagerMenu.print_menu(user)

        if logged_user['Type'] == 'Employee':
            user = Employee(*args)
            EmployeeMenu.print_menu(user)


class StudentMenu(Menu):

    # @classmethod
    # def print_menu(cls, user_object):
    #     """
    #     Prints menu with options for student.
    #     :param user_object: object of one of user's subclass
    #     :return:
    #     """
    #     while True:
    #         Ui.clear()
    #         Menu.logged_as(user_object)
    #         Ui.print_head('Student menu:', 'header')
    #
    #         options = '\t1: Show assignment list with grades\n' \
    #                   '\t2: Show assignment description\n' \
    #                   '\t3: Submit assignment\n' \
    #                   '\t4: Show my submission list \n' \
    #                   '\t5: Show my overall attendance \n' \
    #                   '\t0: Exit program'
    #
    #         user_choice = Ui.get_menu(options, 0, 6)
    #         cls.choose_option(user_choice, user_object)

    # @classmethod
    # def choose_option(cls, choice, logged_user):
    #     """
    #     Creates action for option, which was chosen.
    #     :param choice: str - users choice
    #     :param logged_user: user object
    #     :return:
    #     """
    #
    #     students_assignments = Assignment.pass_assign_for_student()
    #
    #     if choice == '1':
    #         cls.get_assignment_list_with_grades(logged_user)
    #         input('Enter to back to menu')
    #     elif choice == '2':
    #         cls.assignment_description()
    #         input('Enter to back to menu')
    #     elif choice == '3':
    #         cls.student_makes_submission(logged_user, students_assignments)
    #         input('Enter to back to menu')
    #     elif choice == '4':
    #         cls.my_subbmisions(logged_user)
    #         input('Enter to back to menu')
    #     elif choice == '5':
    #         cls.my_attendance(logged_user)
    #         input('Enter to back to menu')
    #     elif choice == '0':
    #         exit()

    # @staticmethod
    # def get_assignment_list_with_grades(logged_user):
    #     """
    #     Makes list with assignments visible for student with notation if assignment was submitted
    #     and how it was graded.
    #     :param logged_user: (user object)
    #     :return: assignments_list_to_print
    #     """
    #     Ui.clear()
    #     Ui.print_head("{} {}'s assignments with grades".format(logged_user.name, logged_user.last_name), 'header')
    #     title_list = ['nr', 'title', 'mentor_id', 'start date', 'end date', 'type of assignment', 'submitted', 'grade']
    #     assignments_list = Assignment.pass_assign_for_student()
    #     assignments_list_to_print = []
    #     n = 1
    #     for assignment in assignments_list:
    #         type_of_assignment = 'Individual'
    #         if assignment.group == '1':
    #             type_of_assignment = 'Group'
    #         new_line = [str(n), assignment.title, assignment.mentor_id, assignment.start_date, assignment.end_date, type_of_assignment]
    #         submission = Submission.find_submission(logged_user, assignment)
    #         if submission:
    #             new_line.append('submitted')
    #             if submission.grade:
    #                 new_line.append(submission.grade)
    #             else:
    #                 new_line.append('None')
    #         else:
    #             new_line.append('not submitted')
    #             new_line.append('None')
    #         assignments_list_to_print.append(new_line)
    #         n += 1
    #     Ui.print_table(assignments_list_to_print, title_list)
    #
    #     return assignments_list_to_print

    @staticmethod
    def assignment_list_with_grades(logged_user):
        """
        Makes list with assignments visible for student with notation if assignment was submitted
        and how it was graded.
        :param logged_user: (user object)
        :return: assignments_list_to_print
        """
        Assignment.list_from_sql()
        assignments_list = Assignment.pass_assign_for_student()
        Submission.list_from_sql()
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


    @staticmethod
    def assignment_description():
        """
        Prints description of a chosen assignment
        :return:
        """

        Ui.clear()
        Ui.print_head("List of assignments", "header")
        assignments_list = Assignment.pass_assign_for_student()
        assignments_list_to_print = []
        n = 1
        for assignment in assignments_list:
            assignments_list_to_print.append([str(n), assignment.title, str(assignment.start_date),
                                              str(assignment.end_date)])
            n += 1
        Ui.print_table(assignments_list_to_print, ['nr', 'title', 'start date', 'end date'])
        n = len(assignments_list)
        Ui.print_text("Choose number of assignment you want read, 0 for exit")
        user_choice = int(Ui.get_menu('', 0, n))
        if user_choice == 0:
            return None
        else:
            Ui.clear()
            description = assignments_list[user_choice - 1].assignment_description()
        Ui.print_head("Description", "header")
        Ui.print_text(description)

    @classmethod
    def student_makes_submission(cls, logged_user, students_assignments):
        """
        Makes submission of chosen assignment.
        :param logged_user: user object
        :param students_assignments: assignment object
        :return:
        """
        Ui.clear()
        list_to_submit = cls.get_assignment_list_with_grades(logged_user)
        n = len(list_to_submit)
        Ui.print_text("Choose number of assignment you want to submit")
        user_choice = int(Ui.get_menu('', 0, n))
        assignment_to_submit = students_assignments[user_choice - 1]
        if assignment_to_submit.group == '0':
            if not Submission.find_submission(logged_user, assignment_to_submit):
                link = Ui.get_inputs(['Link to your repo:'])
                Submission.add_submission(logged_user.idx, assignment_to_submit.idx, date.today(), link[0])
            else:
                Ui.print_text("You can't submit this assignment - it's already submitted")
        else:
            cls.submission_for_group(logged_user, assignment_to_submit)

    @staticmethod
    def submission_for_group(logged_user, assignment_to_submit):
        team_id = logged_user.id_team
        if team_id:
            link = Ui.get_inputs(['Link to your repo:'])
            team = Team.get_by_id(team_id)
            for student_id in team.students_id:
                student = Student.return_by_id(student_id)
                if not Submission.find_submission(student, assignment_to_submit):
                    Submission.add_submission(student_id, assignment_to_submit.idx, date.today(), link[0])
                else:
                    Ui.print_text("You can't submit this assignment - it's already submitted")
        else:
            Ui.print_text("You can't submit this assignment - you are not in team")

    @staticmethod
    def my_subbmisions(logged_user):
        """
        Prints only submitted assignments with date of submission and link to repo.
        :param logged_user: user object.
        :return:
        """
        Ui.clear()
        Ui.print_head("My submissions", "header")
        logged_user_submission = Submission.pass_submission_for_student(logged_user)
        logged_user_submission_to_print = []
        for sub in logged_user_submission:
            assignment = Assignment.get_by_id(sub.assignment_idx)
            logged_user_submission_to_print.append([assignment.title, assignment.start_date, assignment.end_date,
                                                   str(sub.date_of_submission), sub.link, sub.grade, sub.mentor_id])
        Ui.print_table(logged_user_submission_to_print, ['title', 'start date', 'end date', 'submission date',                                                 'link to repo', 'grade', 'mentor_id'])

    @staticmethod
    def my_attendance(user):
        query = 'SELECT STATUS, COUNT(STATUS) AS count FROM `Attendance` WHERE ID_STUDENT=? GROUP BY STATUS'
        values = [user.idx]
        back_values = sql.query(query, values)
        to_print =[]
        all_days = 0
        average = 0
        for row in back_values:
            to_print.append([row[0], row[1]])
            if row[0] == 'Present':
                average += 1
            elif row[0] == 'Late':
                average += 0.75
            all_days += row[1]

        to_print.append(['overall %', average * 100 / all_days])
        Ui.print_table(to_print, ['Status', 'amount'])

    @staticmethod
    def my_checkpoints(user):
        Checkpoint.student_checkpoint(user)


class MentorMenu(Menu):

    @classmethod
    def print_menu(cls, user_object):
        """
        Display menu to user
        :param user_object: object ( object contain logged user)
        :return: None
        """
        while True:
            Ui.clear()
            Menu.logged_as(user_object)
            Ui.print_head('Mentor menu:', 'header')

            options = '\t1: Show students\n' \
                      '\t2: Add assignment\n' \
                      '\t3: Grade submission\n' \
                      '\t4: Show attendance\n' \
                      '\t5: Check attendance of students\n' \
                      '\t6: Add student\n' \
                      '\t7: Remove student\n' \
                      '\t8: Edit student\n' \
                      '\t9: Checkpoints\n' \
                      '\t10: Show teams\n' \
                      '\t11: Create team\n' \
                      '\t12: Add student to team\n' \
                      '\t13: Statistics\n' \
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 13)

            cls.choose_option(user_choice, user_object)

    @classmethod
    def choose_option(cls, choice, user_object):
        """
        Checks which option was selected by user and run assigned method
        :param choice: string ( user input)
        :param user_object: User object (logged user)
        :return: None
        """
        if choice == '1':
            cls.print_user(Student.object_list)
            Ui.get_input('ENTER')

        elif choice == '2':
            cls.add_assignment(user_object)
            Ui.get_input('ENTER')

        elif choice == '3':
            Ui.clear()
            cls.grade_submission(user_object)

        elif choice == '4':
            Ui.clear()
            cls.show_attendance_of_students()
            Ui.get_input('ENTER')

        elif choice == '5':
            cls.switch_attendance()

        elif choice == '6':
            cls.add_user('Student')

        elif choice == '7':
            cls.remove_user('Student')

        elif choice == '8':
            cls.edit_user('Student')

        elif choice == '9':
            cls.checkpoint(user_object)

        elif choice == '10':
            cls.show_teams()
            Ui.get_input('ENTER')

        elif choice == '11':
            cls.add_new_team()
            Ui.get_input('ENTER')

        elif choice == '12':
            cls.add_student_to_team()

        elif choice == '13':

            Ui.clear()
            Checkpoint.show_statistics_for_mentor(user_object.idx)

        elif choice == '0':
            exit()

    @classmethod
    def add_student_to_team(cls):
        """
        Lets user to move student between teams
        :return: None
        """
        cls.print_user(Student.object_list)
        option = 'id student\'s which you want to add to team?'
        student_id = Ui.get_input(option)
        student = Student.return_by_id(int(student_id))

        if student:
            cls.show_teams()
            option = 'id team\'s where you want to add student?'
            team_id = Ui.get_input(option)
            team = Team.get_team_by_id(team_id)
            if team:
                Team.student_to_team(team, student)
                student_fullname = student.name + ' ' + student.last_name
                Ui.print_text('\n---::: You added {} to team {} :::---'.format(student_fullname, team.name))
                Ui.get_input('ENTER')
            else:
                Ui.print_text('There is no team with this ID')
                Ui.get_input('ENTER')
        else:
            Ui.print_text('There is no student of this ID')
            Ui.get_input('ENTER')

    @classmethod
    def add_new_team(cls):
        """
        Adds new team
        :return: None
        """
        label_list = ['Name']
        user_data = Ui.get_inputs(label_list)
        name = user_data[0]
        if name == '' or '\t' in name or len(name) < 3 or name[0] == ' ' or '  ' in name:

            Ui.print_text('Wrong name format')

            return

        Team.new_team(name)
        Ui.print_head('You created a new team called: {}'.format(name), 'warning')

    @staticmethod
    def show_teams():
        """
        Prints all teams with students
        :return: None
        """
        for team in Team.teams_list:
            titles = ['ID: {}'.format(team.id_team), 'Team: {}'.format(team.name)]
            students = []
            student_nr = 1
            for student_id in team.students_id:
                for student in Student.object_list:
                    if student.idx == student_id:
                        students.append([student_nr, student.name + ' ' + student.last_name])
                        student_nr += 1
                        break
            Ui.print_table(students, titles)

    @staticmethod
    def show_attendance_of_students():
        """
        Prints students in table with their presences
        :return:None
        """
        titles = ['Name', 'Last name', 'Present', 'Late', 'Absent']
        engagement_list = Attendance.students_engagement()
        Ui.print_table(engagement_list, titles)

    @classmethod
    def grade_submission(cls, mentor_user):
        """
        It enables assessment tasks
        :return:None
        """
        titles = ['Nr', 'Student\'s e-mail', 'Assignment title', 'Date of submission', 'Grade', 'Mentor_id']
        grades_list = []
        assignment_list = []  # need to check if submission is group
        n = 1

        for submission in Submission.submission_list:
            student = Student.return_by_id(submission.student_idx)

            if student:
                assignment = Assignment.get_by_id(submission.assignment_idx)
                grades_list.append([str(n), student.mail, assignment.title, str(submission.date_of_submission),
                                    str(submission.grade), submission.mentor_id])
                assignment_list.append(assignment)
                print(n)
                n += 1

        Ui.print_table(grades_list, titles)
        options = 'Choose number of submission to grade'
        user_choice = int(Ui.get_menu(options, 1, n))
        submission_to_grade = Submission.submission_list[user_choice - 1]
        new_grade = Ui.get_inputs(['New grade:'])[0]
        assignment = assignment_list[user_choice - 1]
        if assignment_list[user_choice - 1].group == "1":
            cls.grade_group_submission(mentor_user, submission_to_grade, new_grade, assignment)
        else:
            submission_to_grade.change_grade(new_grade, mentor_user.idx, submission_to_grade.student_idx,
                                            submission_to_grade.assignment_idx)

    @staticmethod
    def grade_group_submission(mentor_user, submission_to_grade, grade, assignment):
        student = Student.return_by_id(submission_to_grade.student_idx)
        team_id = student.id_team
        team = Team.get_by_id(team_id)
        assignment_idx = submission_to_grade.assignment_idx
        for student_id in team.students_id:
            student_from_team = Student.return_by_id(student_id)
            sub_to_grade = Submission.find_submission(student_from_team, assignment)
            #if Submission.find_submission(student_from_team, assignment_idx):
            sub_to_grade.change_grade(grade, mentor_user.idx, student_id, assignment_idx)


    @staticmethod
    def add_assignment(user_object):
        """
        Adds new assignment
        :param user_object: User object (The currently logged in user)
        :return: None
        """
        mentor_id = user_object.idx #user_object.name + ' ' + user_object.last_name
        title = ''
        while not title or '\t' in title or title == ' ':
            title = Ui.get_input('title (cannot be empty)')
        while True:
            try:
                start_date = Common.make_corect_date(Ui.get_input('start date(YYYY-MM-DD)'))
                break
            except (IndexError, ValueError, UnboundLocalError):
                print('Wrong date format, try one more time.')
        while True:
            try:
                end_date = Common.make_corect_date(Ui.get_input('end date(YYYY-MM-DD)'))
                break
            except (IndexError, ValueError, UnboundLocalError):
                print('Wrong date format, try one more time.')

        group = Ui.get_input('If assignment is for group type 1, else enter: ')
        filename_from_title = '_'.join(title.split(' '))
        filename = 'csv/assignments_description/{}.txt'.format(filename_from_title)
        filename_short = '{}.txt'.format(filename_from_title)

        with open(filename, 'w'):
            Ui.print_text('File is created')
        if group == '1':
            Assignment.add_assignment(title, mentor_id, start_date, end_date, filename_short, '1')
        else:
            Assignment.add_assignment(title, mentor_id, start_date, end_date, filename_short)

    @staticmethod
    def switch_attendance():
        """
        Sets the state of the presence each student at today
        :return: None
        """
        Attendance.create_new_day()
        for student in Attendance.attendance_list:
            Ui.clear()
            if student.date == str(date.today()):

                student_data = sql.query('SELECT * FROM `Users` WHERE ID={}'.format(student.id_student))
                Ui.print_head(student_data[0]['Name'] + ' ' + student_data[0]['Surname'], 'warning')
                text = 'Is this student present today?\n(1: Present, 2: Late, 3: Absent):  '
                mentor_choice = Ui.get_menu(text, 1, 3)

                Attendance.toggle_present(student, mentor_choice)
                query = "UPDATE `Attendance` SET `STATUS` = '{}' WHERE `ID_STUDENT` = {} AND `DATE` = '{}';"\
                        .format(student.present, student.id_student, student.date)

                sql.query(query)


class EmployeeMenu(Menu):
    @staticmethod
    def print_menu(user_object):
        """
        Display menu to user
        :param user_object: object ( object contain logged user)
        :return: None
        """
        while True:
            Ui.clear()
            Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))
            options = '\t1: Show students\n' \
                      '\t0: Exit program'
            user_choice = Ui.get_menu(options, 0, 1)
            EmployeeMenu.choose_option(user_choice)

    @staticmethod
    def choose_option(choice):
        """
        Check witch option was chosen by user and run assigned method
        :param choice: string (user input)
        :return: None
        """
        if choice == '1':
            EmployeeMenu.print_user(Student.object_list)
            Ui.get_input('ENTER')

        elif choice == '0':
            exit()


class ManagerMenu(Menu):

    @staticmethod
    def print_menu(user_object):
        """
        Display menu to user
        :param user_object: object ( object contain logged user)
        :return: None
        """
        while True:
            Ui.clear()
            Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))
            Ui.print_head('Manager menu:', 'header')
            options = '\t1: Add mentor\n' \
                      '\t2: Show mentor list\n' \
                      '\t3: Remove mentor\n' \
                      '\t4: Add student\n' \
                      '\t5: Show student\n' \
                      '\t6: Edit Mentor\n' \
                      '\t7: Display Student statistic\n' \
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 7)

            ManagerMenu.choose_option(user_choice)

    @staticmethod
    def choose_option(choice):
        """
        Check witch option was chosen by user and run assigned method
        :param choice: string (user input)
        :return: None
        """
        if choice == '1':
            Ui.clear()
            ManagerMenu.add_user('Mentor')
        elif choice == '2':
            ManagerMenu.print_user(Mentor.object_list)
            Ui.get_input('ENTER')
            Ui.clear()

        elif choice == '3':
            Ui.clear()
            ManagerMenu.remove_user('Mentor')
        elif choice == '4':
            Ui.clear()
            ManagerMenu.add_user('Student')
        elif choice == '5':
            Ui.clear()
            ManagerMenu.print_user(Student.object_list)
            Ui.get_input('ENTER')

        elif choice == '6':
            Ui.clear()
            ManagerMenu.edit_user('Mentor')
        elif choice == '7':
            ManagerMenu.student_statistic()
        else:
            exit()
