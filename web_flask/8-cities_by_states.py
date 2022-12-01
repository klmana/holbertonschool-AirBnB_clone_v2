#!/usr/bin/python3
"""
   Web application  be listening on 0.0.0.0, port 5000
   Use storage for fetching data from the storage engine
   (FileStorage or DBStorage)=>from models import storage and storage.all(...)
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """
      list cities by related state the objects present in DBStorage
    """
    return render_template('8-cities_by_states.html',
                           states=[ct for ct in storage.all('State').values()])


@app.teardown_appcontext
def teardown_db(exception):
    """
      Closes/remove the current SQLAlchemy Session again at end of the request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
