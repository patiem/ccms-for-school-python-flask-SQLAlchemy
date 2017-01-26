from ui import Ui
from user import User
from manager import Manager
from student import Student
from mentor import Mentor
from employee import Employee
from common import Common


class Menu:

    @staticmethod
    def add_user(class_name):
        label_list = ['Name', 'Last Name', 'E-mail', 'telephone']
        user_data = Ui.get_inputs(label_list)
        Menu.where_to_add(class_name, user_data)
        Menu.what_save(class_name)

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
    def edit_user(object_list, class_name):
        edit_arguments_list = Ui.get_inputs(['Mail of user to edit: ', 'what to edit (name,last name,mail,telephone,password): ',
                       'new value: '])
        User.edit_user(object_list, edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])
        Menu.what_save(class_name)

    @staticmethod
    def remove_user(object_list, class_name):
        mail = Ui.get_inputs(['Enter mentor e-mail to remove him : '])
        if User.remove_object(mail[0], object_list):
            Ui.print_text('User removed')
        else:
            Ui.print_text('No user of passed mail')
        Menu.what_save(class_name)

    @staticmethod
    def what_save(class_name):
        if class_name == 'Student':
            Common.save_file(Student.file, Student.create_list_to_save(Student.object_list))
        elif class_name == 'Mentor':
            Common.save_file(Mentor.file, Mentor.create_list_to_save(Mentor.object_list))
        elif class_name == 'Manager':
            Common.save_file(Manager.file, Manager.create_list_to_save(Manager.object_list))
        elif class_name == 'Employee':
            Common.save_file(Employee.file, Employee.create_list_to_save(Employee.object_list))
    
    @staticmethod
    def where_to_add(class_name, user_data):
        if class_name == 'Student':
            Student.add_user(user_data[0], user_data[1], user_data[2], user_data[3], Student.object_list)
        elif class_name == 'Mentor':
            Mentor.add_user(user_data[0], user_data[1], user_data[2], user_data[3], Mentor.object_list)
        elif class_name == 'Manager':
            Manager.add_user(user_data[0], user_data[1], user_data[2], user_data[3], Manager.object_list)
        elif class_name == 'Employee':
            Employee.add_user(user_data[0], user_data[1], user_data[2], user_data[3], Employee.object_list)
        
            
    
    
    @staticmethod
    def show_all_students():
        pass

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

        Student.create_object_list(Student.object_list)
        Mentor.create_object_list(Mentor.object_list)
        Employee.create_object_list(Employee.object_list)
        Manager.create_object_list(Manager.object_list)

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
                  '\t0: Exit program'

        user_choice = Ui.get_menu(options, 0, 2)

    @staticmethod
    def choose_option(choice):
        if choice == '1':
            # Add submit
            pass
        elif choice == '2':
            # View grades
            pass
        elif choice == '0':
            exit()

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
                  '\t7: Edit student\'s data' \
                  '\t0: Exit program'

        user_choice = Ui.get_menu(options, 0, 7)

    @staticmethod
    def choose_option(choice):
        if choice == '1':
            MentorMenu.print_user(Student.object_list)

        elif choice == '2':
            pass

        elif choice == '3':
            pass

        elif choice == '4':
            pass

        elif choice == '5':
            MentorMenu.add_user(Student.object_list)

        elif choice == '6':
            pass

        elif choice == '7':
            pass

        elif choice == '0':
            exit()


class EmployeeMenu(Menu):
    @staticmethod
    def print_menu(user_object):
        Ui.clear()
        Menu.logged_as(user_object)
        Ui.print_head('Mentor menu:', 'header')

        options = '\t1: Show students\n' \
                  '\t0: Exit program'

        user_choice = Ui.get_menu(options, 0, 1)

    @staticmethod
    def choose_option(choice):

        if choice == '1':

            EmployeeMenu.print_user(Student.object_list)
        elif choice == '0':
            exit()


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
                      '\t6: Edit Mentor\n' \
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 6)

            ManagerMenu.choose_option(user_choice)

    @staticmethod
    def choose_option(choice):
        if choice == '1':
            ManagerMenu.add_user('Mentor')
        elif choice == '2':
            ManagerMenu.print_user(Mentor.object_list)
        elif choice == '3':
            ManagerMenu.remove_user(Mentor.object_list, 'Mentor')
        elif choice == '4':
            ManagerMenu.add_user('Student')
        elif choice == '5':
            ManagerMenu.print_user(Student.object_list)
        elif choice == '6':
            ManagerMenu.edit_user(Mentor.object_list, 'Mentor')
        else:
            exit()




            

Student.create_object_list(Student.object_list)
Mentor.create_object_list(Mentor.object_list)
Employee.create_object_list(Employee.object_list)
Manager.create_object_list(Manager.object_list)

ManagerMenu.print_menu(Student.object_list[0])
