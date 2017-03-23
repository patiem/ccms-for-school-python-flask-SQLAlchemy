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


@usercontroller.route('/edit-form', methods=['POST', 'GET'])
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
            User.update_sql(edit_list)
            return redirect(url_for('student_list'))
        elif user_type == 'mentor':
            User.update_sql(edit_list)
            return redirect(url_for('mentor_list'))
        else:
            return render_template('bad.html')


@usercontroller.route('/remove-user', methods=['POST', 'GET'])
@login_required
@correct_type(['Manager', 'Mentor'])
@correct_json(['Idx'])
def remove_user():
    if request.method == 'POST':
        idx = request.json['Idx']
        User.remove_sql(idx)

@usercontroller.route('/save-user', methods=['POST', 'GET'])
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
            User.add_user(add_list, 'Student')
            return redirect(url_for('student_list'))
        elif user_type == 'mentor':
            User.add_user(add_list, 'Mentor')
            return redirect(url_for('mentor_list'))
        else:
            return render_template('bad.html')

@usercontroller.route('/edit', methods=['POST', 'GET'])
@login_required
@correct_type(['Manager', 'Mentor'])
def get_data():
    if request.method == 'POST':
        idx = request.json['Idx']
        user = User.return_by_id(idx)
        user_dict= {'id': idx,
                    'name': user.Name,
                    'surname': user.Surname,
                    'e-mail': user.Email,
                    'telephone': user.Telephone}
        return jsonify(user_dict)
    return 'lipa'