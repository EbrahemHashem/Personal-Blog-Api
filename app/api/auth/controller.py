from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from .dto import AuthDto
from .service import UserService
from flask_restx import Resource


api = AuthDto.api
register_model = AuthDto.register_model
login_model = AuthDto.login_model
data_resp = AuthDto.data_resp
error_response = AuthDto.error_response
login_response = AuthDto.login_response

@api.route("/register")
class Register(Resource):
    
    @api.doc(
        responses={
            200: ("Register Successfully",data_resp),
            400: ("Possible Messages:'Email already exists','Username already exists'",error_response),
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
            return api.marshal(user, data_resp), 200
        if status_code == 400:
            return api.marshal(user, error_response), 400

@api.route("/login")
class Login(Resource):
    
    @api.doc(
        responses={
            200: ("Request login Successfully",login_response),
            400: ("Possible Messages:'Invalid email or password'",error_response),
            403: "Access Denied!",
            404: "Request Not Found",
            500: "Unexpected Error Occurred"
        },
        description="login a user"                           
    )
    @api.expect(login_model, validate=True)
    def post(self):
        data = request.json
        user, status_code = UserService.login_user(data)
        if status_code == 200:
            return api.marshal(user, login_response), 200
        if status_code == 400:
            return api.marshal(user, error_response), 400

@api.route("/profile")
class Login(Resource):
    
    @api.doc(
        responses={
            200: ("Request login Successfully",login_response),
            400: ("Possible Messages:'User not found'",error_response),
            403: "Access Denied!",
            404: "Request Not Found",
            500: "Unexpected Error Occurred"
        },
        description="User profile"                           
    )
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user, status_code = UserService.get_user_profile(user_id)
        if status_code == 200:
            return api.marshal(user, login_response), 200
        if status_code == 400:
            return api.marshal(user, error_response), 400

