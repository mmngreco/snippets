import core


def test_boom():
    obtained = core.boom()
    expected = "boom"
    assert obtained == expected
