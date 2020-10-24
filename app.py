from flask import Flask, render_template, flash, redirect
from forms import RegistrationForm, LoginForm
from flask.helpers import url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a9ae0fc9ba4ef967c995959a2f18485f'

@app.route("/")
@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/register.html")
def register():
    form = RegistrationForm()
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)


