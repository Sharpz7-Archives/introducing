"""
Scrape https://earthview.withgoogle.com/ for a single location
"""

import re

import requests


def get():
    """
    Returns a fake face
    """

    url = "https://earthview.withgoogle.com/"

    # get url
    content = requests.get(url).text

    # regex to look for href="/map/X"
    # where X is the location
    regex = r'href="/map/([^"]+)"'
    tag = re.search(regex, content).group(1)

    # split tag by -
    tag = tag.split("-")

    # move last element to first
    # to make sure "places" is in right order

    tag.insert(0, tag.pop())
    image_no, *places = tag

    place = " ".join(places).title()
    url = f"https://www.gstatic.com/prettyearth/assets/full/{image_no}.jpg"

    return place, url
