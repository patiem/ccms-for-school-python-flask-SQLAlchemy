from app.modules import sql
from app.modules.mod_student.student import Student
from app import db


class Team(db.Model):
    # teams_list = []

    __tablename__ = "TEAMS"
    ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String, nullable=False)
    students = db.relationship('UsersTeam', backref='team', lazy='dynamic')

    def __init__(self, id_team, name, students):
        self.ID = id_team
        self.NAME = name
        self.students = students

    @staticmethod
    def create_teams_list():
        """
        Creates teams_list with Team objects
        """
        list_from_db = Team.query.all()
        return list_from_db

    # @classmethod
    # def get_by_id(cls, team_id):
    #     """
    #     Returns Team object
    #     :param team_id: int - id of team which you object need
    #     :return: Team object
    #     """
    #     for team in cls.teams_list:
    #         if team.ID == team_id:
    #             return team
    #     return False

    @classmethod
    def new_team(cls, name):
        """
        Send new team to DB & reload teams_list
        :param name: str - name of new team
        :return: None
        """
        new_team = Team(None, name, [])
        db.session.add(new_team)
        db.session.commit()

    # @classmethod
    # def clear_and_load_list(cls):
    #     """
    #     Loads class attribute teams_list
    #     :return: None
    #     """
    #     cls.teams_list = []
    #     cls.create_teams_list()

    @classmethod
    def student_to_team(cls, team, student):
        """
        Adds student to team
        :param team: Team object
        :param student: Student object
        :return: None
        """
        id_t = team.ID
        id_s = student.ID
        if student.id_team:
            query = "UPDATE `Users_team` SET ID_TEAM={} WHERE ID_USER={};".format(id_t, id_s)
        else:
            query = "INSERT INTO `Users_team`(`ID_TEAM`, `ID_USER`) VALUES ({}, {});".format(id_t, id_s)
        student.id_team = id_t
        sql.query(query)
        # cls.clear_and_load_list()

    @classmethod
    def get_team_by_id(cls, team_id):
        """
        Returns Team object
        :param team_id: int - id of team which you object need
        :return: Team object
        """
        teams_list = cls.create_teams_list()

        for team in teams_list:
            if str(team.ID) == str(team_id):
                return team
        return False

    @classmethod
    def find_student_team(cls, student_id):
        """

        :param student_id: int - id of team which you object need
        :return: team_id in which student is or False if he is not in team
        """
        team_id = db.session.query(UsersTeam.ID_TEAM).filter(UsersTeam.ID_USER == student_id).first()
        if team_id:
            team_id = team_id[0]
        return team_id

    @staticmethod
    def add_student_to_team(student_id, team_id):
        """
        Lets user to move student between teams
        :return: None
        """
        student = Student.return_by_id(student_id)
        if student:
            student_team = Team.get_team(student.ID)
            student.id_team = student_team
            team = Team.get_team_by_id(int(team_id))
            if team:
                Team.student_to_team(team, student)
            else:
                print('There is no team with this ID')
        else:
            print('There is no student with this ID')

    @staticmethod
    def remove_team(team_id):
        query = "DELETE FROM `TEAMS` WHERE `ID` = {};".format(int(team_id))
        sql.query(query)

        query = "DELETE FROM `Users_team` WHERE `ID_TEAM` = {};".format(int(team_id))
        sql.query(query)

    @staticmethod
    def add_new_team(team_name):
        """
        Adds new team
        :return: None
        """

        name = team_name
        if name == '' or '\t' in name or len(name) < 3 or name[0] == ' ' or '  ' in name:

            return 'Wrong name format'

        Team.new_team(name)

    @staticmethod
    def remove_student_from_team(student_id):
        query = "DELETE FROM `Users_team` WHERE `ID_USER` = {};".format(int(student_id))
        sql.query(query)

    @classmethod
    def get_team_members(cls, team_id):
        query = "SELECT ID_USER FROM users_team WHERE ID_TEAM=?"
        params = [team_id]
        return sql.query(query, params)

    @staticmethod
    def update_name(idx, team_name):
        edited_team = Team.query.filter_by(ID=idx).first()
        edited_team.NAME = team_name
        db.session.commit()

    @classmethod
    def get_team(cls, idx):

        team = UsersTeam.query.filter_by(ID_USER=idx).first()
        if team:
            return team.ID_TEAM

    @staticmethod
    def dict_with_students_id(teams_list):
        """
        Returns dict {team_id: [users_ids]}
        :param teams_list: list with Team objects
        :return dict_with_ids: dict {team_id: [users_ids]}
        """
        dict_with_ids = {}
        for team in teams_list:
            students_ids = []
            for student in team.students:
                students_ids.append(student.ID_USER)
            dict_with_ids[team.ID] = students_ids
        return dict_with_ids


class UsersTeam(db.Model):

    __tablename__ = "Users_team"
    ID = db.Column(db.Integer, primary_key=True)
    ID_TEAM = db.Column(db.Integer, db.ForeignKey('TEAMS.ID'))
    ID_USER = db.Column(db.Integer, nullable=False)
    # TEAM = db.Column(db.Integer, db.ForeignKey('TEAMS'))

    def __init__(self, idx, id_team, id_user):
        self.ID = idx
        self.ID_TEAM = id_team
        self.ID_USER = id_user
