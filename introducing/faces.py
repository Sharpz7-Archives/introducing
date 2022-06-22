"""
Scrape https://this-person-does-not-exist.com/en for a single face
"""

import requests
from requests_html import HTMLSession

from introducing.urls import pre_download


@pre_download(url="https://this-person-does-not-exist.com")
def get():
    """
    Returns a fake face
    """

    url = "https://this-person-does-not-exist.com"

    try:
        session = HTMLSession()
        response = session.get(url)

    except requests.exceptions.RequestException as e:
        print(e)

    # get src of tag with id avatar
    avatar_src = response.html.find('#avatar', first=True).attrs['src']

    session.close()

    return url + avatar_src
