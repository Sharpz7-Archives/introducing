import logging
import random
import re

import names

from introducing.constants import (EASTER_EGG_REPLACERS, MIN_BACKSTORY_LENGTH,
                                   NAMES, REPLACERS, THEM_WORDS, THEY_WORDS)
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
            if word == "you" or word == "you,":

                # check if comma is needed
                add = ""
                if "," in word:
                    add = ","

                # check if next word is a verb, past or present tense
                if any(part in words[i + 1] for part in THEY_WORDS):
                    words[i] = "they" + add

                elif any(part in words[i + 1] for part in THEM_WORDS):
                    words[i] = "them" + add


        # update backstory with new words
        backstory = " ".join(words)

        # Do other replacements
        for change in REPLACERS:
            backstory = backstory.replace(*change)

        for change in EASTER_EGG_REPLACERS:
            lower_check = change[0].lower()
            upper_check = change[0].upper()

            backstory = backstory.replace(lower_check, change[1])
            backstory = backstory.replace(upper_check, change[1])

        tests = {
            "Length Check": len(backstory) > MIN_BACKSTORY_LENGTH,
            "Wrong Pronouns": "you" not in backstory
        }

        if tests["Length Check"] and tests["Wrong Pronouns"]:
            break

        else:
            update_one(cache, URL)
            logging.info(backstory)
            # logging.info whatever test failed
            if not tests["Length Check"]:
                logging.info(len(backstory))
                logging.info("Length Check Failed")

            elif not tests["Wrong Pronouns"]:
                logging.info("Pronouns Check Failed")


    return backstory
