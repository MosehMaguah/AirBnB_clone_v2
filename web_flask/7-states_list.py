#!/usr/bin/python3
"""
The script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def handle_teardow(self):
    """
    After each request you have to kill the current session of SQLAlchemy
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_of_state():
    """
    Function called with the route /states_list
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
