from flask import request
from src.utils.app import create_app
from src.utils.enum import HttpMethod
from src.views.sign_up import SignUpView

app = create_app()


@app.route("/sign-up", methods=[HttpMethod.POST.value])
def sign_up():
    payload = request.get_json()
    response = SignUpView.post(payload["email"], payload["password"])

    return response.to_json_response()
