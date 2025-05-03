from flask_restx import Namespace, fields



class DataResponseDto:
    api = Namespace("response", description="Response Descrioption")
    data_resp_obj = api.model(
        "Data Response",
        {
            "status": fields.Boolean(example=True),
            "message": fields.String(example="Request created successfully")
        },
    )
    error_response  = api.model(
        "ErrorResponse",
        {
            "status": fields.Boolean(example = False),
            "message": fields.String(example = "Unit Does Not Exist"),
            "error_reason": fields.String(example = "unit_400"),
        }
    )
