from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["umair", "ahmad", "ali"]:
        assert hello("umair") == "hello, umair"