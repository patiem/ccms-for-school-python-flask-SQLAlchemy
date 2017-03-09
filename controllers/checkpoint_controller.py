from flask import session, render_template, Blueprint, request, redirect, url_for
from models.checkpoint import *

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


    return redirect(url_for('checkpointcontroller.checkpoint_mentor_student', user=session['user'], checkpoint_id=checkpoint_id, mentor_id=mentor, students=students_list))


@checkpointcontroller.route('/checkpoint-make/<checkpoint_id>/<mentor_id>')
def checkpoint_mentor_student(checkpoint_id, mentor_id):

    mentor = mentor_id
    students_list = Student.get_students_without_checkpoint(checkpoint_id)
    return render_template('checkpoint-select-student.html', user=session['user'], checkpoint_id=checkpoint_id, mentor=mentor, students=students_list)


@checkpointcontroller.route('/checkpoint-make/<checkpoint_id>')
def checkpoint_mentor(checkpoint_id):
    checkpoint = Checkpoint()
    mentors = checkpoint.select_mentors_not_in_checkpoint(checkpoint_id)

    checkpoints = checkpoint.show_checkpoints()

    return render_template('checkpoint-select-mentor.html', user=session['user'], checkpoint_id=checkpoint_id,
                           mentors=mentors)


@checkpointcontroller.route('/checkpoint-make', methods=['POST', 'GET'])
def checkpoint():
    checkpoint = Checkpoint()

    if request.method == 'POST':
        new_checkpoint = request.form['new_checkpoint']
        date_of_checkpoint = request.form['date_checkpoint']
        Checkpoint.add_checkpoint(new_checkpoint, date_of_checkpoint, session['user']['id'])

    checkpoints = checkpoint.show_checkpoints()

    return render_template('checkpoint.html', checkpoints=checkpoints, user=session['user'])
