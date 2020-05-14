import os
import socket
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from app.resources.book_recommend import Recommend


flask_app = Flask(__name__)
api = Api(flask_app)



@flask_app.route("/")
def index():
    return "Hello World! (HOSTNAME=%s, PID=%s)" % (socket.gethostname(), os.getpid())


#endpoints
api.add_resource(Recommend, '/recommend/<string:book>/<int:number>')