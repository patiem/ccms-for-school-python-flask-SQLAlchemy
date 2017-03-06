from flask import Flask, request, session


app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')
def index():
    session['username'] = 'jest'
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"

    #session.pop('username', None)
    return "You are not logged in <br><a href = '/login'></b>" + \
       "click here to log in</b></a>"




if __name__ == "__main__":
    app.run(debug=True)
