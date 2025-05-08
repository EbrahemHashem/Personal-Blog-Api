from flask_restx import Namespace, fields
from app.api.dto import DataResponseDto


data_resp_obj = DataResponseDto.data_resp_obj
error_response = DataResponseDto.error_response

class CommentDto:
    api = Namespace('comment', description='Comment related operations')

    data_resp = api.clone("Request Response",data_resp_obj)
    error_response = api.clone("Error Response Extend",error_response)

    comment_model = api.model('Comment', {
        'title': fields.String(required=True, description='User username'),
        'content': fields.String(required=True, description='User email address'),
    })



