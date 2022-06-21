from introducing import faces


def test_faces():
    """
    Testing faces

    Should assert that output contains https://this-person-does-not-exist.com/img/avatar and jpg
    """

    output = faces.get()
    assert 'https://this-person-does-not-exist.com/img/avatar' in output
    assert 'jpg' in output
