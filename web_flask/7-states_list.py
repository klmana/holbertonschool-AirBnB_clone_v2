#!/usr/bin/python3
"""
  web application to generate list of states dynamically
  be listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template
from os import getenv
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """
      access File/DB Storage for all State objects and render to HTML
    """

    return render_template(
        states=[st for st in storage.all('State').values()])


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
