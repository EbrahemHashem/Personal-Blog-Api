from flask import request
from flask_jwt_extended import jwt_required
from .dto import AuthDto
from .service import UserService
from flask_restx import Resource


register_model = AuthDto.register_model
api = AuthDto.api
data_resp = AuthDto.data_resp
error_response = AuthDto.error_response

@api.route("/register")
class Register(Resource):
    
    @api.doc(
        responses={
            200: ("Request Created Successfully",data_resp),
            400: ("Possible Messages:'Request Tiltle Exists'",error_response),
            403: "Access Denied!",
            404: "Request Not Found",
            500: "Unexpected Error Occurred"
        },
        description="Register a new user"                           
    )
    @api.expect(register_model, validate=True)
    def post(self):
        data = request.json
        user, status_code = UserService.register_user(data)
        if status_code == 200:
            return api.marshal(data_resp, data_resp), 200
        if status_code == 400:
            return api.marshal(error_response, error_response), 400

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     try:
#         data = UserSchema(only=('email', 'password')).load(request.get_json())
#         result = login_user(data)
#         logger.info(f"User logged in: {data['email']}")
#         return jsonify(result), 200
#     except ValueError as e:
#         logger.error(f"Login error: {str(e)}")
#         raise AppError(str(e), 401)

# @auth_bp.route('/profile', methods=['GET'])
# @jwt_required()
# def profile():
    # user_id = get_jwt_identity()
    # user = User.query.get_or_404(user_id)
    # logger.info(f"Profile accessed: {user.username}")
    # return jsonify(UserSchema().dump(user)), 200