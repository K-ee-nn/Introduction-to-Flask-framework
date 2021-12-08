from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/") # Flask doesn't know where we should be going to get to this page, so we need to give it a route 
def home():
    return render_template("index.html") # route to index.html template


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": # If user is doing submission
        session.permanent = True
        user = request.form["nm"] # The user will type the name and click submit
        session["user"] = user  # create a new session for the user
        flash("Login Successful!")
        return redirect(url_for("user")) # Upon clicking submit it will redirect to a new page("user" function) with the login user name displayed
    else:
        if "user" in session: # If user is already logged in,
            flash("Already Logged In!")
            return redirect(url_for("user")) # Don't allow user to go back to login page again, redirect user to the user page instead

        return render_template("login.html") # else it will route back to login.html page

@app.route("/user")
def user():
    if "user" in session: # Authenticate if the user has logged in
        user = session["user"]
        return render_template("user.html", user=user)
    else: # If user has not logged in,
        flash("You are not Logged In!") 
        return redirect(url_for("login")) # bring user back to the login page 


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info") # flash logged out indication, if not don't flash
    session.pop("user", None) # remove the user data from the session
    return redirect(url_for("login")) # Bring user back to the login page



if __name__ == "__main__": # To start the website on localhost 
    app.run(debug=True) # debug=True allows us to not have to rerun the server everytime we make a change  