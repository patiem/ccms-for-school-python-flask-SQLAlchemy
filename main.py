from flask import Flask, request, session, render_template
from models.user import *

app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        logged_user = User.login(request.form['user_login'], request.form['user_pass'])

        if logged_user is not None:
            user = {'id': logged_user['ID'], 'name': logged_user['Name'], 'surname': logged_user['Surname']}
            session['user'] = user

    if 'user' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')


@app.route('/teams')
def teams():
    return render_template('teams.html')


@app.route('/attendance')
def attendance():
    return render_template('teams.html')


if __name__ == "__main__":
    app.run(debug=True)
