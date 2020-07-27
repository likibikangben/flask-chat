import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """Add messages to the 'mesaages' list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    """Get all of the messages and separate using a 'br'"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instruction"""
    return "To send a message  use /USERNAME/MESSAGE"


@pp.route('/<username>')
def user(username):
    """Display chat messages""" 
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@pp.route('/<USERNAME>/<message>')
def send.message(username, message):
    """Creating a new message and redirect back to thechat page"""
    add_messages(username, message)
    return redirect(username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)