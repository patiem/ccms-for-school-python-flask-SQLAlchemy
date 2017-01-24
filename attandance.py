from common import Common


class Attendance:
    attendance_list = []

    def __int__(self, id_student, date, present):
        self.id_student = id_student
        self.date = date
        self.present = present

    def toggle_present(self):
        pass

    def get_attendance_by_date():
        pass

    def get_student_attendance():
        pass

    @classmethod
    def create_attendance_list(cls):
        student_list = Common.read_file('csv/attendance.csv')
        for student in student_list:
            print(student[0])
            print(student[1])
            print(student[2])
            # cls.attendance_list.append(Attendance(student[0], student[1], student[2]))
            # cls.attendance_list = Common.read_file('csv/attendance.csv')


Attendance.create_attendance_list()
# print(Attendance.attendance_list)
