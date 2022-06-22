"""
Scrape https://this-person-does-not-exist.com/en for a single face
"""

from introducing.urls import pre_download

URL = "https://this-person-does-not-exist.com"

@pre_download(url=URL)
def get(cache):
    """
    Returns a fake face
    """

    response = cache[URL]

    # get src of tag with id avatar
    avatar_src = response.html.find('#avatar', first=True).attrs['src']

    return URL + avatar_src
