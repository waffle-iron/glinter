from flask import Flask, render_template, url_for
from glint_tool import *
from glint_io import *

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/")
def home():
    return (render_template("index.html", name="home"))

@app.route("/list")
def list():
    return (render_template("index.html", name="test"))

if __name__ == "__main__":
    app.run(debug=True)
