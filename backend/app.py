from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    print('hello!')

    

    return jsonify(status=200, message='hello world')
