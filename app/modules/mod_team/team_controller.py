from flask import Blueprint
from app.modules.mod_team.team import Team
from app.modules.mod_student.student import Student
from app.modules.decorator import *


teamcontroller = Blueprint('teamcontroller', __name__, template_folder='templates')


@teamcontroller.route('/teams')
@login_required
@correct_type(['Mentor'])
def teams():
    teams_list = Team.create_teams_list()
    students_dict = Team.dict_with_students_id(teams_list)
    students_list = Student.students_list()
    return render_template('team/teams.html', user=session['user'], teams=teams_list,
                           students_list=students_list, students_dict=students_dict)


@teamcontroller.route('/team_name_edit', methods=['POST'])
@login_required
@correct_type(['Mentor'])
@correct_form(['id', 'team_name'])
def team_name_edit():
    idx = request.form['id']
    team_name = request.form['team_name']
    Team.update_name(idx, team_name)
    return redirect('/teams')


@teamcontroller.route('/add_to_team/<student_id>/<team_id>')
@login_required
@correct_type(['Mentor'])
def add_to_team(student_id, team_id):
    Team.add_student_to_team(student_id, team_id)
    return redirect('/teams')


@teamcontroller.route('/remove_team/<team_id>')
@login_required
@correct_type(['Mentor'])
def remove_team(team_id):
    Team.remove_team(team_id)
    return redirect('/teams')


@teamcontroller.route('/add_team', methods=['POST'])
@login_required
@correct_type(['Mentor'])
def add_team():
    name = request.form['new_team_name']
    Team.new_team(name)
    return redirect('/teams')


@teamcontroller.route('/remove_from_team/<student_id>')
@login_required
@correct_type(['Mentor'])
def remove_from_team(student_id):
        Team.remove_student_from_team(student_id)
        return redirect('/teams')
