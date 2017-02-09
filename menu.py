from ui import Ui
from user import User
from manager import Manager
from student import Student
from mentor import Mentor
from employee import Employee
from common import Common
from assignment import Assignment
from submission import Submission
from attandance import Attendance
from datetime import date
from test import Test


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
        Menu.what_save(class_name)

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
        Ui.get_inputs(['Enter anything to leave: '])

    @staticmethod
    def edit_user(class_name):
        """
        Edit user
        :param class_name: string ( name of class where user should be edited)
        :return: None
        """
        edit_arguments_list = Ui.get_inputs(['Mail of user to edit: ',
                                             'what to edit (name,last name,e-mail,telephone,password): ',
                                             'new value: '])
        edit_arguments_list[1] = Test.test_edit_user(edit_arguments_list[1])
        edit_arguments_list[2] = Test.check_argument(edit_arguments_list[1], edit_arguments_list[2])
        Menu.where_to_edit(class_name, edit_arguments_list)
        Menu.what_save(class_name)

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
        Menu.what_save(class_name)

    @staticmethod
    def where_to_edit(class_name, edit_arguments_list):
        """
        Check which class should edit user
        :param class_name: string (name of class that method should be started)
        :param edit_arguments_list: ( list of arguments to run run method)
        :return: None
        """
        if class_name == 'Student':
            Student.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])
        elif class_name == 'Mentor':
            Mentor.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])
        elif class_name == 'Manager':
            Manager.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])
        elif class_name == 'Employee':
            Employee.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])

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
    def what_save(class_name):
        """
        Check which class list should be saved
        :param class_name: string ( name of class that list should be saved)
        :return: None
        """
        if class_name == 'Student':
            Common.save_file(Student.file, Student.create_list_to_save(Student.object_list))
        elif class_name == 'Mentor':
            Common.save_file(Mentor.file, Mentor.create_list_to_save(Mentor.object_list))
        elif class_name == 'Manager':
            Common.save_file(Manager.file, Manager.create_list_to_save(Manager.object_list))
        elif class_name == 'Employee':
            Common.save_file(Employee.file, Employee.create_list_to_save(Employee.object_list))

    @staticmethod
    def where_to_add(class_name, user_data):
        """
        Check witch class should add user
        :param class_name: string ( name of class that user should be add)
        :param user_data: list ( list of attributes to create user)
        :return: None
        """
        if class_name == 'Student':
            Student.add_user(user_data[0], user_data[1], user_data[2], user_data[3])
        elif class_name == 'Mentor':
            Mentor.add_user(user_data[0], user_data[1], user_data[2], user_data[3])
        elif class_name == 'Manager':
            Manager.add_user(user_data[0], user_data[1], user_data[2], user_data[3])
        elif class_name == 'Employee':
            Employee.add_user(user_data[0], user_data[1], user_data[2], user_data[3])

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
            user = Student(*args)
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

    @classmethod
    def print_menu(cls, user_object):
        """
        Prints menu with options for student.
        :param user_object: object of one of user's subclass
        :return:
        """
        while True:
            Ui.clear()
            Menu.logged_as(user_object)
            Ui.print_head('Student menu:', 'header')

            options = '\t1: Show assignment list with grades\n' \
                      '\t2: Show assignment description\n' \
                      '\t3: Submit assignment\n' \
                      '\t4: Show my submission list \n' \
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 4)
            cls.choose_option(user_choice, user_object)

    @classmethod
    def choose_option(cls, choice, logged_user):
        """
        Creates action for option, which was chosen.
        :param choice: str - users choice
        :param logged_user: user object
        :return:
        """
        # if not Assignment.assigments_list:
        #     Assignment.list_from_sql()
        # print(Submission.submission_list)
        # if not Submission.submission_list:
        #     Submission.list_from_sql()

        students_assignments = Assignment.pass_assign_for_student()

        if choice == '1':
            cls.get_assignment_list_with_grades(logged_user)
            input('Enter to back to menu')
        elif choice == '2':
            cls.assignment_description()
            input('Enter to back to menu')
        elif choice == '3':
            cls.student_makes_submission(logged_user, students_assignments)
            input('Enter to back to menu')
        elif choice == '4':
            cls.my_subbmisions(logged_user)
            input('Enter to back to menu')
        elif choice == '0':
            exit()

    @staticmethod
    def get_assignment_list_with_grades(logged_user):
        """
        Makes list with assignments visible for student with notation if assignment was submitted
        and how it was graded.
        :param logged_user: (user object)
        :return: assignments_list_to_print
        """
        Ui.clear()
        Ui.print_head("{} {}'s assignments with grades".format(logged_user.name, logged_user.last_name), 'header')
        title_list = ['nr', 'title', 'mentor_id', 'start date', 'end date', 'type of assignment', 'submitted', 'grade']
        assignments_list = Assignment.pass_assign_for_student()
        assignments_list_to_print = []
        n = 1
        for assignment in assignments_list:
            type_of_assignment = 'Individual'
            if assignment.group == '1':
                type_of_assignment = 'Group'
            new_line = [str(n), assignment.title, assignment.mentor_id, assignment.start_date, assignment.end_date, type_of_assignment]
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
            assignments_list_to_print.append(new_line)
            n += 1
        Ui.print_table(assignments_list_to_print, title_list)

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
        if not Submission.find_submission(logged_user, assignment_to_submit):
            link = Ui.get_inputs(['Link to your repo:'])
            Submission.add_submission(logged_user.idx, assignment_to_submit.idx, date.today(), link[0])
        else:
            Ui.print_text("You can't submit this assignment - it's already submitted")

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
        Ui.print_table(logged_user_submission_to_print, ['title', 'start date', 'end date', 'submission date',
                                                         'link to repo', 'grade', 'mentor_id'])


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
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 8)

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

        elif choice == '2':
            cls.add_assignment(user_object)
            Ui.get_inputs([''])

        elif choice == '3':
            Ui.clear()
            cls.grade_submission()

        elif choice == '4':
            Ui.clear()
            cls.show_attendance_of_students()
            Ui.get_inputs([''])

        elif choice == '5':
            cls.switch_attendance()
            Ui.get_inputs([''])

        elif choice == '6':
            cls.add_user('Student')

        elif choice == '7':
            cls.remove_user('Student')

        elif choice == '8':
            cls.edit_user('Student')

        elif choice == '0':
            exit()

    @staticmethod
    def show_attendance_of_students():
        """
        Prints students in table with their presences
        :return:None
        """
        titles = ['Name', 'Last name', 'Present', 'Late', 'Absent']
        engagement_list = Attendance.students_engagement()
        Ui.print_table(engagement_list, titles)

    @staticmethod
    def grade_submission():
        """
        It enables assessment tasks
        :return:None
        """
        titles = ['Nr', 'Student\'s e-mail', 'Assignment title', 'Date of submission', 'Grade']
        grades_list = []
        n = 1
        for submission in Submission.submission_list:
            student = Common.get_by_id(submission.student_idx, Student.file)
            assignment = Common.get_by_id(submission.assignment_idx, 'csv/assignments.csv')
            grades_list.append([str(n), student[3], assignment[1], str(submission.date_of_submission),
                                str(submission.grade)])
            n += 1
        Ui.print_table(grades_list, titles)
        options = 'Choose number of submission to grade'
        user_choice = int(Ui.get_menu(options, 1, n))
        submission_to_grade = Submission.submission_list[user_choice - 1]
        new_grade = Ui.get_inputs(['New grade:'])[0]
        submission_to_grade.change_grade(new_grade)

    @staticmethod
    def add_assignment(user_object):
        """
        Adds new assignment
        :param user_object: User object (The currently logged in user)
        :return: None
        """
        mentor_id = user_object.idx #user_object.name + ' ' + user_object.last_name
        title = Ui.get_input('title')
        start_date = Common.make_corect_date(Ui.get_input('start date(YYYY-MM-DD)'))
        end_date = Common.make_corect_date(Ui.get_input('end date(YYYY-MM-DD)'))
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
                student_data = Common.get_by_id(student.id_student)
                Ui.print_head(student_data[1] + ' ' + student_data[2], 'warning')

                text = 'Is this student present today?\n(1: Present, 2: Late, 3: Absent):  '
                mentor_choice = Ui.get_menu(text, 1, 3)

                Attendance.toggle_present(student, mentor_choice)


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
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 6)

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
        elif choice == '6':
            Ui.clear()
            ManagerMenu.edit_user('Mentor')
        else:
            exit()
