# pip install pytest-check
from pytest_check import check


@check.check_func
def assert_check(a, b):
    assert a == b


def assert_simple(a, b):
    assert a == b


def test_simple():
    assert_simple(1, 1)
    assert_simple(1, 2)
    assert_simple(1, 1)


def test_check():
    assert_check(1, 1)
    assert_check(1, 2)
    assert_check(1, 1)


