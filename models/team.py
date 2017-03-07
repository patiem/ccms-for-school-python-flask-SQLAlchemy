from models import sql


class Team:
    teams_list = []

    def __init__(self, id_team, name, students_id):
        self.id_team = id_team
        self.name = name
        self.students_id = students_id

    @classmethod
    def create_teams_list(cls):
        """
        Creates teams_list with Team objects
        """
        query = 'SELECT * FROM `TEAMS`'
        teams = sql.query(query)
        if teams:
            for team in teams:
                id_team = team['ID']
                name = team['NAME']
                students_id = []
                query = "SELECT `ID_USER` FROM `Users_team` WHERE `ID_TEAM`='{}'".format(id_team)
                students = sql.query(query)
                if students:
                    for student in students:
                        students_id.append(student['ID_USER'])
                    cls.teams_list.append(Team(id_team, name, students_id))
                else:
                    cls.teams_list.append(Team(id_team, name, []))

    @classmethod
    def get_by_id(cls, team_id):
        """
        Returns Team object
        :param team_id: int - id of team which you object need
        :return: Team object
        """
        for team in cls.teams_list:
            if team.id_team == team_id:
                return team
        return False

    @classmethod
    def new_team(cls, name):
        """
        Send new team to DB & reload teams_list
        :param name: str - name of new team
        :return: None
        """
        query = "INSERT INTO `TEAMS`(`NAME`) VALUES ('{}');".format(name)
        sql.query(query)
        cls.clear_and_load_list()

    @classmethod
    def clear_and_load_list(cls):
        """
        Loads class attribute teams_list
        :return: None
        """
        cls.teams_list = []
        cls.create_teams_list()

    @classmethod
    def student_to_team(cls, team, student):
        """
        Adds student to team
        :param team: Team object
        :param student: Student object
        :return: None
        """
        id_t = team.id_team
        id_s = student.idx
        if student.id_team:
            query = "UPDATE `Users_team` SET ID_TEAM={} WHERE ID_USER={};".format(id_t, id_s)
        else:
            query = "INSERT INTO `Users_team`(`ID_TEAM`, `ID_USER`) VALUES ({}, {});".format(id_t, id_s)
        student.id_team = id_t
        sql.query(query)
        cls.clear_and_load_list()

    @classmethod
    def get_team_by_id(cls, team_id):
        """
        Returns Team object
        :param team_id: int - id of team which you object need
        :return: Team object
        """
        for team in cls.teams_list:
            if str(team.id_team) == str(team_id):
                return team
        return False

    @classmethod
    def find_student_team(cls, student_id):
        """

        :param student_id: int - id of team which you object need
        :return: team_id in which student is or False if he is not in team
        """
        query = "SELECT `id_team` FROM `Users_team` WHERE `user_id`=?;"
        params = [student_id]
        id_team = sql.query(query, params)[0][0]
        if id_team:
            return id_team
        return False
