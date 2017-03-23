from app.modules.decorator import *
from flask import Blueprint
from app.modules.mod_student.student import Student

studentcontroller = Blueprint('student', __name__)

@studentcontroller.route('/student_list')
@login_required
@correct_type(['Manager', 'Employee', 'Mentor'])
def student_list():
    table = Student.students_list()
    if table:
        return render_template('student/student_list.html', table=table, user=session['user'])
    return render_template('student/student_list.html', user=session['user'])