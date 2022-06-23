import logging
import os

from flask import Flask, jsonify

from introducing import faces, location, text, urls

app = Flask(__name__, static_folder="./static")

cache = {}

if os.environ["FLASK_ENV"] == "development":
    app.debug = True
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

@app.route('/')
def default():
    """
    Returns all incomes
    """

    return app.send_static_file('default.html')


@app.route('/introducing', methods=['GET'])
def get_intro():
    """
    Returns an Introduction of someone
    """

    send = {}

    logging.info("UPDATING CACHE")
    urls.update_cache(cache)
    logging.info("FINISHED")

    loc, background = location.get(cache)
    profile_picture = faces.get(cache)
    name = text.get_name()
    title = text.get_title()
    age = text.get_age(profile_picture)
    backstory = text.get_backstory(cache)

    send["profile_picture"] = profile_picture
    send["location"] = loc
    send["background_image"] = background
    send["name"] = name
    send["age"] = age
    send["backstory"] = backstory
    send["title"] = title

    response = jsonify(send)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
