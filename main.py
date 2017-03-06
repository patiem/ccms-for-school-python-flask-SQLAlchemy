from models.student import Student
from flask import Flask, request, session, render_template,redirect, url_for, json
from models.user import User

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
            user = {'id': logged_user['ID'], 'name': logged_user['Name'], 'surname':logged_user['Surname'], 'type':logged_user['Type']}
            session['user'] = user

    if 'user' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')


@app.route('/student_list')
def student_list():
    table = Student.create_student_list()
    if table:
        return render_template('student_list.html', table=table)
    return render_template('student_list.html')


@app.route('/edit', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        idx = request.form['idx']

        return 'null'
    return 'lipa'

if __name__ == "__main__":
    app.run(debug=True)
