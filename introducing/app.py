from flask import Flask, jsonify

from introducing import faces, location, text, urls

app = Flask(__name__, static_folder="./static")

cache = {}

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

    print("UPDATING CACHE")
    urls.update_cache(cache)
    print("FINISHED")

    loc, background = location.get(cache)
    print("Location handled")

    send["profile_picture"] = faces.get(cache)
    send["location"] = loc
    send["background_image"] = background
    send["name"] = text.get_name()
    send["age"] = text.get_age()
    send["backstory"] = text.get_backstory(cache)
    print("Backstory Handled")

    return jsonify(send)
