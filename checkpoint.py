from ui import Ui
from common import Common
import sql


class Checkpoint:

    @staticmethod
    def add_checkpoint(user_object):

        Ui.clear()

        Ui.print_head('Add new checkpoint', 'header')

        title = Ui.get_input('Subject of checkpoint')
        start_date = Common.make_corect_date(Ui.get_input('start date(YYYY-MM-DD)'))

        query = "INSERT INTO Checkpoints ('ID_USER', 'TITLE', 'START_DATE') VALUES (?, ?, ?)"
        sql.query(query, [user_object.idx, title, start_date])

    @staticmethod
    def make_checkpoint():

        pass

    @staticmethod
    def show_checkpoints(user_object):
        Ui.clear()

        Ui.print_head('Created checkpoints', 'header')

        query = "SELECT * FROM Checkpoints, Users WHERE Checkpoints.ID_USER == Users.ID"
        titles = ['ID', 'Subject', 'Created by', 'Start date']
        checkpoints = []

        for checkpoint in sql.query(query):
            checkpoints.append([checkpoint['ID'], checkpoint['TITLE'], checkpoint['NAME'] + checkpoint['SURNAME'], checkpoint['START_DATE']])

        Ui.print_table(checkpoints, titles)
        input()

    @staticmethod
    def show_checkpoint_by_id(ID):

        pass

    @staticmethod
    def make_checkpoint(user_object):

        pass
