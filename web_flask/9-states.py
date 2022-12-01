#!/usr/bin/python3
"""
  Script that starts a Flask web application:
  Web application be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/<id>')
def state_and_id(id=None):
    """
      List the cities and the states by
      objects present in DBStorage with the id
    """
    states = [stt for stt in storage.all('State').values()]
    match_stt = None
    if id:
        for stt in states:
            if stt.id == id:
                match_stt = stt
    return render_template('9-states.html', state=match_stt)


@app.route('/cities_by_states', strict_slashes=False)
def all_states_with_cities_html():
    """
      All the states and cities
    """
    states = [stt for stt in storage.all('State').values()]
    return (render_template('8-cities_by_states.html', states=states))


@app.route('/states')
def states():
    """
      To access File/DB Storage for all
      the State objects and render to HTML
    """
    states = [stt for stt in storage.all('State').values()]
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
      Closes/remove the current SQLAlchemy Session again at end of the request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
