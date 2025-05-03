from ...models.user import User
from ...extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def register_user(data):
    if User.query.filter_by(email=data['email']).first():
        raise ValueError('Email already exists')
    if User.query.filter_by(username=data['username']).first():
        raise ValueError('Username already exists')
    user = User(
        username=data['username'],
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return user

def login_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password_hash, data['password']):
        raise ValueError('Invalid email or password')
    access_token = create_access_token(identity=user.id)
    return {'access_token': access_token}