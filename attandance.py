from common import Common
from student import Student


class Attendance:
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
    def toggle_present(cls, date, student_id, choice):
        """
        Set the presence of a student
        :param date: string (date: DD.MM.YYYY)
        :param student_id: string (user id)
        :param choice: string (1/2/3)
        :return: None
        """
        for student in cls.attendance_list:
            if student.id_student == student_id:
                if student.date == date:
                    if choice == '1':
                        student.present = 'Present'
                    elif choice == '2':
                        student.present = 'Late'
                    elif choice == '3':
                        student.present = 'Absent'
                    return

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
                for student in Student.students_list:
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
                for student in Student.students_list:
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
        student_list = Common.read_file('csv/attendance.csv')
        for student in student_list:
            cls.attendance_list.append(Attendance(student[0], student[1], student[2]))

#
#
# Student.create_student_list()
# Attendance.create_attendance_list()
# print(Attendance.attendance_list)
# print(Attendance.get_attendance_by_date('20.01.2017'))
# print(Attendance.get_student_attendance('1'))
# Attendance.toggle_present('2.03.2016', '1', '2')
# print(Attendance.get_student_attendance('1'))
# Attendance.toggle_present('5.8.2011', '1', '3')
#
# print(Attendance.get_student_attendance('1'))
#

