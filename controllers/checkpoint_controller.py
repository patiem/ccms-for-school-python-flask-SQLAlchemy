from flask import session, render_template, Blueprint
from models.checkpoint import *

checkpointcontroller = Blueprint('checkpointcontroller', __name__, template_folder='templates')


@checkpointcontroller.route('/checkpoint-make/grade')
def grade():


    return render_template('checkpoint-select-student.html')


@checkpointcontroller.route('/checkpoint-make/<checkpoint_id>/<mentor_id>')
def checkpoint_mentor_student(checkpoint_id, mentor_id):
    checkpoint = Checkpoint()
    mentor = mentor_id

    students_list = Student.get_students_without_checkpoint(checkpoint_id)

    return render_template('checkpoint-select-student.html', user=session['user'], checkpoint=checkpoint, mentor=mentor, students=students_list)


@checkpointcontroller.route('/checkpoint-make/<checkpoint_id>')
def checkpoint_mentor(checkpoint_id):
    checkpoint = Checkpoint()
    mentors = checkpoint.select_mentors_not_in_checkpoint(checkpoint_id)

    checkpoints = checkpoint.show_checkpoints()

    return render_template('checkpoint-select-mentor.html', user=session['user'], checkpoint_id=checkpoint_id,
                           mentors=mentors)


@checkpointcontroller.route('/checkpoint-make')
def checkpoint():
    checkpoint = Checkpoint()

    mentors = ""
    # students = get_students_without_checkpoint

    checkpoints = checkpoint.show_checkpoints()

    return render_template('checkpoint.html', checkpoints=checkpoints, user=session['user'])
