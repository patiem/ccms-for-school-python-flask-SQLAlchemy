from models.student import Student
# from flask import Flask, request, session, render_template,redirect, url_for, jsonify, json
# from models.user import User
from models.team import Team
from flask import Flask, request, session, render_template, redirect, url_for, jsonify
from models.user import *
from models.mentor import Mentor


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
    Team.add_student_to_team(student_id, team_id)
    return redirect('/teams')


@app.route('/remove_team/<team_id>')
def remove_team(team_id):
    Team.remove_team(team_id)
    return redirect('/teams')


@app.route('/add_team', methods=['POST'])
def add_team():
    name = request.form['new_team_name']
    Team.new_team(name)
    return redirect('/teams')


@app.route('/remove_from_team/<student_id>')
def remove_from_team(student_id):
    Team.remove_student_from_team(student_id)
    return redirect('/teams')


@app.route('/attendance')
def attendance():
    return render_template('teams.html')


@app.route('/student_list')
def student_list():
    table = Student.create_student_list()
    if table:
        return render_template('student_list.html', table=table, user=session['user'])
    return render_template('student_list.html', user=session['user'])


@app.route('/mentor_list')
def mentor_list():
    table = Mentor.create_mentor_list()
    if table:
        return render_template('mentor_list.html', table=table, user=session['user'])
    return render_template('mentor_list.html', user=session['user'])


@app.route('/edit', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        idx = request.json['Idx']
        user = User.return_by_id(idx)
        user_dict = {'id': idx,
                        'name': user.name,
                        'surname': user.last_name,
                        'e-mail': user.mail,
                        'telephone': user.telephone}
        return jsonify(user_dict)
    return 'lipa'


@app.route('/edit-form', methods=['POST', 'GET'])
def update_student():
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


@app.route('/save-user', methods=['POST'])
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


@app.route('/remove-user', methods=['POST'])
def remove_user():
    if request.method == 'POST':
        idx = request.json['Idx']
        User.remove_sql(idx)


if __name__ == "__main__":
    app.run(debug=True)
