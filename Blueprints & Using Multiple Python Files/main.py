from flask import Flask, render_template
from admin.second import second 

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin") # if we type /admin in the url we will be direct to second.py 


@app.route("/")
def test():
    return "<h1>Test</h1>"


if __name__ == "__main__":
    app.run(debug=True)