from models.student import Student
from models.team import Team
from flask import Flask, request, session, render_template, redirect, url_for
from models.user import *


app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/checkpoint')
def checkpoint():
    return render_template('checkpoint.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        logged_user = User.login(request.form['user_login'], request.form['user_pass'])

        if logged_user is not None:

            user = {'id': logged_user['ID'], 'name': logged_user['Name'], 'surname': logged_user['Surname'],
                    'type': logged_user['Type'], 'ave_grade': Student.ave_grade_flask_version(logged_user['ID']),
                    'my_attendance': Student.my_attendance(logged_user['ID'])}

            session['user'] = user

    if 'user' in session:
        return render_template('index.html', user=session['user'])
    else:
        return render_template('login.html')


@app.route('/teams')
def teams():
    if 'user' in session:
        teams_list = Team.create_teams_list()
        students_list = Student.students_list()
        return render_template('teams.html', user=session['user'], teams=teams_list, students=students_list)
    else:
        return render_template('login.html')


@app.route('/add_to_team/<student_id><team_id>')
def add_to_team(student_id, team_id):

    # return '{} {}'.format(student_id, team_id)

    Team.add_student_to_team(student_id, team_id)

    return redirect('/teams')


@app.route('/attendance')
def attendance():
    return render_template('teams.html')


@app.route('/student_list')
def student_list():
    table = Student.create_student_list()
    student_object = User.return_by_id(1)
    if table:
        return render_template('student_list.html', table=table, student_object=student_object)
    return render_template('student_list.html')


if __name__ == "__main__":
    app.run(debug=True)
