from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/teams')
def teams():
    return render_template('teams.html')


@app.route('/attendance')
def attendance():
    return render_template('teams.html')


if __name__ == "__main__":
    app.run(debug=True)
