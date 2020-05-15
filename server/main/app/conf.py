import os
import socket
import logging
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from app.resources.book_recommend import Recommend
from app.models.cassandra_config import Cassandra
from app.models.book import BooksModel

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

@flask_app.route("/")
def index():
    
    

    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_address=request.environ['REMOTE_ADDR']
    else:
        ip_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    
    #agent
    user_agent = request.user_agent.string

    new_books = BooksModel(book="a book", authors="sfdf,dfdfdf",
                rec_books=["book","sdsdsd"],
                state=True,ip=ip_address, agent=user_agent)
        
    print(new_books.items())
    print('**\n'*5)
        
    try:
        print('----\n'*10)
        new_books.save()

    except Exception as e:
        print('--///*--\n'*3)
        logging.error('Error! {}'.format(e))

        return jsonify({"message": "error"})
    
    print('%%\n'*5)

    print('\n'*5,new_books.items(),'\n'*5)
    return "Hello World! (HOSTNAME=%s, PID=%s)" % (socket.gethostname(), os.getpid())


#endpoints
api.add_resource(Recommend, '/recommend/<string:book>/<int:number>')