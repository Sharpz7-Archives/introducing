import random
import re

import names
import requests

from introducing.constants import NAMES, MIN_BACKSTORY_LENGTH, TENSES


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


def get_backstory():
    """
    Backstory Generator
    """

    while True:
        url = "https://www.kassoon.com/dnd/backstory-generator/"

        # get url
        content = requests.get(url).text

        # regex = r'<h2>Life</h2>([^"]+)<p>'
        # tag = re.search(regex, content).group(1)

        regexes = [r'Motivation: ([^.]+)', r'Origin: ([^.]+)']
        backstory = ""

        for regex in regexes:
            backstory += re.search(regex, content).group(1) + ". "

        if len(backstory) > MIN_BACKSTORY_LENGTH:
            break


    # convert to correct tense
    for change in TENSES:
        backstory = backstory.replace(*change)

    return backstory
