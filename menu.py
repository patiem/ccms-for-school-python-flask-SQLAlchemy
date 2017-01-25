from ui import Ui
from user import User
from manager import *
from student import *
from mentor import Mentor


class Menu:

    @staticmethod
    def logged_as(logged_user):
        Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))

    # @staticmethod
    # def print_menu():
    #     raise NotImplementedError()

    @staticmethod
    def print_menu():
        raise NotImplementedError()

    @staticmethod
    def run():

        logged_user = User.login()

        if logged_user[3] == 'student':
            StudentMenu.print_menu()

        if logged_user[3] == 'mentor':
            MentorMenu.print_menu()

        if logged_user[3] == 'manager':
            EmployeeMenu.print_menu()

        if logged_user[3] == 'employee':
            ManagerMenu.print_menu()



class StudentMenu(Menu):
    pass


class MentorMenu(Menu):
    pass


class EmployeeMenu(Menu):
    pass


class ManagerMenu(Menu):

    @staticmethod
    def print_menu(user_object):

        while True:
            Ui.clear()
            Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))
            Ui.print_head('Manager menu:', 'header')
            options = '\t1: Add mentor\n' \
                      '\t2: Remove Mentor\n' \
                      '\t3: Edit Mentor\n' \
                      '\t4: Show mentor list\n' \
                      '\t5: Show student list\n' \
                      '\t0: Exit program'
            user_choice = Ui.get_menu(options, 1, 5)
            ManagerMenu.chose_option(user_choice)

    @staticmethod
    def chose_option(choice):
        if choice == '1':
            ManagerMenu.add_mentor()
        elif choice == '2':
            ManagerMenu.print_mentors()
        elif choice == '4':
            ManagerMenu.add_student()
        elif choice == '5':
            ManagerMenu.print_students()
        else:
            exit()

    @staticmethod
    def add_student():
        label_list = ['Name', 'Last Name', 'E-mail', 'telephone']
        user_data = Ui.get_inputs(label_list)
        User.add_user(user_data[0], user_data[1], user_data[2], user_data[3], Student.pass_list())

    @staticmethod
    def add_mentor():
        label_list = ['Name', 'Last Name', 'E-mail', 'telephone']
        user_data = Ui.get_inputs(label_list)
        User.add_user(user_data[0], user_data[1], user_data[2], user_data[3], Mentor.pass_list())

    @staticmethod
    def print_students():
        Ui.clear()
        Ui.print_table(User.create_list_to_save(Student.pass_list()),
                       ['id', 'name', 'last name', 'mail', 'telephone'])
        Ui.get_inputs(['Enter anything to leave: '])

    @staticmethod
    def print_mentors():
        Ui.clear()
        Ui.print_table(User.create_list_to_save(Mentor.pass_list()),
                       ['id', 'name', 'last name', 'mail', 'telephone'])
        Ui.get_inputs(['Enter anything to leave: '])

    @staticmethod
    def

Student.create_object_list('csv/students.csv', Student.students_list)
ManagerMenu.print_menu(Student.students_list[0])