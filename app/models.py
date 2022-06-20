from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)
    timers = db.relationship('Timer', backref='author', lazy=True)
    counters = db.relationship('Counter', backref='author', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __repr__(self):
        return '<Timer %r>' % self.title

class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    count = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __repr__(self):
        return '<Counter %r>' % self.title