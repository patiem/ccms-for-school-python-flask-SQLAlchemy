from flask import Flask, request, session, render_template,redirect, url_for, jsonify, Blueprint
from controllers.checkpoint_controller import checkpointcontroller
from models.student import Student
from models.user import User
from models.team import Team


app = Flask(__name__)
app.register_blueprint(checkpointcontroller)
app.secret_key = 'any random string'


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


@app.route('/attendance')
def attendance():
    return render_template('teams.html')


@app.route('/student_list')
def student_list():
    table = Student.create_student_list()
    if table:
        return render_template('student_list.html', table=table, user=session['user'])
    return render_template('student_list.html', user=session['user'])



@app.route('/edit', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        idx = request.json['Idx']
        student = Student.return_by_id(idx)
        student_dict = {'name':student.name,
                        'surname':student.last_name,
                        'e-mail':student.mail,
                        'telephone':student.telephone}
        return jsonify(student_dict)
    return 'lipa'


if __name__ == "__main__":
    app.run(debug=True)
