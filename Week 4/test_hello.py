from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("umair") == "hello, umair"