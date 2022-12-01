#!/usr/bin/python3
"""
  Script that starts a Flask web application:
  Web application be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
      Closes/remove the current SQLAlchemy Session again at end of the request
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
      The list of all State objects present in DBStorage with the id
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
