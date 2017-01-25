from ui import Ui
from user import User
from manager import *
from student import *


class Menu:

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
        Ui.clear()
        Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))
        Ui.print_head('Manager menu:', 'header')
        options = '\t1: Add mentor' \
                  '\t2: Remove Mentor' \
                  '\t3: Edit Mentor' \
                  '\t4: Show mentor list' \
                  '\t5: Show student list'
        user_choice = Ui.get_menu(options, 1, 5)

    @staticmethod
    def chose_option(choice):
        if choice == '1':
            pass
    @staticmethod
    def add_student():
        pass 

