from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_error_handler(Exception, json_error_handler)

    return app


def json_error_handler(e: Exception):
    error = e.description if isinstance(e, HTTPException) else str(e)
    status_code = e.code if isinstance(e, HTTPException) else 500

    return jsonify({"error": error}), status_code
