from flask import Flask, jsonify
from controllers.checkpoint_controller import checkpointcontroller
from models.student import Student
from models.team import Team
from models.user import *
from models.menu import StudentMenu
from models.assignment import Assignment
from models.submission import Submission
from models.mentor import Mentor

from models.decorator import *


app = Flask(__name__)
app.register_blueprint(checkpointcontroller)
app.secret_key = 'any random string'




@app.route('/checkpoint')
def checkpoint():
    return render_template('checkpoint.html')


@app.route('/assignments')
def show_assignments_list():
    # logged_user = make_student()
    if session['user']['type'] == 'Student':
        assignments = StudentMenu.assignment_list_with_grades(session['user']['id'])
        return render_template('assignments.html', user=session['user'], assignments=assignments)
    elif session['user']['type'] == 'Mentor':
        assignments = Assignment.pass_assign_for_mentor()
        return render_template('assignments_mentor.html', user=session['user'], assignments=assignments)


@app.route('/assignments/<idx>', methods=['GET', 'POST'])
def show_assignment(idx):
    # logged_user = make_student()
    assignment = Assignment.get_by_id(int(idx))
    submission = Submission.find_submission_sql(idx, session['user']['id'])
    if request.method == 'GET':
        return render_template('submissions.html', user=session['user'], assignment=assignment, submission=submission)
    elif request.method == 'POST':
        link = request.form['link']
        comment = request.form['comment']
        Submission.add_submission(session['user']['id'], assignment[0], link, comment)
        return redirect(url_for('show_assignment', idx=idx))

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
            print(session['user']['id'])

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
        return redirect('/logout')


@app.route('/add_to_team/<student_id><team_id>')
def add_to_team(student_id, team_id):
    if 'user' in session:
        Team.add_student_to_team(student_id, team_id)
        return redirect('/teams')
    else:
        return redirect('/logout')


@app.route('/remove_team/<team_id>')
def remove_team(team_id):
    if 'user' in session:
        Team.remove_team(team_id)
        return redirect('/teams')
    else:
        return redirect('/logout')


@app.route('/add_team', methods=['POST'])
def add_team():
    if 'user' in session:
        name = request.form['new_team_name']
        Team.new_team(name)
        return redirect('/teams')
    else:
        return redirect('/logout')


@app.route('/remove_from_team/<student_id>')
def remove_from_team(student_id):
    if 'user' in session:
        Team.remove_student_from_team(student_id)
        return redirect('/teams')
    else:
        return redirect('/logout')


@app.route('/attendance')
def attendance():
    return render_template('attendance.html', user=session['user'])


@app.route('/student_list')
@login_required
@correct_type(['Manager', 'Employee', 'Mentor'])
def student_list():
    table = Student.students_list()
    if table:
        return render_template('student_list.html', table=table, user=session['user'])
    return render_template('student_list.html', user=session['user'])


@app.route('/mentor_list')
@login_required
@correct_type(['Manager'])
def mentor_list():
    table = Mentor.create_mentor_list()
    if table:
        return render_template('mentor_list.html', table=table, user=session['user'])
    return render_template('mentor_list.html', user=session['user'])


@app.route('/edit', methods=['POST', 'GET'])
@login_required
@correct_type(['Manager', 'Mentor'])
def get_data():
    if request.method == 'POST':
        idx = request.json['Idx']
        user = User.return_by_id(idx)
        user_dict= {'id': idx,
                    'name': user.name,
                    'surname': user.last_name,
                    'e-mail': user.mail,
                    'telephone': user.telephone}
        return jsonify(user_dict)
    return 'lipa'


@app.route('/edit-form', methods=['POST', 'GET'])
@login_required
@correct_type(['Manager', 'Mentor'])
@correct_form(['type', 'id', 'name', 'surname', 'email', 'telephone'])
def update_user():
    if request.method == 'POST':
        user_type = request.form['type']
        idx = request.form['id']
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        telephone = request.form['telephone']
        edit_list = [name, surname, email, telephone, idx]
        if user_type == 'student':
            Student.update_sql(edit_list)
            return redirect(url_for('student_list'))
        elif user_type == 'mentor':
            Mentor.update_sql(edit_list)
            return redirect(url_for('mentor_list'))
        else:
            return render_template('bad.html')


@app.route('/save-user', methods=['POST', 'GET'])
@login_required
@correct_type(['Manager', 'Mentor'])
@correct_form(['type', 'name', 'surname', 'email', 'telephone'])
def save_user():
    if request.method == 'POST':
        user_type = request.form['type']
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        telephone = request.form['telephone']
        add_list = [name, surname, email, telephone]
        if user_type == 'student':
            Student.add_user(add_list)
            return redirect(url_for('student_list'))
        elif user_type == 'mentor':
            Mentor.add_user(add_list)
            return redirect(url_for('mentor_list'))
        else:
            return render_template('bad.html')


@app.route('/remove-user', methods=['POST', 'GET'])
@login_required
@correct_type(['Manager', 'Mentor'])
@correct_json(['Idx'])
def remove_user():
    if request.method == 'POST':
        idx = request.json['Idx']
        User.remove_sql(idx)


@app.route('/check-mail', methods=['POST'])
@login_required
@correct_type(['Manager', 'Mentor'])
@correct_json(['Mail'])
def mail_exist():
        if request.method == 'POST':
            if request.is_json:
                mail_list = User.return_mails()
                if request.json['Mail'] in mail_list:
                    value = {'value': True}
                    return jsonify(value)
                else:
                    value = {'value': False}
                    return jsonify(value)
            return redirect(url_for('index'))
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
