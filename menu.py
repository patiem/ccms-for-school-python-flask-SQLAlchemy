from ui import Ui
from user import User
from manager import Manager
from student import Student
from mentor import Mentor
from employee import Employee


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

        options = '\t1: Show students' \
                  '\t2: Add assignment' \
                  '\t3: Grade assignment' \
                  '\t4: Check attendance of students' \
                  '\t5: Add student' \
                  '\t6: Remove student' \
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
    def choose_option(choice):
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
    def remove_mentor():
        mail = Ui.get_inputs(['Enter mentor e-mail to remove him : '])
        if Mentor.remove_object(mail):
            Ui.print_text('Mentor removed')
        else:
            Ui.print_text('No mentor of passed mail')