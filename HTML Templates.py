from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<name>") # Flask doesn't know where we should be going to get to this page, so we need to give it a route 
def home(name):
    return render_template("index.html", content=['tim', 'joe', 'bill'])


if __name__ == "__main__": # To start the website on localhost 
    app.run()