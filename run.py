import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_messages(username, message):
    """Add messages to the 'mesaages' list"""
    now = datetime.now().strptime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    """Get all of the messages and separate using a 'br'"""
    return "<br>".join(messages)


@app.route('/', methods =["GET", "POST"])
def index():
    """Main page with instruction"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])    

    return render_template("index.html")


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