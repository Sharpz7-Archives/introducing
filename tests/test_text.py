from introducing import text, urls
from introducing.constants import MIN_BACKSTORY_LENGTH

cache = {}


def test_backstory():
    """
    Text Location is of correct format

    """

    urls.update_cache(cache)
    backstory = text.get_backstory(cache)

    print(backstory)
    print(len(backstory))

    assert len(backstory) > MIN_BACKSTORY_LENGTH
    assert "you" not in backstory
    assert ". " in backstory


def test_age():
    """
    Test Age is within range
    """

    age = text.get_age()

    assert age in range(14, 99)


def test_name():
    """
    Test Name is valid string
    """

    name = text.get_name()

    assert isinstance(name, str)
