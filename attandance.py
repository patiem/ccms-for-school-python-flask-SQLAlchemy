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
        cls.attendance_list = Common.read_file('csv/attendance.csv')


# Attendance.