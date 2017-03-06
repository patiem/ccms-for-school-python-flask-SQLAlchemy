from flask import Flask, render_template
from models.student import Student
from models.user import User

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/student_list')
def student_list():
    table = Student.create_student_list()
    student_object = User.return_by_id(1)
    if table:
        return render_template('student_list.html', table=table, student_object=student_object)
    return render_template('student_list.html')

if __name__ == "__main__":
    app.run(debug=True)
