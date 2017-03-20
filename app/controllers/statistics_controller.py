from flask import session, render_template, Blueprint, request, redirect, url_for
from app.models.checkpoint import *


statistics = Blueprint('statistics', __name__, template_folder='templates')

@statistics.route('/statistics_mentor', methods=['POST', 'GET'])
def statistics_mentor():
    if session['user']['type'] == 'Mentor':
        cards = Checkpoint.show_statistics_for_mentor_cards(session['user']['id'])
        checkpoints = Checkpoint.show_statistics_for_mentor_checkpoints(session['user']['id'])

        return render_template('statistics_mentor.html', user=session['user'], cards=cards, checkpoints=checkpoints)
    return redirect(url_for('index'))

@statistics.route('/statistics_student', methods=['POST', 'GET'])
def statistics_student():
    if session['user']['type'] == 'Student':
        return render_template('statistics_student.html', user=session['user'])
    return redirect(url_for('index'))

@statistics.route('/statistics_manager', methods=['POST', 'GET'])
def statistics_manager():
    if session['user']['type'] == 'Manager':

        grades = Student.get_students_grades()
        attandance = Student.get_students_attandance()

        return render_template('statistics_manager.html', user=session['user'], grades=grades, attandance=attandance)
    return redirect(url_for('index'))