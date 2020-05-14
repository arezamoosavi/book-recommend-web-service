import os
from flask import Flask
import socket


flask_app = Flask(__name__)


@flask_app.route("/")
def index():
    return "Hello World! (HOSTNAME=%s, PID=%s)" % (socket.gethostname(), os.getpid())

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port="5000")