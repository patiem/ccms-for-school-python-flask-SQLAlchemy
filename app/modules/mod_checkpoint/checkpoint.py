from app import db
from app.modules import sql
import datetime


class Checkpoint(db.Model):

    __tablename__ = "Checkpoints"
    ID = db.Column(db.Integer, primary_key=True)
    ID_USER = db.Column(db.Integer)
    TITLE = db.Column(db.String)
    START_DATE = db.Column(db.String)
    USERS_CHECKPOINTS = db.relationship("Users_checkpoints", backref="current_checkpoint", lazy='dynamic')


    @staticmethod
    def select_mentors_not_in_checkpoint(checkpoint_id):

        query = "SELECT * FROM Users WHERE `TYPE` = 'Mentor' AND `ID` NOT IN (SELECT ID_USER FROM Checkpoints WHERE ID={})".format(
            checkpoint_id)
        sql_result = sql.query(query)

        return sql_result

    @staticmethod
    def make_checkpoint(mentor1, mentor2, student, checkpoint_id, grade):

        today = datetime.date.today()

        query = "INSERT INTO Users_checkpoints " \
                "(ID_CHECKPOINT, DATE, GRADE, ID_STUDENT, ID_MENTOR_1, ID_MENTOR_2)" \
                " VALUES (?, ?, ?, ?, ?, ?)"
        params = [checkpoint_id, today, grade, int(student), int(mentor1), int(mentor2)]
        sql.query(query, params)

    @staticmethod
    def show_checkpoints():

        query = "SELECT * FROM Checkpoints, Users WHERE Checkpoints.ID_USER = Users.ID"

        sql_query_result = sql.query(query)
        return sql_query_result


    @staticmethod
    def show_checkpoint_results(checkpoint_id):
        if checkpoint_id != 0:

            query = "SELECT TITLE, ID_CHECKPOINT, DATE, GRADE, student.Name as student_name,  " \
                    "student.Surname as student_surname , mentor.Name as mentor_name,  " \
                    "mentor.Surname as mentor_surname , mentor2.Name as mentor2_name,  " \
                    "mentor2.Surname as mentor2_surname " \
                    "FROM Users_checkpoints LEFT JOIN Users  student ON Users_checkpoints.ID_STUDENT = student.ID " \
                    "LEFT JOIN Users  mentor ON Users_checkpoints.ID_MENTOR_1 = mentor.ID " \
                    "LEFT JOIN Users  mentor2 ON Users_checkpoints.ID_MENTOR_2 = mentor2.ID " \
                    "LEFT JOIN Checkpoints ON Users_checkpoints.ID_CHECKPOINT = Checkpoints.ID " \
                    "WHERE ID_CHECKPOINT  = {}".format(checkpoint_id)

            table = []
            sql_query_result = sql.query(query)

            if isinstance(sql_query_result, list):

                for checkpoint in sql_query_result:
                    table.append({'student': checkpoint['student_name'] + ' ' + checkpoint['student_surname'],
                                  'mentor1': checkpoint['mentor_name'] + ' ' + checkpoint['mentor_surname'],
                                  'mentor2': checkpoint['mentor2_name'] + ' ' + checkpoint['mentor2_surname'],
                                  'date': checkpoint['DATE'],
                                  'grade': checkpoint['grade']
                                  })

                return table

    @staticmethod
    def show_statistics_for_mentor_cards(id_mentor):

        query = "SELECT *, COUNT(GRADE) as cards FROM Users_checkpoints WHERE ID_MENTOR_1 = {} OR ID_MENTOR_2 = {} " \
                "GROUP BY grade".format(id_mentor, id_mentor)

        sql_query_result = sql.query(query)

        return sql_query_result

    @staticmethod
    def show_statistics_for_mentor_checkpoints(id_mentor):

        query = "SELECT * FROM Checkpoints WHERE ID_USER = {} ORDER BY START_DATE ASC".format(
            id_mentor, id_mentor)

        sql_query_result = sql.query(query)

        return sql_query_result


class Users_checkpoints(db.Model):

    __tablename__ = "Users_checkpoints"
    ID = db.Column(db.Integer, primary_key=True)
    ID_CHECKPOINT = db.Column(db.Integer,  db.ForeignKey('Checkpoints.ID'))
    DATE = db.Column(db.String(20))
    GRADE = db.Column(db.String(20))
    ID_STUDENT = db.Column(db.Integer, db.ForeignKey('Users.ID'))
    ID_MENTOR_1 = db.Column(db.Integer)
    ID_MENTOR_2 = db.Column(db.Integer)
