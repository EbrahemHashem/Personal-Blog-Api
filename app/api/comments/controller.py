from flask import request
from flask_restx import Resource

from app.api.comments.service import CommentService
from .dto import CommentDto



api = CommentDto.api
data_resp = CommentDto.data_resp
error_response = CommentDto.error_response
comment_model = CommentDto.comment_model
@api.route("/")
class AddComment(Resource):
    
    @api.doc(
        responses={
            200: ("Added Successfully",data_resp),
            400: ("Possible Messages:'Email already exists','Username already exists'",error_response),
            403: "Access Denied!",
            404: "Request Not Found",
            500: "Unexpected Error Occurred"
        },
        description="Register a new user"                           
    )
    @api.expect(comment_model, validate=True)
    def post(self):
        data = request.json
        return CommentService.create_post(data)


