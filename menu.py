from ui import Ui
from manager import *
from student import *

class Menu:
    logged_user = User.login()


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

