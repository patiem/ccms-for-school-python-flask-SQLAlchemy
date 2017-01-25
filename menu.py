from ui import Ui
from manager import *
from student import *

class Menu:
    #logged_user = User.login()
    pass

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
                      '\t5: Show student list\n'
            user_choice = Ui.get_menu(options, 1, 5)
            ManagerMenu.chose_option(user_choice)

    @staticmethod
    def chose_option(choice):
        if choice == '1':
            ManagerMenu.add_student()
        if choice == '2':
            Ui.print_table(Student.create_list_to_save(Student.pass_list()), ['id', 'name', 'last name', 'mail', 'telephone'])
        else:
            exit()

    @staticmethod
    def add_student():
        label_list = ['Name', 'Last Name', 'E-mail', 'telephone']
        user_data = Ui.get_inputs(label_list)
        Student.add_user(user_data[0], user_data[1], user_data[2], user_data[3], Student.pass_list())

Student.create_object_list('csv/students.csv', Student.students_list)
ManagerMenu.print_menu(Student.students_list[0])