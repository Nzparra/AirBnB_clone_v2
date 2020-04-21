#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """ states list """
    if state_id:
        state_id = 'State.' + state_id
    states = storage.all("State")
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """ teardown """
    storage.close()


if __name__ == "__main__":
    app.run()
