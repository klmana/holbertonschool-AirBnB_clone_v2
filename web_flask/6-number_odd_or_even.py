#!/usr/bin/python3
"""
  Script that starts a Flask web application
  Web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
      Returns text when route is called , display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def route_hbnb():
    """
      Returns text when route is called , display “HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
      Will display “C ” followed by the value of the text variable
      (replace underscore _ symbols with a space )
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", defaults={"text": 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_display(text):
    """
      Display “Python“ followed by the value of the text variable
      (replace underscore _ symbols with a space )
    """
    return "".join(["Python ", text.replace("_", " ")])


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_an_integer(n):
    """
       display “n is a number” only if n is an integer
    """
    if type(n) is int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_is_an_integer_html(n):
    """
      display a HTML page only if n is an integer:
    """
    if type(n) is int:
        return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_is_an_integer_html2(n):
    """
      display a HTML page only if n is an integer:
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
