from user import *
from common import *

class Employee(User):
    employees_list = []

    def __init__(self, id, name, last_name, mail, telephone):
        self.name = name
        self.last_name = last_name
        self.main = mail
        self.telephone = telephone
        self.id = id

    def edit_employee(self, name_of_attribute, new_value):
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
        new_id = Common.generate_id(Employee.employees_list)
        new_employee = Employee(new_id ,name, last_name, mail, telephone)
        Employee.employees_list.append(new_employee)

    @classmethod
    def remove_employee(cls, id):
        for employee in Employee.employees_list:
            if employee.id == id:
                Employee.employees_list.remove(employee)

    @classmethod
    def create_employee_list(cls):
        list_from_csv = Common.read_file('csv/employees.csv')
        for person in list_from_csv:
            Employee.employees_list.append(Employee(person[0], person[1], person[2], person[3], person[4]))