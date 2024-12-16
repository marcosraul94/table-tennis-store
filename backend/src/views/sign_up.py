from flask import request, jsonify
from src.utils.view import View


class SignUpView(View):
    @staticmethod
    def post(email: str, password: str):
        # payload = request.get_json()
        # print(payload)

        body = {"something": "here"}

        return jsonify(
            status=200,
            message=body,
        )
