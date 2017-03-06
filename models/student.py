from models.user import *
from models import sql


class Student(User):
    """
    Class represent student
    """
    object_list = []
    file = 'csv/students.csv'

    def __init__(self, idx, name, last_name, mail, telephone, password, id_team=''):
        """
        Create Student object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        """
        User.__init__(self, idx, name, last_name, mail, telephone, password)
        self.id_team = id_team

    @classmethod
    def create_object_list(cls):
        """
        Crete objects of class student from sql
        :return: None
        """
        query = """
                SELECT ID, Name, Surname, `E-mail`, Telephone, Password
                FROM Users
                WHERE Type = 'Student'"""
        data = sql.query(query)
        table = []

        if data:
            for row in data:
                table.append([row[0], row[1], row[2], row[3], row[4], row[5]])
            for line in table:
                team_id = []
                get_team_id = """
                                SELECT ID_TEAM
                                FROM Users_team
                                WHERE ID_USER = ?"""

                # for row in sql.query(get_team_id, [line[0]]):
                #     team_id = row[0]
                # line.append(team_id)
                # print(line)
                # new_object = cls(line[0], line[1], line[2], line[3], line[4], line[5], line[6])

                if sql.query(get_team_id, [line[0]]):
                    for row in sql.query(get_team_id, [line[0]]):
                        team_id = row[0]

                if team_id:
                    line.append(team_id)
                    new_object = cls(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                else:
                    new_object = cls(line[0], line[1], line[2], line[3], line[4], line[5])

                cls.object_list.append(new_object)


    @staticmethod
    def save_sql(data):
        """
        Save data to sql
        :param data: list (FORMAT : NAME, SURNAME, E-MAIL, TELEPHONE, PASSWORD)
        :return:
        """
        query = """
                INSERT INTO Users (Name, Surname, `E-mail`, Telephone, Password, Type)
                VALUES (?, ?, ?, ?, ?, 'Student')"""
        sql.query(query, data)

    @staticmethod
    def update_sql(edit_list):
        """
        :param edit_list: (FORMAT: E-MAIL, ATTRIBUTE, NEW VALUE)
        :return:
        """

        query = """
                  UPDATE Users
                  SET `{}` = ?
                  WHERE `E-mail` = ?
                  AND Type = 'Student'""".format(edit_list[1])
        sql.query(query, [edit_list[2], edit_list[0]])

    @staticmethod
    def avg_grade():
        """
        Count avg grade of students
        :return: Table (FORMAT: NAME, SURNAME, AVG GRADE)
        """
        query = """
                   SELECT Name, Surname, AVG(GRADE)
                   FROM Users as U
                   LEFT Join Sumbissions as S
                   ON U.ID = S.ID_Student
                   where Type = 'Student'
                   GROUP BY Name;"""
        sql_data = sql.query(query)
        table = []
        for row in sql_data:
            table.append([row[0], row[1], row[2]])
        return table
