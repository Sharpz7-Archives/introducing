from introducing import __version__
from introducing import faces


def test_version():
    """Testing version"""

    assert __version__ == '0.1.0'


def test_faces():
    """Testing faces"""
    assert faces.get_fake_face() == 'faces'
