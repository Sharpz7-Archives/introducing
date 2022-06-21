"""
Scrape https://this-person-does-not-exist.com/en for a single face
"""

import requests

def get_fake_face():
    """
    Returns a fake face
    """

    response = requests.get('https://this-person-does-not-exist.com/en')

    # get src of tag with id avatar

    print(img_src)