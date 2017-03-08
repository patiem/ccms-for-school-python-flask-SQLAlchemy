from models.common import Common
from models.student import Student
import datetime
from models import sql


class Attendance:
    file = 'csv/attendance.csv'
    attendance_list = []

    def __init__(self, id_student, date, present):
        """
        Create Attendance object
        :param id_student: string (user id)
        :param date: string (date: DD.MM.YYYY)
        :param present: string (Present/Late/Absent)
        """
        self.id_student = id_student
        self.date = date
        self.present = present

    @classmethod
    def toggle_present(cls, student, choice):
        """
        Set the presence of a student
        :param student: Attendance object
        :param choice: string (1/2/3)
        :return: None
        """

        if choice == '1':
            student.present = 'Present'
        elif choice == '2':
            student.present = 'Late'
        elif choice == '3':
            student.present = 'Absent'

    @classmethod
    def save_attendance_list(cls):
        """
        Saves cls.attendance_list to .csv file
        :return: None
        """
        list_to_save = []
        for record in cls.attendance_list:
            list_to_save.append([record.id_student, record.date, record.present])

        Common.save_file(cls.file, list_to_save)

    @classmethod
    def create_new_day(cls):
        """
        Adds new day to attendance list.
        Creates new rows in attendance.csv for each student
        :return: None
        """
        today = str(datetime.date.today())

        for student in Student.object_list:
            cls.attendance_list.append(Attendance(student.idx, today, 'Absent'))

            query = 'INSERT INTO `Attendance`(`ID_STUDENT`,`DATE`,`STATUS`) VALUES (?,?,?)'
            params = list([student.idx, today, 'Absent'])

            sql.query(query, params)

    @classmethod
    def get_attendance_by_date(cls, date):
        """
        Returns a list of students with date and presence status
        :param date: string (date: DD.MM.YYYY)
        :return: string (list of students with date and presence status)
        """
        output_string = ''
        for attendance in cls.attendance_list:
            if attendance.date == date:
                for student in Student.object_list:
                    if student.id == attendance.id_student:
                        output_string += date + ' ' + student.name + ' ' + student.last_name + ' presence status: ' + \
                                         attendance.present + '\n'
        return output_string[:-1]

    @classmethod
    def get_student_attendance(cls, student_id):
        """
        Returns all students occurrence in attendance_list
        :param student_id: string (user id)
        :return: string (list of all instances)
        """
        output_string = ''
        for attendance in cls.attendance_list:
            if attendance.id_student == student_id:
                for student in Student.object_list:
                    if student.id == attendance.id_student:
                        output_string += attendance.date + ' ' + student.name + ' ' + student.last_name \
                                         + ' presence: ' + attendance.present + '\n'
                        break
        return output_string[:-1]

    @classmethod
    def create_attendance_list(cls, date):
        """
        Creates attendance_list with Attendance objects
        """
        attendance_list = []

        query = "SELECT * FROM `Attendance` WHERE `DATE`=?"
        params = [date]
        attendance = sql.query(query, params)
        # student_list = Student.students_list()

        # for student in student_list:
        #     attendance_list.append(cls(student.idx, date, student['STATUS']))
        if attendance:
            for student in attendance:
                attendance_list.append(Attendance(student['ID_STUDENT'], student['DATE'], student['STATUS']))

            return attendance_list
        return False

    @classmethod
    def students_engagement(cls):
        """
        Creates list with students attendance.
        Counts the presence of students.
        :return engagement_list: two dimensional list
        """
        engagement_list = []
        for student in Student.object_list:
            student_attendance = {'Present': 0, 'Late': 0, 'Absent': 0}
            for attendance in cls.attendance_list:
                if attendance.id_student == student.idx:
                    student_attendance[attendance.present] += 1
            engagement_list.append([student.name, student.last_name, str(student_attendance['Present']),
                                    str(student_attendance['Late']),
                                    str(student_attendance['Absent'])])
        return engagement_list

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
