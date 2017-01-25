from ui import Ui
from user import User
from manager import *
from student import *


class Menu:

    @staticmethod
    def chose_option(choice):
        raise NotImplementedError()

    @staticmethod
    def logged_as(logged_user):
        Ui.print_head('Logged as {} {}'.format(logged_user.name, logged_user.last_name, 'header'))

    @staticmethod
    def print_menu(user_object):
        raise NotImplementedError()

    @staticmethod
    def run():

        logged_user = User.login()
        
        if logged_user[3] == 'student':
            for student in Student.object_list:
                if student.idx == logged_user[0]:
                    user = student
                    StudentMenu.print_menu(user)

        if logged_user[3] == 'mentor':
            MentorMenu.print_menu(logged_user)

        if logged_user[3] == 'manager':
            EmployeeMenu.print_menu(logged_user)

        if logged_user[3] == 'employee':
            ManagerMenu.print_menu(logged_user)

    @staticmethod
    def find_user(logged_user):



class StudentMenu(Menu):

    @staticmethod
    def print_menu(user_object):
        Ui.clear()
        Menu.logged_as(user_object)
        Ui.print_head('Student menu:', 'header')

        options = '\t1: Add submit assignment' \
                  '\t2: View my grades' \

        user_choice = Ui.get_menu(options, 1, 2)

    @staticmethod
    def chose_option(choice):
        if choice == '1':
            pass

    @staticmethod
    def add_student():
        pass


class MentorMenu(Menu):

    @staticmethod
    def print_menu(user_object):
        Ui.clear()
        Menu.logged_as(user_object)
        Ui.print_head('Mentor menu:', 'header')

        options = '\t1: Show students' \
                  '\t2: Add assignment' \
                  '\t3: Grade assignment' \
                  '\t4: Check attendance of students' \
                  '\t5: Add student' \
                  '\t6: Remove student' \
                  '\t7: Edit student\'s data'

        user_choice = Ui.get_menu(options, 1, 7)

    @staticmethod
    def chose_option(choice):
        if choice == '1':
            pass

    @staticmethod
    def add_student():
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

