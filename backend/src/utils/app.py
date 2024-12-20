import json
from flask import request
from flask_cors import CORS
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from src.utils.enum import HttpMethod
from src.utils.enum import HttpStatus
from src.views.orders import OrdersView
from src.views.sign_up import SignUpView
from src.views.sign_in import SignInView
from src.utils.auth import extract_email_from_jwt


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_error_handler(Exception, json_error_handler)
    register_routes(app)

    return app


def json_error_handler(e: Exception):
    error = e.description if isinstance(e, HTTPException) else str(e)
    status_code = (
        e.code
        if isinstance(e, HTTPException)
        else HttpStatus.INTERNAL_SERVER_ERROR.value
    )

    return jsonify({"error": error}), status_code


def register_routes(app):
    @app.route("/sign-up", methods=[HttpMethod.POST.value])
    def sign_up():
        payload = json.loads(request.json)
        response = SignUpView.post(payload["email"], payload["password"])

        return response.to_json_response()

    @app.route("/sign-in", methods=[HttpMethod.POST.value])
    def sign_in():
        payload = json.loads(request.json)
        response = SignInView.post(payload["email"], payload["password"])

        return response.to_json_response()

    @app.route("/orders", methods=[HttpMethod.GET.value])
    @extract_email_from_jwt
    def orders(email: str):
        response = OrdersView.get(email)

        return response.to_json_response()
