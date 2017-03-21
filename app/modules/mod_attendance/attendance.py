import datetime

from app.modules import sql
from app.modules.mod_student.student import Student


class Attendance:

    def __init__(self, id_student, fullname, date, present):
        """
        Create Attendance object
        :param id_student: string (user id)
        :param date: string (date: DD.MM.YYYY)
        :param present: string (Present/Late/Absent)
        """
        self.id_student = id_student
        self.fullname = fullname
        self.date = date
        self.present = present

    @classmethod
    def create_attendance_list(cls, date):
        """
        Creates attendance_list with Attendance objects
        """
        attendance_list = []

        query = "SELECT * FROM `Attendance` WHERE `DATE`=?"
        params = [date]
        attendance = sql.query(query, params)

        if attendance:
            for student in attendance:
                user = Student.return_by_id(int(student['ID_STUDENT']))
                fullname = user.full_name()
                attendance_list.append(Attendance(student['ID_STUDENT'], fullname, student['DATE'], student['STATUS']))

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

        query = "SELECT * FROM `Attendance` WHERE `DATE`=?"
        params = [date]
        attendance = sql.query(query, params)

        if today == date:
            if attendance:
                pass
            else:
                for student in Student.students_list():
                    query = """INSERT INTO `Attendance`(`ID`,`ID_STUDENT`,`DATE`,`STATUS`) VALUES (NULL,?,?,'None');"""
                    params = [student.idx, today]
                    sql.query(query, params)
        list_of_attendance = Attendance.create_attendance_list(date)

        # ------------------------- EXAMPLE USE -------------------------- #

        # attendance_list = Attendance.get_attendance_list('2016-10-00')
        # if attendance_list:
        #     for student in attendance_list:
        #         print(student.id_student, student.date, student.present)

        # ---------------------------------------------------------------- #

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

