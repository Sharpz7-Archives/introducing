"""
Scrape https://earthview.withgoogle.com/ for a single location
"""

import re

from introducing.urls import pre_download

URL = "https://earthview.withgoogle.com/"

@pre_download(url=URL)
def get(cache):
    """
    Returns a fake face
    """

    # get url
    content = str(cache[URL].text)

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
