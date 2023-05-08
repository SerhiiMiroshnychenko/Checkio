from collections.abc import Iterable
from numpy import unique, asarray


def checkio(data: list[int]) -> Iterable[int]:
    return [x for x in data if data.count(x) > 1]


def checkio_speed(data: list[int]) -> Iterable[int]:
    from collections import Counter
    count = Counter(data)
    return [n for n in data if count[n] > 1]


def checkio_3rd_party(data):
    u, ri, c = unique(asarray(data), return_inverse=True, return_counts=True)
    return [int(u[i]) for i in ri if c[i] > 1]


checkio_clear = lambda d: [x for x in d if d.count(x) > 1]


if __name__ == "__main__":
    print("Example:")
    print(list(checkio([1, 2, 3, 1, 3])))
    print(list(checkio_speed([1, 2, 3, 1, 3])))
    print(list(checkio_3rd_party([1, 2, 3, 1, 3])))
    print(list(checkio_clear([1, 2, 3, 1, 3])))

    # These "asserts" are used for self-checking
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
    assert not list(checkio([1, 2, 3, 4, 5]))
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
    assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
    assert list(checkio([10, 20, 30, 10])) == [10, 10]
    assert not list(checkio([7]))
    assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
    assert list(checkio([99, 98, 99])) == [99, 99]
    assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
    assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

    print("The mission is done! Click 'Check Solution' to earn rewards!")
