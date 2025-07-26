from typing import Dict


class CustomResponse:
    def __init__(self):
        pass
    @staticmethod
    def list_response(result_dic):
        response = {
            "statusCode": 200,
            "message": "success",
            "data": result_dic,
            "success": True,
        }
        return response

    @staticmethod
    def error_occurred_response(errors, msg):
        response = {"statusCode": 400, "message": msg, "errors": errors}
        return response

    @staticmethod
    def not_found_response(errors):
        response = {
            "statusCode": 404,
            "message": errors,
        }
        return response

    @staticmethod
    def success_response(msg, result):
        response = {"statusCode": 200, "message": msg, "results": result}
        return response

    @staticmethod
    def create_response(msg, result):
        response = {"statusCode": 201, "message": msg, "results": result}
        return response

    @staticmethod
    def delete_response(msg):
        response = {
            "statusCode": 200,
            "message": msg,
        }
        return response

    @staticmethod
    def serializers_errors(errors: Dict) -> Dict:
        error_messages = " & ".join(
            "".join(str(error) for error in error_list)
            for error_list in errors.values()
        )
        response = {
            "statusCode": 400,
            "message": error_messages,
            "errors": errors,
        }
        return response
 