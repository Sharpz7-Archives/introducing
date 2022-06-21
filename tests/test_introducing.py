from introducing import __version__
from introducing import faces


def test_version():
    """Testing version"""

    assert __version__ == '0.1.0'


def test_faces():
    """
    Testing faces

    Should assert that output contains https://this-person-does-not-exist.com/img/avatar and jpg
    """

    output = faces.get_fake_face()
    assert 'https://this-person-does-not-exist.com/img/avatar' in output
    assert 'jpg' in output
