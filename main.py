from flask import Flask, request, session, render_template


app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/', methods=['GET', 'POST'])
def index():
    #session['username'] = 'jest'
    session.pop('username', None)
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"


    #return "You are not logged in <br><a href = '/login'></b>" + \
      # "click here to log in</b></a>"

    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)
