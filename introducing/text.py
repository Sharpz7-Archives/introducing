import random
import re

import names

from introducing.constants import MIN_BACKSTORY_LENGTH, NAMES, TENSES
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

        # split backstory by word
        words = backstory.split()

        # for every time "you" is in the backstory
        # check if the word after "you" is a verb
        # if so, replace "you" with "they"

        for i, word in enumerate(words):
            if word == "you":
                # check if next word is a verb, past or present tense
                print(word, words[i + 1])

                if "ed" in words[i + 1]:
                    words[i + 1] = "they"


        # update backstory with new words
        backstory = " ".join(words)

        # Do other replacements
        for change in TENSES:
            backstory = backstory.replace(*change)

        if len(backstory) > MIN_BACKSTORY_LENGTH and "you" not in backstory:
            break

        else:
            update_one(cache, URL)
            print(backstory)


    return backstory
