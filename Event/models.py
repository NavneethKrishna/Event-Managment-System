from Event import db, login_manager
from flask_login import  UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):  #How object is printed when we print it .
        return f"User('{self.name}','{self.email}')"

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30), nullable=False) 
    feedback = db.Column(db.String(120), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30), nullable=False)
    event_name = db.Column(db.String(30), nullable = False)
    city = db.Column(db.String(30), nullable = False)
    venue = db.Column(db.String(30), nullable=True)
    date = db.Column(db.String(30), nullable = False)
    phone = db.Column(db.String(30), nullable = False)
    attendees = db.Column(db.Integer, nullable = False)
    time = db.Column(db.Time, nullable = False)
    additional_requirements = db.Column(db.String(120), nullable=False)
