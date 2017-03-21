from app.modules.decorator import *
from app.modules.mod_user.user import User
from flask import Blueprint, jsonify
from app.modules.mod_student.student import Student

usercontroller = Blueprint('user', __name__)


@usercontroller.route('/check-mail', methods=['POST'])
@login_required
@correct_type(['Manager', 'Mentor'])
@correct_json(['Mail'])
def mail_exist():
        if request.method == 'POST':
            if request.is_json:
                mail_list = User.return_mails()
                for mail in mail_list:
                    if mail.Email == request.json['Mail']:
                        value = {'value': True}
                        return jsonify(value)
                value = {'value': False}
                return jsonify(value)
            return redirect(url_for('index'))
        return redirect(url_for('index'))


@usercontroller.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        logged_user = User.login(request.form['user_login'], request.form['user_pass'])

        if logged_user is not None:

            user = {'id': logged_user.ID, 'name': logged_user.Name, 'surname': logged_user.Surname,
                    'type': logged_user.Type, 'ave_grade': Student.ave_grade_flask_version(logged_user.ID),
                    'my_attendance': Student.my_attendance(logged_user.ID)}

            session['user'] = user
    if 'user' in session:
        return render_template('index.html', user=session['user'])
    else:
        return render_template('login.html')


@usercontroller.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('user.index'))
