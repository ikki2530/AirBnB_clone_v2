#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    """list states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    render = render_template('10-hbnb_filters.html', states=states, amenities=amenities)
    return render


@app.teardown_appcontext
def shutdown_session(exception=None):
    """close the sessions"""
    storage.close()


