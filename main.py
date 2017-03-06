from flask import Flask, render_template, request, url_for, redirect
from models.student import Student

app = Flask(__name__)

logged_student = Student.

@app.route('/')
def index():
    return 'Hello World'

@app.route('assignments')
def show_assignments():

@app.route('/assignments/<assignent_id>')
def show_assignment():
    logged_user = None
    return render_template('submissions.html')







if __name__ == "__main__":
    app.run(debug=True)
