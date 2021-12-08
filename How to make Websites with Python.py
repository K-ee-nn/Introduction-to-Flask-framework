from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/") # Flask doesn't know where we should be going to get to this page, so we need to give it a route 
def home():
    return 'Hello! this is the main page <h1>HELLO<h1>'

@app.route("/<name>") # Whenever we type something it's actually gonna grab that value and pass it to "user" function as a parameter  
def user(name):
    return f"Hello {name}!"

@app.route('/admin/')
def admin():
    return redirect(url_for('user', name="Admin!")) # redirect brings you to a different page 


if __name__ == "__main__": # To start the website on localhost 
    app.run()