from menu import *
from ui import *
from user import *

def main():

    print('Pass for everyone is: 1')
    logged_user = User.login()

    print('You are logged as:', logged_user[1])
    print('You are:', logged_user[3])


if __name__ == '__main__':
    main()
