#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_li():
    """Call the template to list states"""
    sts = storage.all(State)
    return render_template('8-cities_by_states.html', states=sts)

@app.teardown_appcontext
def shutdown_session(exception=None):
    """close the sessions"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
