import os
import getpass


class Color:
    """Simple Class of coloring text"""

    # terminal design
    Header = '\033[92m'
    Warning = '\033[93m'
    Error = '\033[91m'

    TableHead = '\033[93m'

    # additional colors
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    End = '\033[0m'
    Default = '\033[99m'


class Ui:

    @staticmethod
    def get_input(text):
        user_input = input('Type ' + text + ': ')
        return user_input

    @staticmethod
    def clear():
        """clear screen"""

        os.system('cls' if os.name == 'nt' else 'clear')  # clear console

    @staticmethod
    def count_table_size(table, title_list):
        """counting table size, this method use only methon print_table"""

        cell_size = list()

        for i, title in enumerate(title_list):
            cell_size.append(len(title))

        for items in table:
            for i, item in enumerate(items):
                try:
                    if cell_size[i] < len(str(item)):
                        cell_size[i] = len(str(item))
                except:
                    cell_size.append(len(item))

        # how big table
        table_size = 1
        for dash in cell_size:
            table_size += (dash + 3)

        return table_size, cell_size

    @staticmethod
    def print_table(table, title_list):
        """
               Displays table

               Args:
                   table(list): table to print
                   title_list(list): headers for table
                Returns:
                   This function doesn't return anything it only prints to console.
        """

        # checking largest cells
        table_size = Ui.count_table_size(table, title_list)
        cell_size = table_size[1]
        table_size = table_size[0]

        print(Color.TableHead + '', '-' * table_size)

        for i, title in enumerate(title_list):
            if i == 0:
                print(' |', end="")
            print(' {:{width}} |'.format(title, width=cell_size[i]), end="")

        print('\n ' + '-' * table_size + Color.End)

        for items in table:
            for i, item in enumerate(items):
                if i == 0:
                    print(' |', end="")

                print(' {:{width}} |'.format(str(item), width=cell_size[i]), end="")
            print()

        print('', '-' * table_size)
        print()

    @staticmethod
    def print_head(message, type_of_header=''):
        """
        Displays header

        Args:
            message(str): message displayed
            type(str): type of message (accepts: header, error, warning)

        Returns:
            This function doesn't return anything it only prints to console.

        """

        message = '| ' + message + ' |'

        if type_of_header == 'header':
            print(Color.Header + '-' * len(message))  # separator
        elif type_of_header == 'warning':
            print(Color.Warning + '-' * len(message))  # separator
        elif type_of_header == 'error':
            print(Color.Error + '-' * len(message))  # separator
        else:
            print(Color.White + '-' * len(message))  # separator

        print(message)
        print('-' * (len(message)) + Color.End)  # separator

    @staticmethod
    def print_text(text):
        """
                Displays text

                Args:
                    text(str): text to display

                Returns:
                    This function doesn't return anything it only prints to console.

        """
        print(text)

    @staticmethod
    def get_inputs(list_labels):
        """
        Gets list of inputs from the user.
        Sample call:
            get_inputs(["Name","Surname","Age"],"Please provide your personal information")
        Sample display:
            Please provide your personal information
            Name <user_input_1>
            Surname <user_input_2>
            Age <user_input_3>

        Args:
            list_labels: list of strings - labels of inputs

        Returns:
            List of data given by the user. Sample return:
                [<user_input_1>, <user_input_2>, <user_input_3>]
        """
        inputs = []

        for label in list_labels:
            inputs.append(input(label + ' '))

        return inputs

    @staticmethod
    def get_pass(label):
        """
        hidden input from user
        :param: label
        return: users input
        """

        return getpass.getpass(label)

    @staticmethod
    def get_menu(menu, menu_from, menu_to):
        """
        printing menu from menu, menu from option to option
        :param menu:
        :param menu_from:
        :param menu_to:
        :return option:
        """
        while True:
            # os.system('clear')
            print(menu)
            try:

                option = input("Select an option: ")
                if menu_from > int(option) or int(option) > menu_to:
                    raise NameError('None option')
                else:
                    break
            except:
                print('Wrong select!')

        return option
