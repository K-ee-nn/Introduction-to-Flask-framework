from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="templates" ) # this is the blueprint of main.py

@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html") # routing to the home.html page

@second.route("/test")
def test():
    return "<h1>This is the Testing Page</h1>"

