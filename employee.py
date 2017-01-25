from user import *
from common import *

class Employee(User):
    employees_list = []

    def __init__(self, id, name, last_name, mail, telephone):
        """
        Create Employee object
        :param id: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        self.name = name
        self.last_name = last_name
        self.main = mail
        self.telephone = telephone
        self.id = id

    def edit_employee(self, name_of_attribute, new_value):
        """
        Edit employee passed attribute
        :param name_of_attribute: string (what attribute should be edit)
        :param new_value: string (new value for attribute)
        :return: None
        """
        if name_of_attribute == 'Name':
            self.name = new_value
        elif name_of_attribute == 'Last Name':
            self.last_name = new_value
        elif name_of_attribute == 'mail':
            self.mail = new_value
        elif name_of_attribute == 'telephone':
            self.telephone = new_value

    @classmethod
    def add_employee(cls, name, last_name, mail, telephone):
        """
        Add new employee object to list
        :param name: string (name of student)
        :param last_name: string (last name)
        :param mail: string (mail of student)
        :param telephone: string (telephone to student)
        :return: None
        """
        if Common.is_email_correct(mail):
            if Common.is_phone_correct(telephone):
                new_id = Common.generate_id(Employee.employees_list)
                new_employee = Employee(new_id ,name, last_name, mail, telephone)
                Employee.employees_list.append(new_employee)
            else:
                raise ValueError('Wrong number')
        else:
            raise ValueError('Wrong e-mail')

    @classmethod
    def remove_employee(cls, id):
        """
        Remove employee from list of employees
        :param id: string ( id of student to remove)
        :return: None
        """
        for employee in Employee.employees_list:
            if employee.id == id:
                Employee.employees_list.remove(employee)

    @classmethod
    def create_employee_list(cls):
        """
        Create list containing object of employees
        :return: None
        """
        list_from_csv = Common.read_file('csv/employees.csv')
        for person in list_from_csv:
            Employee.employees_list.append(Employee(person[0], person[1], person[2], person[3], person[4]))