from flask import Flask, jsonify
from introducing import faces, location

app = Flask(__name__, static_folder="./static")


@app.route('/')
def default():
    """
    Returns all incomes
    """

    return app.send_static_file('default.html')


@app.route('/face')
def get_face():
    """
    Returns a fake face
    """

    return jsonify(faces.get())


@app.route('/location')
def get_location():
    """
    Returns a fake face
    """

    return jsonify(location.get())