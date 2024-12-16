from flask import Flask, jsonify
from flask_cors import CORS
from src.utils.enum import HttpMethod

app = Flask(__name__)
CORS(app)


@app.route("/sign-up", methods=[HttpMethod.POST.value])
def hello():
    print("hello!")

    return jsonify(status=200, message="hello world")
