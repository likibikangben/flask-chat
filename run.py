import os
from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with instruction"""
    return "To send a message  use /USERNAME/MESSAGE"



@pp.route('/<USERNAME>')
def user(username):
    return "Hi" + username


@pp.route('/<USERNAME>/<message>')
def send.message(username, message):
    return "{0}: {1}".format(username, message)

app.run(os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)