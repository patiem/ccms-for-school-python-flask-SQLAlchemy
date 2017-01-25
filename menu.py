from ui import Ui
from manager import *

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
    def print_manager_menu(user_object):
        Ui.clear()
        Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))
        Ui.print_head('Manager menu:', 'header')
        options_list = ['1: Add mentor',
                        '2: Remove Mentor',
                        '3: Edit Mentor',
                        '4: Show mentor list'
                        '5: Show student list']
        Ui.print_menu(options_list)
