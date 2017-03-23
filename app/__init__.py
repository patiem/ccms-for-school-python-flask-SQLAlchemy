from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.secret_key = 'any random string'
# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.modules.mod_checkpoint.checkpoint import *
from app.modules.mod_checkpoint.checkpoint_controller import checkpointcontroller
from app.modules.mod_statistic.statistics_controller import statistics
from app.modules.mod_attendance.attendance_controller import attendancecontroller
from app.modules.decorator import *
from app.modules.mod_team.team import Team
from app.modules.mod_assigment.assignment import Assignment
from app.modules.mod_submission.submission import Submission
from app.modules.mod_attendance.attendance import Attendance
from app.modules.mod_team.team_controller import teamcontroller
from app.modules.mod_user.user_controller import usercontroller
from app.modules.mod_student.student_controller import studentcontroller
from app.modules.mod_mentor.mentor_controller import mentorcontroller
from app.modules.mod_submission.submission_controller import submissioncontroller

app.register_blueprint(checkpointcontroller)
app.register_blueprint(mentorcontroller)
app.register_blueprint(studentcontroller)
app.register_blueprint(statistics)
app.register_blueprint(attendancecontroller)
app.register_blueprint(teamcontroller)
app.register_blueprint(usercontroller)
app.register_blueprint(submissioncontroller)


@app.route('/assignments', methods=['GET', 'POST'])
@login_required
@correct_type(['Student', 'Mentor'])
def show_assignments_list():
    if session['user']['type'] == 'Student':
        assignments = Assignment.assignment_list_with_grades(session['user']['id'])
        return render_template('assignments/assignments.html', user=session['user'], assignments=assignments)

    elif session['user']['type'] == 'Mentor':
        if request.method == 'GET':
            assignments = Assignment.pass_assign_for_mentor()
            return render_template('assignments/assignments_mentor.html', user=session['user'], assignments=assignments)
        elif request.method == 'POST':
            title = request.form['a_title']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            group = request.form['group']
            description = request.form['description']
            Assignment.add_assignment(title, session['user']['id'], start_date, end_date, description, group)
            return redirect(url_for('show_assignments_list'))


@app.route('/assignments/<idx>', methods=['GET', 'POST'])
@login_required
@correct_type(['Student', 'Mentor'])
def show_assignment(idx):
    assignment = Assignment.get_by_id(int(idx))
    submission = Submission.find_submission_sql(idx, session['user']['id'])
    if request.method == 'GET':
        return render_template('submission/submissions.html', user=session['user'], assignment=assignment, submission=submission)
    elif request.method == 'POST':
        link = request.form['link']
        comment = request.form['comment']
        Submission.add_submission(session['user']['id'], assignment[0], link, comment, assignment[6])
        return redirect(url_for('show_assignment', idx=idx))
