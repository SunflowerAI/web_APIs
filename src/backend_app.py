import sys
import json
import jwt

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins":"*"}})

@app.route("/", methods=["GET"])
def hello():
    token = request.authorization.token
    print("Successful Get Test")
    if len(token) > 0:
        print(">0")
    else:
        print("=0")
    return "Hello world", 200

@app.route("/test", methods=["GET"])
def test_get():
    token = request.authorization.token
    print("Successful Get Test")
    if len(token) > 0:
        print(">0")
    else:
        print("=0")
    return "Hello world", 200

@app.route("/test", methods=["POST"])
def test_post():
    data = request.get_json()
    print("Successful Post Test")
    
    token = jwt.encode(data, 'secret', algorithm='HS256')
    
    response = jsonify({"token": token})
    
    return response, 200

if __name__=="__main__":
    app.run(debug=True)