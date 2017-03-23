from app.modules.mod_user.user import *
from app.modules import sql


class Student(User):
    """
    Class represent student
    """ 

    def __init__(self, idx, name, last_name, mail, telephone, type, password, id_team=''):
        """
        Create Student object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        User.__init__(self, idx, name, last_name, mail, telephone, type, password)
        self.id_team = id_team

    def full_name(self):
        return self.Name + ' ' + self.Surname

    @staticmethod
    def save_sql(data):
        """
        Save data to sql
        :param data: list (FORMAT : NAME, SURNAME, E-MAIL, TELEPHONE, PASSWORD)
        :return:
        """
        new_student = Student(None, data[0], data[1], data[2], data[3],'Student', data[4], )
        db.session.add(new_student)
        db.session.commit()

    @staticmethod
    def get_students_without_checkpoint(checkpoint_id):
        """
        :param checkpoint_id:
        :return: list_of_students
        """
        query = "SELECT * FROM Users WHERE ID NOT  IN (SELECT ID_STUDENT FROM Users_checkpoints WHERE ID_CHECKPOINT = {}) AND Type='Student'".format(checkpoint_id)
        students = sql.query(query)

        return students

    @staticmethod
    def ave_grade_flask_version(idx):
        """
        Count avg grade of students
        :param idx: index of studentSELECT * FROM Users WHERE ID NOT  IN (SELECT ID_STUDENT FROM Users_checkpoints WHERE ID_CHECKPOINT = 1) AND Type='Student'
        :return average grade (int):
        """
        query = """
                   SELECT U.ID, Name, Surname, AVG(GRADE)
                   FROM Users as U
                   LEFT Join Sumbissions as S
                   ON U.ID = S.ID_Student
                   where Type = 'Student'
                   GROUP BY Name;"""
        sql_data = sql.query(query)
        for row in sql_data:
            student_id = row[0]
            if int(student_id) == int(idx):
                if row[3]:
                    return int(row[3])
                else:
                    return

    @staticmethod
    def get_students_attandance():

        students = Student.students_list()

        table = []
        for student in students:
            table.append([student.name, student.last_name, Student.my_attendance(student.idx)])
        return table

    @staticmethod
    def get_students_grades():
        students = Student.students_list()
        table = []
        for student in students:
            table.append([student.name, student.last_name, Student.ave_grade_flask_version(student.idx)])
        return table

    @staticmethod
    def my_attendance(idx):
        query = 'SELECT STATUS, COUNT(STATUS) AS count FROM `Attendance` WHERE ID_STUDENT=? GROUP BY STATUS'
        values = [int(idx)]
        back_values = sql.query(query, values)
        to_print =[]
        all_days = 0
        average = 0
        if back_values:
            for row in back_values:
                to_print.append([row[0], row[1]])
                if row[0] == 'Present':
                    average += 1
                elif row[0] == 'Late':
                    average += 0.75
                all_days += row[1]

            return int(average * 100 / all_days)
        else:
            pass

    @staticmethod
    def students_list():
        """
        Crete objects of class student from sql
        :return: None
        """
        student_list = Student.query.filter_by(Type='Student')
        for student in student_list:
            print(student.id_team)
        return student_list

    @classmethod
    def make_student(cls, user_id):
        if cls.return_by_id(user_id):
            logged_user = cls.return_by_id(user_id)  # what with team id??
            return logged_user
        return False
