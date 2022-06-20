from crypt import methods
from datetime import datetime
import jwt
from requests import session
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request, url_for, redirect
from app import app
from models import User
from . import db

@app.route('/', methods = ['GET', 'POST'])
@app.route("/login", methods = ['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if User.query.filter_by(email=email).first() or User.query.filter_by(username=email).first():
        user = User.query.filter_by(email).first()
        if check_password_hash(password, user.password):
            token = jwt.encode({
                'user': request.form.get('username'),
                'expiration' : str(datetime.utcnow() + timedelta(seconds=120))
            },
                app.config['SECRET_KEY']
            )
            return jsonify({'token': token.decode('utf-8')})
    else: 
        msg = "Check your details and try again"


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_pass = request.form.get('confirmpass')

    user = User.query.filter_by(email=email).first()

    if user:
        msg = 'Account already exists'
        return redirect(url_for(login))
    
    if password == confirm_pass:
        new_user = User(username=username, email=email, password=generate_password_hash(password), method='sha265')

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

