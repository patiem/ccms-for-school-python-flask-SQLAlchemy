from flask import Blueprint, jsonify
from app.modules.mod_submission.submission import Submission
from app.modules.decorator import *

submissioncontroller = Blueprint('submissioncontroller', __name__, template_folder='templates')


@submissioncontroller.route('/grade_submission', methods=['GET', 'POST'])
@login_required
@correct_type(['Mentor'])
def grade_submission():
    if request.method == 'GET':
        sub_list = Submission.subs_to_grade()
        return render_template('submission/grade_submission.html', user=session['user'], sub_list=sub_list)


@submissioncontroller.route('/update_submission', methods=['POST'])
@login_required
@correct_type(['Mentor'])
def update_submission():
    value = request.json['Value']
    link = request.json['Link']
    mentor_id = session['user']['id']
    Submission.update_grade(value, link, mentor_id)
    user_dict = {'fullname': session['user']['name'] + ' ' + session['user']['surname']}
    return jsonify(user_dict)
