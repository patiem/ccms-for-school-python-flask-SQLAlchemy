from app.modules.decorator import *
from app.modules.mod_user.user import User
from flask import Blueprint, jsonify

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