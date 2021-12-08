from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/") # Flask doesn't know where we should be going to get to this page, so we need to give it a route 
def home():
    return render_template("index.html")


if __name__ == "__main__": # To start the website on localhost 
    app.run(debug=True) # debug=True allows us to not have to rerun the server everytime we make a change  