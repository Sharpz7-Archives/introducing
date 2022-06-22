from introducing import faces, urls

cache = {}

def test_faces():
    """
    Testing faces

    Should assert that output contains https://this-person-does-not-exist.com/img/avatar and jpg
    """

    urls.update_cache(cache)
    output = faces.get(cache)
    assert 'https://this-person-does-not-exist.com/img/avatar' in output
    assert 'jpg' in output
