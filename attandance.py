from common import Common
from student import Student
import datetime


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

        cls.save_attendance_list()

    @classmethod
    def save_attendance_list(cls):
        list_to_save = []
        for record in cls.attendance_list:
            list_to_save.append([record.id_student, record.date, record.present])

        Common.save_file(cls.file, list_to_save)

    @classmethod
    def create_new_day(cls):
        today = str(datetime.date.today())
        for student in Student.object_list:
            cls.attendance_list.append(Attendance(student.idx, today, 'Absent'))
        cls.save_attendance_list()




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
                        output_string += date + ' ' + student.name + ' ' + student.last_name + ' presence status: ' +\
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
    def create_attendance_list(cls):
        """
        Creates attendance_list with Attendance objects
        """
        student_list = Common.read_file(cls.file)
        for student in student_list:
            cls.attendance_list.append(Attendance(student[0], student[1], student[2]))

    @classmethod
    def students_engagement(cls):
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
