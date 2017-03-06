from flask import Flask, render_template, request, url_for, redirect, session
from models.student import Student
from models.user import *

app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/assignments')
def show_assignments_list():
    logged_user = session['user']['id']
    return render_template('assignments.html')


@app.route('/assignments/<id>')
def show_assignment(id):
    # logged_user = None
    return render_template('submissions.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        logged_user = User.login(request.form['user_login'], request.form['user_pass'])

        if logged_user is not None:
            user = {'id': logged_user['ID'], 'name': logged_user['Name'], 'surname':logged_user['Surname']}
            session['user'] = user
            print(session['user']['id'])

    if 'user' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')





if __name__ == "__main__":
    app.run(debug=True)
