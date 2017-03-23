import datetime
from app.modules import sql
from app.modules.mod_student.student import Student
from app import db


class Attendance(db.Model):

    __tablename__ = "Attendance"
    ID = db.Column(db.Integer, primary_key=True)
    ID_STUDENT = db.Column(db.Integer, nullable=False)
    DATE = db.Column(db.String, nullable=False)
    STATUS = db.Column(db.String, nullable=False)

    def __init__(self, id_student, date, fullname='', status='None'):
        """
        Create Attendance object
        :param id_student: string (user id)
        :param date: string (date: DD.MM.YYYY)
        :param status: string (Present/Late/Absent)
        """
        self.ID_STUDENT = id_student
        self.fullname = fullname
        self.DATE = date
        self.STATUS = status

    @classmethod
    def create_attendance_list(cls, date):
        """
        Creates attendance_list with Attendance objects
        """
        attendance_list = []

        attendance = Attendance.query.filter_by(DATE=date).all()

        if attendance:
            for student in attendance:
                user = Student.query.filter_by(ID=student.ID_STUDENT).first()
                fullname = user.full_name()
                attendance_list.append(Attendance(student.ID_STUDENT, fullname, student.DATE, student.STATUS))

            return attendance_list
        return False

    @staticmethod
    def get_attendance_list(date):
        """
        Sets the state of the presence each student at today
        :param date: str 'YYYY-MM-DD'
        :return list_of_attendance: list with Attendance objects
        """

        # EXAMPLE: today = '2017-03-07', date = '2017-03-07'
        today = str(datetime.date.today())
        attendance = Attendance.query.filter_by(DATE=date).first()

        if today == date:
            if attendance:
                pass
            else:
                for student in Student.students_list():
                    new_attendance = Attendance(id_student=student.ID, date=today)
                    db.session.add(new_attendance)
                db.session.commit()
        list_of_attendance = Attendance.create_attendance_list(date)

        return list_of_attendance

    @classmethod
    def update(cls, students_dict, date):  # IN USE

        # ----------- SQL UPDATE EXAMPLE ------------
        # """UPDATE `Attendance` SET `STATUS`='None'
        # WHERE `ID_STUDENT`=12
        # AND `DATE`='2017-03-09';"""
        # -------------------------------------------

        for idx in students_dict:

            query = """UPDATE `Attendance` SET `STATUS`=?
                       WHERE `ID_STUDENT`=? AND `DATE`=?;"""

            params = [students_dict[idx], idx, date]
            sql.query(query, params)

