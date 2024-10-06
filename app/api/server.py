from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS, cross_origin

from mysql.connector import Error as SQLError

import json
from os import environ as env

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) # cross-origin resource sharing, allows all root resources to be accessed by requests of any origin. replace * with any known URLs for web servers accessing your API

host=env["DB_HOST"]
pass=env["DB_PASS"]

@app.route('/', methods=['GET'])
def home():
    return "hello!"

@app.route('/user', methods=['POST'])
def addUser():
    user = request.get_json()
    name = user['username']
    pass = user['password']
    img = user['image'] # change this to parse json however needed, you may need multer for help with this
    return f"hello from POST /user {token}!"

@app.route('/user/<str:token>', methods=['GET'])
def getUser(token):
    return f"hello from GET /user/{token}!"

