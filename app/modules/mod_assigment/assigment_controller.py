from app.modules.decorator import *
from flask import Blueprint
from app.modules.mod_assigment.assignment import Assignment
from app.modules.mod_submission.submission import Submission

assigmentcontroller = Blueprint('assigment', __name__)


@assigmentcontroller.route('/assignments', methods=['GET', 'POST'])
@login_required
@correct_type(['Student', 'Mentor'])
def show_assignments_list():
    if session['user']['type'] == 'Student':
        assignments = Assignment.assignment_list_with_grades(session['user']['id'])
        return render_template('assignments/assignments.html', user=session['user'], assignments=assignments)

    elif session['user']['type'] == 'Mentor':
        if request.method == 'GET':
            assignments = Assignment.pass_assign_for_mentor()
            return render_template('assignments/assignments_mentor.html', user=session['user'], assignments=assignments)
        elif request.method == 'POST':
            title = request.form['a_title']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            group = request.form['group']
            description = request.form['description']
            Assignment.add_assignment(title, session['user']['id'], start_date, end_date, description, group)
            return redirect(url_for('assigment.show_assignments_list'))


@assigmentcontroller.route('/assignments/<idx>', methods=['GET', 'POST'])
@login_required
@correct_type(['Student', 'Mentor'])
def show_assignment(idx):
    assignment = Assignment.get_by_id(int(idx))
    submission = Submission.find_submission_sql(idx, session['user']['id'])
    if request.method == 'GET':
        return render_template('submission/submissions.html', user=session['user'], assignment=assignment, submission=submission)
    elif request.method == 'POST':
        link = request.form['link']
        comment = request.form['comment']
        Submission.add_submission(session['user']['id'], assignment.ID, link, comment, assignment.GROUP)
        return redirect(url_for('assigment.show_assignments_list'))
