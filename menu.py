from ui import Ui
from user import User
from manager import Manager
from student import Student
from mentor import Mentor
from employee import Employee
from common import Common


class Menu:

    @staticmethod
    def choose_option(choice):
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

        Student.create_object_list(Student.pass_list())
        Mentor.create_object_list(Mentor.pass_list())
        Employee.create_object_list(Employee.pass_list())
        Manager.create_object_list(Manager.pass_list())

        if logged_user[3] == 'student':
            for student in Student.object_list:
                if student.idx == logged_user[0]:
                    user = student
                    StudentMenu.print_menu(user)

        if logged_user[3] == 'mentor':

            for mentor in Mentor.object_list:
                if mentor.idx == logged_user[0]:
                    user = mentor
                    MentorMenu.print_menu(user)

        if logged_user[3] == 'manager':
            for manager in Manager.object_list:
                if manager.idx == logged_user[0]:
                    user = manager
                    ManagerMenu.print_menu(user)
        if logged_user[3] == 'employee':
            for employee in Employee.object_list:
                if employee.idx == logged_user[0]:
                    user = employee
                    ManagerMenu.print_menu(user)


class StudentMenu(Menu):

    @staticmethod
    def print_menu(user_object):
        Ui.clear()
        Menu.logged_as(user_object)
        Ui.print_head('Student menu:', 'header')

        options = '\t1: Add submit assignment\n' \
                  '\t2: View my grades' \

        user_choice = Ui.get_menu(options, 1, 2)

    @staticmethod
    def choose_option(choice):
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

        options = '\t1: Show students\n' \
                  '\t2: Add assignment\n' \
                  '\t3: Grade assignment\n' \
                  '\t4: Check attendance of students\n' \
                  '\t5: Add student\n' \
                  '\t6: Remove student\n' \
                  '\t7: Edit student\'s data'

        user_choice = Ui.get_menu(options, 1, 7)

    @staticmethod
    def choose_option(choice):
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

        while True:
            Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))
            Ui.print_head('Manager menu:', 'header')
            options = '\t1: Add mentor\n' \
                      '\t2: Show mentor list\n' \
                      '\t3: Remove mentor\n' \
                      '\t4: Add student\n' \
                      '\t5: Show student\n' \
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 5)

            ManagerMenu.choose_option(user_choice)

    @staticmethod
    def choose_option(choice):
        if choice == '1':
            ManagerMenu.add_user(Mentor.pass_list())
        elif choice == '2':
            ManagerMenu.print_user(Mentor.pass_list())
        elif choice == '3':
            ManagerMenu.remove_mentor()
        elif choice == '4':
            ManagerMenu.add_user(Student.pass_list())
        elif choice == '5':
            ManagerMenu.print_user(Student.pass_list())
        else:
            exit()


    @staticmethod
    def add_user(object_list):
        label_list = ['Name', 'Last Name', 'E-mail', 'telephone']
        user_data = Ui.get_inputs(label_list)
        password = User.encode('1')
        User.add_user(user_data[0], user_data[1], user_data[2], user_data[3], password, object_list)

    @staticmethod
    def print_user(object_list):
        Ui.clear()
        print_list = []
        for list in User.create_list_to_save(object_list):
            print_list.append([list[0], list[1], list[2], list[3], list[4]])
        Ui.print_table(print_list,
                       ['id', 'name', 'last name', 'mail', 'telephone'])
        Ui.get_inputs(['Enter anything to leave: '])

    @staticmethod
    def remove_mentor():
        mail = Ui.get_inputs(['Enter mentor e-mail to remove him : '])
        if Mentor.remove_object(mail[0]):
            Ui.print_text('Mentor removed')
        else:
            Ui.print_text('No mentor of passed mail')
            

Student.create_object_list(Student.pass_list())
Mentor.create_object_list(Mentor.pass_list())
Employee.create_object_list(Employee.pass_list())
Manager.create_object_list(Manager.pass_list())

ManagerMenu.print_menu(Student.object_list[0])