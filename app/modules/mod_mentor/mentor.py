from app.modules.mod_user.user import *
from app.modules import sql


class Mentor(User):


    @classmethod
    def create_mentor_list(cls):
        table = Mentor.query.filter_by(Type='Mentor')
        return table

    @staticmethod
    def mentor_exist(idx):
        mentor = Mentor.query.filter_by(Type='Mentor', ID=idx).first()
        if mentor:
            return True
        else:
            return False