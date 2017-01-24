


class Common:
    @staticmethod
    def read_file(file):
        """
        Loads list from csv file.
        """
        imported_list = []
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for line in reader[1:]:
                """if line.index == 0:
                    atributes_names = line[:]
                else:"""
                imported_list.append(line)
        return imported_list

    @staticmethod
    def save_file(file, list_to_save):
        """
        Saves list to csv file.
        """
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            atributes_names = reader[0]

        with open(file, 'w') as f:
            f.write(';'.join(atributes_names) + '\n')
            for item in list_to_save:
                f.write(';'.join(item) + '\n')

lista = [['a', '1', 11], ['b', '2', 22], ['c', '3', 33]]

Commmon.save_file('test.csv', lista)