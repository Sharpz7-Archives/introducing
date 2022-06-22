from flask import Flask, jsonify

from introducing import faces, location, text

app = Flask(__name__, static_folder="./static")


@app.route('/')
def default():
    """
    Returns all incomes
    """

    return app.send_static_file('default.html')


@app.route('/introducing')
def get_intro():
    """
    Returns an Introduction of someone
    """

    send = {}

    loc, background = location.get()

    send["profile_picture"] = faces.get()
    send["location"] = loc
    send["background_image"] = background
    send["name"] = text.get_name()
    send["age"] = text.get_age()
    send["backstory"] = text.get_backstory()

    return jsonify(send)
