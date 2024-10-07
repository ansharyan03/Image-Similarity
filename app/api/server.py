from flask import Flask, redirect, url_for, jsonify, request
from flask_cors import CORS, cross_origin

from model.model import SimilarityModel
from api.s3util import S3Uploader
from api.dbutil import UserImageDB

import json
from os import environ as env

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) # cross-origin resource sharing, allows all root resources to be accessed by requests of any origin. replace * with any known URLs for web servers accessing your API

# host=env["DB_HOST"]
# password=env["DB_PASS"]

db = UserImageDB()

@app.route('/', methods=['GET'])
def home():
    return "hello!"

@app.route('/user', methods=['POST', 'GET'])
def addUser():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        img = request.files['image']
        db.sign_up(name, password, img)
        return f"hello from POST /user! {name} {password} {img.filename}"
    else:
        return db.get_all_users()

@app.route('/similar/<string:user1>/<string:user2>', methods=['GET'])
def getSimilarity(user1, user2):
    return {"similarity": db.get_similarity(user1, user2)}

@app.route('/user/<string:token>', methods=['GET'])
def getUser(token):
    user = db.get_user(token)
    if user:
        return user
    else:
        return "error: no user found with name %s" % (token,)
    return db.get_user(token)


if __name__=="__main__":
    app.run('0.0.0.0', port=8000)