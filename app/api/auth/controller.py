from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..auth import auth_bp
import logging

logger = logging.getLogger(__name__)
api = AuthDto.api

@api.route('/register')
def register():
    try:
        data = UserSchema().load(request.get_json())
        user = register_user(data)
        logger.info(f"User registered: {user.username}")
        return jsonify(UserSchema().dump(user)), 201
    except ValueError as e:
        logger.error(f"Registration error: {str(e)}")
        raise AppError(str(e), 400)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = UserSchema(only=('email', 'password')).load(request.get_json())
        result = login_user(data)
        logger.info(f"User logged in: {data['email']}")
        return jsonify(result), 200
    except ValueError as e:
        logger.error(f"Login error: {str(e)}")
        raise AppError(str(e), 401)

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    logger.info(f"Profile accessed: {user.username}")
    return jsonify(UserSchema().dump(user)), 200