from flask import Flask, render_template, request, session
from menu import Menu

app = Flask(__name__) # create the application instance :)

def main():
    Menu.run()

if __name__ == '__main__':
    main()
