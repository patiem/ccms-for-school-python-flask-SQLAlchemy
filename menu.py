from ui import Ui
from user import User
from manager import Manager
from student import Student
from mentor import Mentor
from employee import Employee


class Menu:

    @staticmethod
    def logged_as(logged_user):
        #Ui.print_head('Logged as {} {}'.format(user_object.name, user_object.last_name, 'header'))
        pass

    # @staticmethod
    # def print_menu():
    #     raise NotImplementedError()

    @staticmethod
    def print_menu():
        raise NotImplementedError()

    @staticmethod
    def run():

        logged_user = User.login()

        Student.create_object_list(Student.pass_list())
        Mentor.create_object_list(Mentor.pass_list())
        Employee.create_object_list(Employee.pass_list())
        Manager.create_object_list(Manager.pass_list())

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
            ManagerMenu.add_mentor()
        elif choice == '2':
            ManagerMenu.print_mentors()
        elif choice == '3':
            ManagerMenu.remove_mentor()
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
        if Mentor.remove_object(mail[0]):
            Ui.print_text('Mentor removed')
        else:
            Ui.print_text('No mentor of passed mail')
            

# Student.create_object_list(Student.pass_list())
# Mentor.create_object_list(Mentor.pass_list())
# Employee.create_object_list(Employee.pass_list())
# Manager.create_object_list(Manager.pass_list())
#
# ManagerMenu.print_menu(Student.object_list[0])