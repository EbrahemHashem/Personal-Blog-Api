from ...models.user import User
from ...extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import logging
from app.utils import err_resp


logger = logging.getLogger(__name__)

class UserService:
    def register_user(data):
        if User.query.filter_by(email=data['email']).first():
            return err_resp('Email already exists','user_400', 400)
        if User.query.filter_by(username=data['username']).first():
            return err_resp('Username already exists', 'user_400', 400)
        user = User(
            username=data['username'],
            email=data['email'],
            password_hash=generate_password_hash(data['password'])
        )
        db.session.add(user)
        db.session.commit()
        logger.info(f"User registered: {user.username}")
        return user, 200

    def login_user(data):
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not check_password_hash(user.password_hash, data['password']):
            return err_resp('Invalid email or password','user_400', 400)
        access_token = create_access_token(identity=user.id)
        logger.info(f"User logged in: {data['email']}")
        return {'access_token': access_token}, 200
    
    def get_user_profile(user_id):
        user = User.query.get_or_404(user_id)
        if not user:
            return err_resp('User not found', 'user_404', 404)
        logger.info(f"Profile accessed: {user.username}")
        return user, 200