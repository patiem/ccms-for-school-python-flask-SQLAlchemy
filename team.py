import sql


class Team:
    teams_list = []

    def __init__(self, id_team, name, students_id):
        self.id_team = id_team
        self.name = name
        self.students_id = students_id

    # @classmethod
    # def create_teams_list(cls):
    #     """
    #     Creates teams_list with Team objects
    #     """
    #     query = "SELECT * FROM `TEAMS`"
    #
    #     student_list = sql.query(query)
    #     for student in student_list:
    #         cls.teams_list.append(Team())
