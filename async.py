def gen():
    count = 0

    while count < 4:
        count += 1
        print(count)
        yield count

    return count


def test_gen():
    g = gen()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))


def genOFgen():
    yield from "abc"
    yield from [1,2,3]



if __name__ == '__main__':
    g =genOFgen()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
