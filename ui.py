import os
import getpass

class color:
    """Simple Class of coloring text"""

    #terminal design
    Header = '\033[92m'
    Warning = '\033[93m'
    Error = '\033[91m'

    TableHead = '\033[92m'

    #additional colors
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

        print(color.TableHead + '', '-' * table_size)

        for i, title in enumerate(title_list):
            if i == 0:
                print(' |', end="")
            print(' {:{width}} |'.format(title, width=cell_size[i]), end="")

        print('\n ' + '-' * table_size + color.End )

        for items in table:
            for i, item in enumerate(items):
                if i == 0:
                    print(' |', end="")

                print(' {:{width}} |'.format(str(item), width=cell_size[i]), end="")
            print()

        print('', '-' * table_size)
        print()

    @staticmethod
    def print_head(message, type = ''):
        """
        Displays header

        Args:
            message(str): message displayed
            type(str): type of message (accepts: header, error, warning)

        Returns:
            This function doesn't return anything it only prints to console.

        """

        message = '| '+message+ ' |'

        if type == 'header':
            print(color.Header + '-' * len(message))  # separator
        elif type == 'warning':
            print(color.Warning + '-' * len(message))  # separator
        elif type == 'error':
            print(color.Error + '-' * len(message))  # separator
        else:
            print(color.White + '-' * len(message))  # separator

        print(message)
        print('-' * (len(message)) + color.End)  # separator

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
            title: title of the "input section"

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

        return getpass.getpass(label)

#Examples of using Ui

# Ui.clear() #clearing site
#
# table = list([['cell 1', 'cell 2', 'cell 3'], ['cell 1', 'cell 2', 'cell 3']])
# table_title = list(['title 1', 'title 2', 'title 3'])
#
# Ui.print_table(table, table_title) #displaying table
# Ui.print_head('To jest error', 'error' ) #displaying errors
# Ui.print_head('To jest header', 'header') #displaying header of site
# Ui.print_head('To jest warning', 'warning') #displaying header of site

# Ui.print_text("Simple text to print \n\n")
#
# inputs = ['First input', 'Second input', 'Third input']
# print(Ui.get_inputs(inputs))