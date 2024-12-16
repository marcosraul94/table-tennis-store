from flask import Flask, request
from flask_cors import CORS
from src.utils.enum import HttpMethod
from src.views.sign_up import SignUpView

app = Flask(__name__)
CORS(app)


@app.route("/sign-up", methods=[HttpMethod.POST.value])
def sign_up():
    payload = request.get_json()

    return SignUpView.post(payload["email"], payload["password"])
