from flask import Blueprint
from app.modules.mod_attendance.attendance import Attendance
from app.modules.decorator import *

attendancecontroller = Blueprint('attendancecontroller', __name__, template_folder='templates')


@attendancecontroller.route('/attendance', methods=['GET', 'POST'])
@login_required
@correct_type(['Mentor'])
@correct_form(['set_date'])
def attendance():
    if request.method == 'GET':
        import datetime
        date = str(datetime.date.today())
        if 'date' in request.args:
            date = request.args['date']
        attendance_list = Attendance.get_attendance_list(date)
        return render_template('attendance/attendance.html', user=session['user'], date=date, attendance_list=attendance_list)

    elif request.method == 'POST':
        students_present = {}
        date_from_form = ''
        for item in request.form:
            if item[:6] == 'person':
                student_id = int(item[6:])
                students_present[student_id] = request.form[item]
            elif item == 'set_date':
                date_from_form = request.form[item]
        Attendance.update(students_present, date_from_form)
        return redirect(url_for('attendancecontroller.attendance', date=date_from_form))


@attendancecontroller.route('/attendance/<date>')
@login_required
@correct_type(['Mentor'])
def attendance_date(date):
    return redirect(url_for('attendancecontroller.attendance', date=date))
