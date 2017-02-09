import sql


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
        query = "SELECT * FROM `TEAMS`"
        teams = sql.query(query)

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
    def new_team(cls):

        pass
