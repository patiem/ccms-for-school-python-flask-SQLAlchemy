from app.modules.decorator import *
from flask import Blueprint
from app.modules.mod_mentor.mentor import Mentor

mentorcontroller = Blueprint('Mentor', __name__)

@mentorcontroller.route('/mentor_list')
@login_required
@correct_type(['Manager'])
def mentor_list():
    table = Mentor.create_mentor_list()
    if table:
        return render_template('mentor/mentor_list.html', table=table, user=session['user'])
    return render_template('mentor/mentor_list.html', user=session['user'])