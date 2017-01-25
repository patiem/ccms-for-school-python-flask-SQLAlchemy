from menu import *
from ui import *
from user import *
from menu import Menu


def main():
    print('Pass for everyone is: 1')
    logged_user = User.login()

    print('You are logged as:', logged_user[1])
    print('You are:', logged_user[3])

    # Menu.run(logged_user)

    menu = """What do you want to do?

       (1) First Option
       (2) Second option
       (3) Third option

       (0) Exit program
       """

    option = Ui.get_menu(menu, 0, 3)
    print("You selected ", option)


if __name__ == '__main__':
    main()
