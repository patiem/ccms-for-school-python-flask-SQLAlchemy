from flask import session, render_template, Blueprint, request, redirect, url_for
from app.modules.mod_checkpoint.checkpoint import *
from app.modules.mod_student.student import Student
from sqlalchemy import func

statistics = Blueprint('statistics', __name__, template_folder='templates')

@statistics.route('/statistics_mentor', methods=['POST', 'GET'])
def statistics_mentor():
    if session['user']['type'] == 'Mentor':

        id_mentor = session['user']['id']
        cards = db.session.query(Users_checkpoints.GRADE, func.count(Users_checkpoints.GRADE)).\
            filter((Users_checkpoints.ID_MENTOR_1==id_mentor)|(Users_checkpoints.ID_MENTOR_2==id_mentor)).\
            group_by('GRADE').all()

        checkpoints = Checkpoint.query.filter_by(ID_USER=session['user']['id']).all()

        return render_template('statistic/statistics_mentor.html', user=session['user'], cards=cards, checkpoints=checkpoints)
    return redirect(url_for('index'))

@statistics.route('/statistics_student', methods=['POST', 'GET'])
def statistics_student():
    if session['user']['type'] == 'Student':
        return render_template('statistic/statistics_student.html', user=session['user'])
    return redirect(url_for('index'))

@statistics.route('/statistics_manager', methods=['POST', 'GET'])
def statistics_manager():
    if session['user']['type'] == 'Manager':

        grades = Student.get_students_grades()
        attandance = Student.get_students_attandance()

        return render_template('statistic/statistics_manager.html', user=session['user'], grades=grades, attandance=attandance)
    return redirect(url_for('index'))