import hashlib
from app.modules import sql
from app import db


class User(db.Model):
    __tablename__ = 'Users'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Surname = db.Column(db.String)
    Email = db.Column(db.String)
    Telephone = db.Column(db.Integer)
    Password = db.Column(db.String)
    Type = db.Column(db.String)
    id_team_object = db.relationship('UsersTeam', backref='student', cascade='all, delete', lazy='joined')
    attendance_object = db.relationship('Attendance', backref='student', cascade='all, delete', lazy='joined')

    def __init__(self, idx, name, last_name, mail, telephone, type, password):
        """
        Create object
        :param idx: string (id of student)
        :param name: string (name of student)
        :param last_name: string (last name of student)
        :param mail: string  (mail of student)
        :param telephone: string (telephone number)
        :param password: string (encode password to usser account)
        """
        self.ID = idx
        self.Name = name
        self.Surname = last_name
        self.Email = mail
        self.Telephone = telephone
        self.Password = password
        self.Type = type

    @classmethod
    def return_mails(cls):
        """Return:
                List of objects with users Emails"""
        return db.session.query(User.Email).all()

    @classmethod
    def add_user(cls, data, user_type):
        """
        :param data: LIST (FORMAT: NAME, SURNAME, E-MAIL, TELEPHONE)
        :return:
        """
        data.append(User.encode('1'))
        cls.save_sql(data, user_type)

    @staticmethod
    def save_sql(data, user_type):
        """
        Save data to sql
        :param data: list (FORMAT : NAME, SURNAME, E-MAIL, TELEPHONE, PASSWORD)
        :return:
        """
        new_student = User(None, data[0], data[1], data[2], data[3], user_type, data[4], )
        db.session.add(new_student)
        db.session.commit()

    @classmethod
    def return_by_id(cls, idx):
        """
        Return object of passed id
        :param idx: int (id of object)
        :return: object
        """
        user_object = User.query.filter_by(ID=idx).first()
        return user_object

    @classmethod
    def create_object_list(cls):
        """
        Create list containing instance of class
        :return: None
        """
        raise NotImplementedError

    @staticmethod
    def remove_sql(idx):
        """
        Remove user from user table and his attendance by id
        :param idx: idx of user to remove
        :return: None
        """
        to_remove = User.query.filter_by(ID=idx).first()
        db.session.delete(to_remove)
        db.session.commit()

    def __str__(self):
        """
        :return: String representation for object
        """
        return 'ID: {}'.format(self.ID)

    @staticmethod
    def get_by_login_and_pass(login, password):
        """
        Get user object by login and pass from user table
        :param login: Login to check
        :param password: Password to check
        :return: Object
        """
        user = User.query.filter_by(Email=login, Password=password).first()
        if user:
            return user

    @staticmethod
    def update_sql(edit_list):
        edit_user = User.query.filter_by(ID=edit_list[4]).first()
        edit_user.Name = edit_list[0]
        edit_user.Surname = edit_list[1]
        edit_user.Email = edit_list[2]
        edit_user.Telephone = edit_list[3]
        db.session.commit()

    @staticmethod
    def login(user_login, user_pass):
        """
        login method
        :return Object of logged user
        """
        encoded_password = User.encode(user_pass)  # get passoword and encode using hash and salt

        if User.get_by_login_and_pass(user_login, encoded_password) is not None:

            return User.get_by_login_and_pass(user_login, encoded_password)

        else:
            return None

    @staticmethod
    def encode(password):
        """Encoding password using salt and hash sha256
        :param password:
        :return encoded_password:
        """
        _salt = "Coder"
        encoded_password = hashlib.sha256()
        encoded_password.update(_salt.encode('utf-8') + password.encode('utf-8'))
        encoded_password = encoded_password.digest()
        return str(encoded_password)

    def full_name(self):
        """Create full name from name ans surname"""
        return self.Name + ' ' + self.Surname