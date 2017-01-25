from ui import Ui
from user import User


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
    pass
