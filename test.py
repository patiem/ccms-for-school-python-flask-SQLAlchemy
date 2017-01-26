import re
from ui import Ui


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
        if label == 'Name':
            argument = cls.test_name(argument)
        elif label == 'Last Name':
            argument = cls.test_last_name(argument)
        elif label == 'E-mail':
            argument = cls.test_mail(argument)
        elif label == 'Phone Number':
            argument = cls.test_phone_number(argument)
        elif label == 'telephone':
            argument = cls.test_phone_number(argument)
        return argument

    @classmethod
    def test_mail(cls, mail):
        """
        test if e-mail is correct
        :param mail: string ( e-mail to check)
        :return: mail
        """
        while not cls.is_email_correct(mail):
            Ui.print_text('Wrong mail')
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
            Ui.print_text('Wrong phone number')
            phone_number = Ui.get_inputs(['Phone number:'])[0]
        return phone_number

    @classmethod
    def test_name(cls, name):
        """
        test name is correct
        :param name: string ( name to test)
        :return: name
        """
        while not cls.is_name_correct(name):
            Ui.print_text('Wrong name')
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
            Ui.print_text('Wrong last name')
            last_name = Ui.get_inputs(['Last Name:'])[0]
        return last_name

    @classmethod
    def test_edit_user(cls, attribute_name):
        attribute_list = ['name', 'last name', 'mail', 'telephone', 'password']

        while True:
            if attribute_name in attribute_list:
                break
            else:
                Ui.print_text('Wrong attribute to edit')
                attribute_name = Ui.get_inputs(['Attribute to edit (name,last name,mail,telephone,password): '])[0  ]
        return attribute_name

    @staticmethod
    def is_email_correct(email):
        """
        Validates if email is correct gmail adress.
        Argument: email (str)
        Return: Bool
        """
        if email:
            pattern = r'^((\w+\.*)+)@\w+.\w+$'
            if re.search(pattern, email):
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
        if name:
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
        if date:
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