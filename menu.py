from ui import Ui
from user import User
from manager import Manager
from student import Student
from mentor import Mentor
from employee import Employee
from common import Common
from assignment import Assignment
from submission import Submission

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
    def edit_user(class_name):
        edit_arguments_list = Ui.get_inputs(['Mail of user to edit: ',
                                             'what to edit (name,last name,mail,telephone,password): ',
                                             'new value: '])
        Menu.where_to_edit(class_name, edit_arguments_list)
        Menu.what_save(class_name)

    @staticmethod
    def remove_user(class_name):
        mail = Ui.get_inputs(['Enter mentor e-mail to remove him : '])
        if Menu.where_to_remove(class_name, mail[0]):
            Ui.print_text('User removed')
        else:
            Ui.print_text('No user of passed mail')
        Menu.what_save(class_name)

    @staticmethod
    def where_to_edit(class_name, edit_arguments_list):
        if class_name == 'Student':
            Student.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])
        elif class_name == 'Mentor':
            Mentor.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])
        elif class_name == 'Manager':
            Manager.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])
        elif class_name == 'Employee':
            Employee.edit_user(edit_arguments_list[0], edit_arguments_list[1], edit_arguments_list[2])

    @staticmethod
    def where_to_remove(class_name, mail):
        if class_name == 'Student':
            return Student.remove_object(mail)
        elif class_name == 'Mentor':
            return Mentor.remove_object(mail)
        elif class_name == 'Manager':
            return Manager.remove_object(mail)
        elif class_name == 'Employee':
            return Employee.remove_object(mail)

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
            Student.add_user(user_data[0], user_data[1], user_data[2], user_data[3])
        elif class_name == 'Mentor':
            Mentor.add_user(user_data[0], user_data[1], user_data[2], user_data[3])
        elif class_name == 'Manager':
            Manager.add_user(user_data[0], user_data[1], user_data[2], user_data[3])
        elif class_name == 'Employee':
            Employee.add_user(user_data[0], user_data[1], user_data[2], user_data[3])

    @staticmethod
    def show_all_students():
        pass

    @staticmethod
    def choose_option(choice):   #a co z przekazaniem zalogowanego uzytkownika??
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
        Assignment.create_assignment_list()
        Submission.create_submission_list()


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

    @classmethod
    def print_menu(cls, user_object):
        while True:
            Ui.clear()
            Menu.logged_as(user_object)
            Ui.print_head('Student menu:', 'header')

            options = '\t1: Show assignment list\n' \
                      '\t2: Add submit assignment\n' \
                      '\t3: View my grades\n' \
                      '\t0: Exit program'

            user_choice = Ui.get_menu(options, 0, 3)
            cls.choose_option(user_choice, user_object)

    @classmethod
    def choose_option(cls, choice, logged_user):

        if choice == '1':
            cls.get_assignment_list_with_grades(logged_user)
            input('Enter to back to menu')

        elif choice == '2':
            cls.student_makes_submission(logged_user)
            pass
        elif choice == '3':
            # View grades
            pass
        elif choice == '0':
            exit()

    @staticmethod
    def get_assignment_list_with_grades(logged_user):
        """
        Makes list with assignments visible for student with notation if assignment was submitted
        and how it was graded.
        :param logged_user: (user object)
        :return:
        """
        Ui.clear()
        Ui.print_text("{} {}'s assignments with grades".format(logged_user.name, logged_user.last_name))
        title_list = ['nr', 'title', 'author', 'start date', 'end date', 'submitted', 'grade']
        assignments_list = Assignment.pass_assign_for_student()    #doublled list of assignments!!
        assignments_list_to_print = []
        n = 1
        for assignment in assignments_list:
            new_line = [str(n), assignment.title, assignment.author, assignment.start_date, assignment.end_date]
            submission = Submission.find_submission(logged_user, assignment)
            if submission:
                new_line.append('submitted')
                if submission.grade:
                    new_line.append(submission.grade)
                else:
                    new_line.append('None')
            else:
                new_line.append('not submitted')
                new_line.append('None')
            assignments_list_to_print.append(new_line)
            n += 1
        Ui.print_table(assignments_list_to_print, title_list)
        return len(assignments_list_to_print)

    @classmethod
    def student_makes_submission(cls, logged_user):
        n = cls.get_assignment_list_with_grades(logged_user)
        user_choice = Ui.get_menu('', 0, n)


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
            MentorMenu.show_attendance_of_students()

        elif choice == '5':
            MentorMenu.add_user(Student.object_list)

        elif choice == '6':
            pass

        elif choice == '7':
            pass

        elif choice == '0':
            exit()

    @staticmethod
    def show_attendance_of_students():
        pass


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
            ManagerMenu.remove_user('Mentor')
        elif choice == '4':
            ManagerMenu.add_user('Student')
        elif choice == '5':
            ManagerMenu.print_user(Student.object_list)
        elif choice == '6':
            ManagerMenu.edit_user('Mentor')
        else:
            exit()




            
# Student.create_object_list(Student.pass_list())
# Mentor.create_object_list(Mentor.pass_list())
# Employee.create_object_list(Employee.pass_list())
# Manager.create_object_list(Manager.pass_list())
#
# ManagerMenu.print_menu(Student.object_list[0])
