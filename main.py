from flask import Flask, request, session, render_template,redirect, url_for
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
            user = {'id': logged_user['ID'], 'name': logged_user['Name'], 'surname':logged_user['Surname'], 'type':logged_user['Type']}
            session['user'] = user

    if 'user' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')









if __name__ == "__main__":
    app.run(debug=True)
