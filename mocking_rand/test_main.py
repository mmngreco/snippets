import random


class Random(object):

    def randin(self, a, b) -> int:
        return random.randint(a, b)


class MyClass(Random):

    def __init__(self, values) -> None:
        self.values = values

    def seq(self) -> list[int]:
        return self.values

    def rand(self) -> list[int]:
        return [self.randint(1, 4) for _ in range(3)]


def test_seq():
    obtained = MyClass().seq()
    expected = [1,2,3]
    assert obtained == expected, f"wrong seq, got {obtained}, wanted {expected}"


class RandMock:

    values = [1, 2, 3]
    counter = 0

    def randint(self, a, b) -> int:

        out = self.values[self.counter]
        self.counter += 1

        return out


def test_rand():

    Random.randint = RandMock().randint  # mocking

    obtained = MyClass().rand()
    expected = [1,2,3]

    assert obtained == expected, f"wrong seq, got {obtained}, wanted {expected}"

