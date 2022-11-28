#!/usr/bin/python3
    """
      Script that starts Flask web application:
      Web application must be listening on 0.0.0.0, port 5000
    """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def main():
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)