from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'# Going to be the name of the table that you're gonna be referencing 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # make it so that we're not tracking all the modifications to the database 
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app) # sqlalchemy database

# Model
class users(db.Model):# users table
    _id = db.Column("id", db.Integer, primary_key=True) # every single row has to have a different ID
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/") # Flask doesn't know where we should be going to get to this page, so we need to give it a route 
def home():
    return render_template("index.html") # route to index.html template


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": # If user is doing submission
        session.permanent = True
        user = request.form["nm"] # The user will type the name and click submit
        session["user"] = user  # create a new session for the user

        found_user = users.query.filter_by(name=user).first() # query from the Model(class users)
        for user in found_user:
            user.delete() 
        if found_user: # If user is present
            session["email"] = found_user.email # query and grab email from the database 
        else:# if the user doesn't exist
            usr = users(user, "") 
            db.session.add(usr)  # we'll add a new one to the database
            db.session.commit()


        flash("Login Successful!")
        return redirect(url_for("user")) # Upon clicking submit it will redirect to a new page("user" function) with the login user name displayed
    else:
        if "user" in session: # If user is already logged in,
            flash("Already Logged In!")
            return redirect(url_for("user")) # Don't allow user to go back to login page again, redirect user to the user page instead

        return render_template("login.html") # else it will route back to login.html page



@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session: # Authenticate if the user has logged in
        user = session["user"]

        if request.method == "POST": # If request method is a POST request,
            email = request.form["email"] # Ask user to submit email
            session["email"] = email      # store email in the session
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email # change the user's email,
            db.session.commit() # and save it in the database
            flash("Email was saved.")

        else: # if request method is a GET,
            if "email" in session:
                email = session["email"] # get the email from the session

        return render_template("user.html", email=email)
    else: # If user has not logged in,
        flash("You are not Logged In!") 
        return redirect(url_for("login")) # bring user back to the login page 


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info") # flash logged out indication whenever user has logged out
    session.pop("user", None) # remove the user data from the session
    session.pop("email", None)
    return redirect(url_for("login")) # Bring user back to the login page



if __name__ == "__main__": # To start the website on localhost
    db.create_all() # Create the sql database if it doesn't already exist in our program
    app.run(debug=True) # debug=True allows us to not have to rerun the server everytime we make a change  