import csv


class Common:
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