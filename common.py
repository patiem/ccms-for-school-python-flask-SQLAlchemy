import csv
import re
import random
import datetime


class Common:
    """
    Class
    """

    @staticmethod
    def get_by_id():
        pass

    @staticmethod
    def generate_id(table):
        """
        Generates random and unique string. Used for id/key generation.
        Args:
            table: list containing keys. Generated string should be different then all of them
        Returns:
            Random and unique string
        """
        list_of_id = []
        for record in table:
            list_of_id.append(record.id)

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
        Args: file (str with file's path)
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
        pattern = r'^((\w+\.*)+)@gmail.com$'
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
        pattern = r'^\d{4}\.(0\d|1[012])\.([012]\d|3[01])$'
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
    def is_user_choice_correct(user_input, choices):
        """
        Checks if number is in range
        Args: user_input(string): should be number in range of options
              choices(int): max number in options
        Returns: Boolean
        """
        if user_input.isnumeric():
            if int(user_input) <= choices and int(user_input) >= 0:
                return True
        return False

    @staticmethod
    def make_corect_date(date):
        """
        Take string and returns date as datetime object.
        Args: date(string): year.month.day
        Returns: datetime object
        """
        date_list = date.split('.')
        correct_date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return correct_date

"""lista = [['a', '1', 11], ['b', '2', 22], ['c', '3', 33], ['d', '4', 44]]

Common.save_file('test.csv', lista)
print(Common.read_file('test.csv'))
emails = ['dupa@gmail.com', 'dupa.dupa@gmail.com', 'dupa@gail.com', 'dupa,f@gmai.com', '.dupa@gmail.com',
          '22.poo@gmail.com']
for email in emails:
    Common.is_email_correct(email)
phones = ['123123123', '123 123 123', '123-123-123', ' 123123123', '123 123123', '123-123-123 ',
          '1231231231', 'a23 123 123', '12#-123-123', '+48123123123', '48 123 123 123', ' + 48 123-123-123']
for number in phones:
    Common.is_phone_correct(number)
names = ['Aaa', 'AAaa', 'Aą Aa', 'Aa-Aa', 'A2aa', 'Ćwiek']
for name in names:
    Common.is_name_correct(name)
print(Common.does_file_exist('csv/students.csv'))
dates = ['1234.12.30', '9999.13.01', '2011.01.43']
for date in dates:
    print(Common.is_date_correct(date))

print(Common.make_corect_date('1234.12.30'))"""