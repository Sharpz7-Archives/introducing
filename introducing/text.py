import random
import re

import names

from introducing.constants import NAMES, MIN_BACKSTORY_LENGTH, TENSES
from introducing.urls import pre_download, update_one


URL = "https://www.kassoon.com/dnd/backstory-generator/"


def get_age():
    """
    Return a persons age.
    """

    return random.randrange(14, 99)


def get_name():
    """
    Return a random persons name
    """

    first = random.choice(NAMES)
    last = names.get_last_name()

    return f"{first} {last}"


@pre_download(url=URL)
def get_backstory(cache):
    """
    Backstory Generator
    """

    while True:

        # get url
        content = str(cache[URL].text)

        # regex = r'<h2>Life</h2>([^"]+)<p>'
        # tag = re.search(regex, content).group(1)

        regexes = [r'Motivation: ([^.]+)', r'Origin: ([^.]+)']
        backstory = ""

        for regex in regexes:
            backstory += re.search(regex, content).group(1) + ". "

        if len(backstory) > MIN_BACKSTORY_LENGTH:
            break

        else:
            update_one(cache, URL)


    # convert to correct tense
    for change in TENSES:
        backstory = backstory.replace(*change)

    return backstory
