from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/") # Flask doesn't know where we should be going to get to this page, so we need to give it a route 
def home():
    return render_template("index.html") # route to index.html template


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST': # If user is doing submission
        user = request.form["nm"] # The user will type the name and click submit
        return redirect(url_for("user", usr=user)) # Upon clicking submit it will redirect to a new page("user" function) with the login user name displayed
    else:
        return render_template("login.html") # else it will route back to login.html page



@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__": # To start the website on localhost 
    app.run(debug=True) # debug=True allows us to not have to rerun the server everytime we make a change  