from app.modules.mod_student.student import Student
from app import db


class Team(db.Model):
    """
    Class of Team
    """

    __tablename__ = "TEAMS"

    ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String, nullable=False)
    students = db.relationship('UsersTeam', backref='team', cascade='all, delete', lazy='dynamic')

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

    @classmethod
    def student_to_team(cls, team, student):
        """
        Adds student to team
        :param team: Team object
        :param student: Student object
        :return: None
        """
        user_team = UsersTeam.query.filter_by(ID_USER=student.ID).first()

        if user_team:
            user_team.ID_TEAM = team.ID
            return db.session.commit()
        new_user_to_team = UsersTeam(team=team, ID_USER=student.ID)
        db.session.add(new_user_to_team)
        db.session.commit()

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
        """
        Removes team from db
        :param team_id: int
        """
        team_to_remove = Team.query.filter_by(ID=team_id).first()
        db.session.delete(team_to_remove)
        db.session.commit()

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
        """
        Removes student from `Users_team` table
        :param student_id: int
        """
        remove_student = UsersTeam.query.filter_by(ID_USER=student_id).first()
        db.session.delete(remove_student)
        db.session.commit()

    @staticmethod
    def update_name(idx, team_name):
        """
        Updates name of team in `TEAMS` table
        :param idx: int
        :param team_name: str
        """
        edited_team = Team.query.filter_by(ID=idx).first()
        edited_team.NAME = team_name
        db.session.commit()

    @classmethod
    def get_team(cls, idx):
        """
        Returns Team ID where is Student with 'idx'
        :param idx: int
        :return: Team ID (int) / None
        """

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
    """
    Class of UsersTeam
    """

    __tablename__ = "Users_team"

    ID = db.Column(db.Integer, primary_key=True)
    ID_USER = db.Column(db.Integer, db.ForeignKey('Users.ID'))
    ID_TEAM = db.Column(db.Integer, db.ForeignKey('TEAMS.ID'))
