import os
import socket
import logging
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from app.resources.book_recommend import Recommend, SearchHistory
from app.resources.auth import signIn
from app.models.cassandra_config import Cassandra
from app.models.book import BooksModel
from app.models.user import UserModel
from app.Utils.Auth.TokenConfig import Auth

#loging
logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


flask_app = Flask(__name__)
api = Api(flask_app)

#defaults
flask_app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@flask_app.before_first_request
def create_tables():
    cassandra = Cassandra()
    cassandra.sync_table(database=BooksModel)
    cassandra.sync_table(database=UserModel)




@flask_app.route('/authuser', methods=['GET'])
@Auth.auth_required
def get_a_user():

    return jsonify({"Msg":"AUTH-OK"})

@flask_app.route('/authadmin', methods=['GET'])
@Auth.auth_admin
def get_a_admin():

    return jsonify({"Msg":"Admin-Ok"})




#endpoints
api.add_resource(Recommend, '/recommend/<string:book>/<int:number>')
api.add_resource(SearchHistory, '/')
api.add_resource(signIn,'/register')