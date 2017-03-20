from flask import session, render_template, Blueprint, request, redirect, url_for
from app.models.checkpoint import *
from app.models.mentor import Mentor

checkpointcontroller = Blueprint('checkpointcontroller', __name__, template_folder='templates')


@checkpointcontroller.route('/checkpoint-make/<checkpoint_id>/<mentor_id>/<gradestudent>', methods=['POST', 'GET'])
def grade_student(checkpoint_id, mentor_id, gradestudent):

    mentor = mentor_id

    if request.method == 'POST':

        student = request.form['student']
        checkpoint_id = request.form['checkpoint']
        grade = request.form['grade' + request.form['student']]

        Checkpoint.make_checkpoint(session['user']['id'], mentor, student, checkpoint_id, grade)

    students_list = Student.get_students_without_checkpoint(checkpoint_id)

    return redirect(url_for('checkpointcontroller.checkpoint_mentor_student', user=session['user'],
                            checkpoint_id=checkpoint_id, mentor=mentor, students=students_list))


@checkpointcontroller.route('/checkpoint-make/<checkpoint_id>/<mentor>')
def checkpoint_mentor_student(checkpoint_id, mentor):

    if not Mentor.mentor_exist(mentor):
        return redirect(url_for('checkpointcontroller.checkpoint'))

    students_list = Student.get_students_without_checkpoint(checkpoint_id)

    return render_template('checkpoint-select-student.html', user=session['user'], checkpoint_id=checkpoint_id,
                           mentor=mentor, students=students_list)


@checkpointcontroller.route('/checkpoint-results/<checkpoint_id>')
def checkpoint_results(checkpoint_id):

    results = Checkpoint.show_checkpoint_results(checkpoint_id)
    if results is None:
        return redirect(url_for('checkpointcontroller.checkpoint'))
    checkpoint_name = Checkpoint.get_name(checkpoint_id)

    return render_template('checkpoint-results.html', user=session['user'], checkpoint_id=checkpoint_id,
                           checkpoint_name=checkpoint_name[0]['TITLE'], results=results)


@checkpointcontroller.route('/checkpoint-make/<checkpoint_id>')
def checkpoint_mentor(checkpoint_id):

    mentors = Checkpoint.select_mentors_not_in_checkpoint(checkpoint_id)
    if Checkpoint.get_name(checkpoint_id) is None:
        return redirect(url_for('checkpointcontroller.checkpoint'))

    return render_template('checkpoint-select-mentor.html', user=session['user'], checkpoint_id=checkpoint_id,
                           mentors=mentors)


@checkpointcontroller.route('/checkpoint-make', methods=['POST', 'GET'])
def checkpoint():

    if request.method == 'POST':
        new_checkpoint = request.form['new_checkpoint']
        date_of_checkpoint = request.form['date_checkpoint']
        Checkpoint.add_checkpoint(new_checkpoint, date_of_checkpoint, session['user']['id'])

    checkpoints = Checkpoint.show_checkpoints()

    return render_template('checkpoint.html', checkpoints=checkpoints, user=session['user'], today=datetime.date.today())
