from flask_restx import Api
from flask import Blueprint

from .user.controller import api as user_ns

authorizations = {
    "Bearer":
    {
    "type": "apiKey",
    "in": "header",
    "name": "Authorization"
    }
    }

# Import controller APIs as namespaces.
api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="Main routes.", authorizations=authorizations, security="Bearer")

# API namespaces
api.add_namespace(user_ns,"/api/user")

