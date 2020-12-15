from flask import render_template, flash, redirect
from Event import app, db, bcrypt 
from Event.forms import RegistrationForm, LoginForm, FeedbackForm, BookingForm
from Event.models import User, Feedback, Booking
from flask.helpers import url_for
from flask_login import login_user


@app.route("/")
@app.route("/login.html", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@event.com' and form.password.data == 'password':
            flash("You have been Logged in !!","success")
            return redirect(url_for('home'))
        else:
            user = User.query.filter_by(email = form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You have been Logged in !!","success")
                return redirect(url_for('home'))
            else:
                flash("Login unsuccessful. Please check your email and password","success")

    return render_template('login.html', title='Title', form=form)

@app.route("/register.html", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created successfully!!","success")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/form.html", methods=['GET', 'POST'])
def form():
    form = BookingForm()
    if form.validate_on_submit():
        print("Success")
        booking = Booking(name=form.name.data, email=form.email.data, event_name=form.event_name.data, date=form.date.data, phone=form.phone.data, attendees=form.attendees.data, time=form.time.data, city=form.city.data, venue=form.venue.data, additional_requirements=form.additional_requirements.data)
        db.session.add(booking)
        db.session.commit()
        flash("Thank you for the feedback !!","success")
    return render_template('form.html', title='Forms', form=form)

@app.route("/feedback.html", methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        print("Success")
        feedback = Feedback(name=form.name.data, email=form.email.data, feedback=form.feedback.data)
        db.session.add(feedback)
        db.session.commit()
        flash("Thank you for the feedback !!","success")
    return render_template('feedback.html', title='Feedback', form=form)
    