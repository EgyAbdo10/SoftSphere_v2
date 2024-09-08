#!/usr/bin/python3
"""dynamically generate web content"""
from flask import Flask, render_template, make_response
from uuid import uuid4
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def close(error):
    storage.close()
@app.route("/", strict_slashes=False)
@app.route("/softsphere", strict_slashes=False)
def home():
    """ SoftSphere is Alive! """
    categories = storage.all("Category").values()
    categories = sorted(categories, key=lambda k: k.name)
    projects = storage.all("Project").values()
    projects = sorted(projects, key=lambda k: k.name)
    users = storage.all("User").values()
    return render_template("0-index.html",
                           categories=categories,
                           projects=projects,
                           users=users,
                           cache_id=uuid4())

if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)
