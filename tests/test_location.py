from introducing import location


def test_location():
    """
    Text Location is of correct format

    """

    loc = location.get()

    print(loc)

    assert len(loc) == 2
    assert isinstance(loc[0], str)

    assert isinstance(loc[1], str)
    assert 'https://www.gstatic.com/prettyearth/assets/full/' in loc[1]
    assert '.jpg' in loc[1]
