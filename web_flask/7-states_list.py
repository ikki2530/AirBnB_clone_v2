#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_li():
    """Call the template to list states"""
    sts = storage.all(State)
    return render_template('7-states_list.html', states=sts)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """close the sessions"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
