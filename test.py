import re
from ui import Ui
from common import Common


class Test:

    @classmethod
    def test_add_arguments(cls, label_list, arguments_list):
        """
        test passed arguments are correct
        :param label_list: list ( list with names of attribute to check)
        :param arguments_list: list ( list of arguments to test)
        :return: arguments_list
        """
        idx = 0
        for label in label_list:
            arguments_list[idx] = cls.check_argument(label, arguments_list[idx])
            idx += 1
        return arguments_list

    @classmethod
    def check_argument(cls, label, argument):
        '''
        Choose how to check argument
        :param label: string ( name of argument)
        :param argument: string ( argument to check)
        :return: argument
        '''
        if label.lower() == 'Name'.lower():
            argument = cls.test_name(argument)
        elif label.lower() == 'Last Name'.lower():
            argument = cls.test_last_name(argument)
        elif label.lower() == 'E-mail'.lower():
            argument = cls.test_mail(argument)
        elif label.lower() == 'Phone Number'.lower():
            argument = cls.test_phone_number(argument)
        elif label.lower() == 'telephone'.lower():
            argument = cls.test_phone_number(argument)
        return argument

    @classmethod
    def test_mail(cls, mail):
        """
        test if e-mail is correct
        :param mail: string ( e-mail to check)
        :return: mail
        """
        mail_list = []
        users_list = Common.aggregation_users()
        for item in users_list:
            mail_list.append(item[1])
        while True:
            if cls.is_email_correct(mail):
                if mail in mail_list:
                    Ui.print_text('\n E-mail already exist')
                    mail = Ui.get_inputs(['Mail:'])[0]
                else:
                    break
            else:
                Ui.print_text('\nWrong mail format')
                mail = Ui.get_inputs(['Mail:'])[0]
        return mail

    @classmethod
    def test_phone_number(cls, phone_number):
        """
        test phone number
        :param phone_number: string (phone number to test)
        :return: phone_number
        """
        while not cls.is_phone_correct(phone_number):
            Ui.print_text('\nWrong phone number')
            phone_number = Ui.get_inputs(['Phone number:'])[0]
        return phone_number

    @classmethod
    def test_name(cls, name):
        """
        test name is correct
        :param name: string ( name to test)
        :return: name
        """
        while True:
            if cls.is_name_correct(name):
                break
            else:
                Ui.print_text('\nWrong name')
                name = Ui.get_inputs(['Name:'])[0]
        return name

    @classmethod
    def test_last_name(cls, last_name):
        """
        test last name is correct
        :param last_name: string (last name to test)
        :return: last_name
        """
        while not cls.is_name_correct(last_name):
            Ui.print_text('\nWrong last name')
            last_name = Ui.get_inputs(['Last Name:'])[0]
        return last_name

    @classmethod
    def test_edit_user(cls, attribute_name):
        """
        Test name of chosen  argument to edit user
        :param attribute_name:
        :return:
        """
        attribute_list = ['Name', 'Surname', 'E-mail', 'Telephone', 'Password']

        while True:
            if attribute_name in attribute_list:
                break
            else:
                Ui.print_text('\nWrong attribute to edit')
                attribute_name = Ui.get_inputs(['Attribute to edit (name,last name,mail,telephone,password): '])[0]
        return attribute_name

    @staticmethod
    def is_email_correct(email):
        """
        Validates if email is correct gmail adress.
        Argument: email (str)
        Return: Bool
        """
        if email and not email == '\t':
            pattern = r'^((\w+\.*)+)@\w+.\w+$'
            if re.search(pattern, email):
                return True
            return True
        return False

    @staticmethod
    def is_phone_correct(phone):
        """
        Validates if phone number is correct polish mobile number.
        Argument: phone (str)
        Return: Bool
        """
        if phone:
            pattern = r'^\s*(\+?48)*\s*((\d{3})[ \-]?){3}\s*$'
            if re.search(pattern, phone):
                return True
        return False

    @staticmethod
    def is_name_correct(name):
        """
        Validates if name is correct - can have more than one part with space or '-' between.
        Argument: name (str)
        Return: Bool
        """
        if name and not name == '\t':
            pattern = r'^\s*([A-ZŚĆŻ][a-ząęśćńżó]+[ \-]?)*s*$'
            if re.search(pattern, name):
                return True
        return False

    @staticmethod
    def is_date_correct(date):
        """
        Validates if date is correct and can be made datetime object.
        Argument: date (str)
        Return: Bool
        """
        if date and not date == '\t':
            pattern = r'^\d{4}[-\.](0\d|1[012])[-\.]([012]\d|3[01])$'
            if re.search(pattern, date):
                return True
        return False

    @staticmethod
    def does_file_exist(file):
        """
        Validates if file exists.
        Args: file (str with file's path)
        Return: Boolean
        """
        try:
            open(file, 'r')
            return True
        except FileNotFoundError:
            return False
