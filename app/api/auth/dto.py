from flask_restx import Namespace, fields
from app.api.dto import DataResponseDto


data_resp_obj = DataResponseDto.data_resp_obj
error_response = DataResponseDto.error_response
class AuthDto:
    api = Namespace('auth', description='Authentication related operations')

    data_resp = api.clone("Request Response",data_resp_obj)
    error_response = api.clone("Error Response Extend",error_response)

    login_model = api.model('Login', {
        'email': fields.String(required=True, description='User email address'),
        'password': fields.String(required=True, description='User password')
    })

    register_model = api.model('Register', {
        'username': fields.String(required=True, description='User username'),
        'email': fields.String(required=True, description='User email address'),
        'password': fields.String(required=True, description='User password')
    })

    login_response = api.model('Login Response', {
        'access_token': fields.String(description='JWT access token')
    })