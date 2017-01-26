import csv
import re
import datetime


class Common:
    """
    Class
    """

    @staticmethod
    def aggregation_users():
        """
        Generates full list of users
        :return: list (user list: ID|E-MAIL|PASSWORD|TYPE)
        """
        users_list = []
        files_list = ['csv/students.csv', 'csv/mentors.csv', 'csv/employees.csv', 'csv/managers.csv']

        for file in files_list:
            array = Common.read_file(file)
            for person in array:
                users_list.append([person[0], person[3], person[5], file[4:-5]])
        return users_list

    @staticmethod
    def get_by_id(index, file=None):
        """
        Returns list
        :param index: string (user_id/attendance_id/...)
        :param file: string (file path - 'csv/students.csv')
        :return: list (row from file)
        """
        files_list = ['csv/students.csv', 'csv/mentors.csv', 'csv/employees.csv', 'csv/manager.csv']

        if file:
            row = Common.get_row(index, file)
            if row:
                return row

        for item in files_list:
            row = Common.get_row(index, item)
            if row:
                return row
        raise IndexError("There is no such index")

    @staticmethod
    def get_row(index, filename):
        """
        Helper for get_by_id()
        :param index: string
        :param filename: string
        :return: list or bool (row from file or False)
        """
        array = Common.read_file(filename)
        for row in array:
            if row[0] == index:
                return row
        return False

    @staticmethod
    def generate_id():
        """
        Generates random and unique string. Used for id/key generation.
        Returns:
            Random and unique string
        """
        import random

        table = Common.aggregation_users()
        assignments = Common.read_file('csv/assignments.csv')
        for assignment in assignments:
            table.append(assignment)

        list_of_id = []
        for record in table:
            list_of_id.append(record[0])

        generated = ''

        special_char_index = list(range(33, 48)) + list(range(58, 59)) + list(range(60, 65)) \
                                                 + list(range(91, 97)) + list(range(124, 127))
        start = True
        max_len_id = 3
        while start:
            list_of_char = []
            new_id = ''

            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(str(chr(random.choice(special_char_index))))
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(str(random.randint(0, 9)))
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(chr(random.randint(97, 122)).upper())
            for i in range(random.randint(2, max_len_id)):
                list_of_char.append(chr(random.randint(97, 122)))

            for i in range(len(list_of_char)):
                char = random.choice(list_of_char)
                new_id += char
                list_of_char.remove(char)
            if new_id not in list_of_id:
                generated += new_id
                start = False

        return generated

    @staticmethod
    def read_file(file, header=None):
        """
        Loads list from csv file.
        Args: file (str with file's path)
              header (if set to not None returns first line of file with data structure)
        Returns: imported_list[1:] (2d list from file)
        """
        imported_list = []
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for line in reader:
                imported_list.append(line)
        if header:
            return imported_list[0]
        return imported_list[1:]

    @classmethod
    def save_file(cls, file, list_to_save):
        """
        Saves list to csv file.
        Args:
             list_to_save (list)
        """
        atributes_names = cls.read_file(file, 1)

        with open(file, 'w') as f:
            f.write(';'.join(atributes_names) + '\n')
            for item in list_to_save:
                for n, cell in enumerate(item):
                    if type(cell) != str:
                        item[n] = str(cell)
                f.write(';'.join(item) + '\n')

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
        Argument: date (str - should be in format YYYY.MM.DD or YYYY-MM-DD or YYYY MM DD)
        Return: Bool
        """
        if date:
            pattern = r'^\d{4}[ -\.](0\d|1[012])[ -\.]([012]\d|3[01])$'
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

    @staticmethod
    def make_corect_date(date):
        """
        Take string and returns date as datetime object.
        Args: date(string): year.month.day
        Returns: datetime object
        """
        if '.' in date:
            date_list = date.split('.')
        elif '-' in date:
            date_list = date.split('-')
        elif ' ' in date:
            date_list = date.split(' ')
        correct_date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return correct_date
