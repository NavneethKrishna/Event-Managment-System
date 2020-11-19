from flask import render_template, flash, redirect
from Event import app, db, bcrypt 
from Event.forms import RegistrationForm, LoginForm
from Event.models import User
from flask.helpers import url_for
from flask_login import login_user


@app.route("/")
@app.route("/login.html", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@event.com' and form.password.data == 'password':
            flash('You have been Logged in !!','success')
            return redirect(url_for('home'))
        else:
            user = User.query.filter_by(email = form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Login unsuccessful. Please check your email and password')

    return render_template('login.html', title='Title', form=form)

@app.route("/register.html", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created successfully!!','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/form.html")
def form():
    return render_template('form.html', title='Forms')

@app.route("/feedback.html")
def feedback():
    return render_template('feedback.html', title='Feedback')