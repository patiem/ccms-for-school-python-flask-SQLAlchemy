import csv

class Common:

    @staticmethod
    def get_by_id():
        pass

    @staticmethod
    def generate_id(table):
        import random

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


lista = [['a', '1', 11], ['b', '2', 22], ['c', '3', 33], ['d', '4', 44]]

Common.save_file('test.csv', lista)
print(Common.read_file('test.csv'))