from models.student import Student
from flask import Flask, request, session, render_template,redirect, url_for
from models.user import *
from models.menu import StudentMenu

app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/checkpoint')
def checkpoint():
    return render_template('checkpoint.html')


@app.route('/assignments')
def show_assignments_list():
    user_id = session['user']['id']
    logged_user = Student.return_by_id(user_id) #what with team id??
    assignments = StudentMenu.assignment_list_with_grades(logged_user)
    return render_template('assignments.html', user=logged_user, assignments=assignments)


@app.route('/assignments/<id>')
def show_assignment(id):
    # logged_user = None
    return render_template('submissions.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        logged_user = User.login(request.form['user_login'], request.form['user_pass'])

        if logged_user is not None:
            user = {'id': logged_user['ID'], 'name': logged_user['Name'], 'surname':logged_user['Surname'], 'type':logged_user['Type']}
            session['user'] = user
            print(session['user']['id'])

    if 'user' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')



@app.route('/student_list')
def student_list():
    table = Student.create_student_list()
    student_object = User.return_by_id(1)
    if table:
        return render_template('student_list.html', table=table, student_object=student_object)
    return render_template('student_list.html')


if __name__ == "__main__":
    app.run(debug=True)
