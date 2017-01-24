import csv
import re
import random

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
    def read_file(file):
        """
        Loads list from csv file.
        """
        imported_list = []
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for line in reader:
                imported_list.append(line)
        return imported_list[1:]

    @classmethod
    def save_file(cls, file, list_to_save):
        """
        Saves list to csv file.
        """
        atributes_names = cls.read_file(file)[0]

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
        Argument: str
        Return: Bool
        """
        pattern = r'^((\w+\.*)+)@gmail.com$'
        if re.search(pattern, email):
            print(email, ' ok')
            return True
        print(email, ' No')
        return False

    @staticmethod
    def is_phone_correct(phone):
        """
        Validates if phone number is correct polish mobile number.
        Argument: str
        Return: Bool
        """
        pattern = r'^\s*(\+?48)*\s*((\d{3})[ \-]?){3}\s*$'
        if re.search(pattern, phone):
            print(phone, ' ok')
            return True
        print(phone, ' No')
        return False

    @staticmethod
    def is_name_correct(name):
        """
        Validates if name is correct - can have more than one part with space or '-' between.
        Argument: str
        Return: Bool
        """
        pattern = r'^\s*([A-ZŚĆŻ][a-ząęśćńżó]+[ \-]?)*s*$'
        if re.search(pattern, name):
            print(name, ' ok')
            return True
        print(name, ' No')
        return False

    @staticmethod
    def does_file_exist(file):
        """
        Validates if file exists.
        Argument: str
        Return: Bool
        """
        try:
            open(file, 'r')
            return True
        except FileNotFoundError:
            return False


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
print(Common.does_file_exist('csv/students.csv'))"""