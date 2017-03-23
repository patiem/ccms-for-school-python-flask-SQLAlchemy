from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.secret_key = 'any random string'
# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.modules.mod_checkpoint.checkpoint_controller import checkpointcontroller
from app.modules.mod_attendance.attendance_controller import attendancecontroller
from app.modules.decorator import *
from app.modules.mod_submission.submission import Submission
from app.modules.mod_team.team_controller import teamcontroller
from app.modules.mod_user.user_controller import usercontroller
from app.modules.mod_student.student_controller import studentcontroller
from app.modules.mod_mentor.mentor_controller import mentorcontroller
from app.modules.mod_submission.submission_controller import submissioncontroller
from app.modules.mod_assigment.assigment_controller import assigmentcontroller
from app.modules.mod_statistic.statistics_controller import statistics

app.register_blueprint(checkpointcontroller)
app.register_blueprint(mentorcontroller)
app.register_blueprint(studentcontroller)
app.register_blueprint(statistics)
app.register_blueprint(attendancecontroller)
app.register_blueprint(teamcontroller)
app.register_blueprint(usercontroller)
app.register_blueprint(submissioncontroller)
app.register_blueprint(assigmentcontroller)
