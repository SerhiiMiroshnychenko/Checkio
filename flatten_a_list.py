from collections.abc import Iterable


def flat_list(array: list) -> Iterable[int]:
    new_items = []
    while array:
        if new_items:
            start_items = new_items
            new_items = []
        else:
            start_items = array
        for i in start_items:
            try:
                new_items.extend(iter(i))
            except TypeError:
                new_items.append(i)
        if start_items == new_items or new_items == []:
            return new_items
    return []


def flat_list_clear(array: list) -> Iterable[int]:
    result = []

    def func(items):
        for i in items:
            result.append(i) if type(i) is int else func(i)

    func(array)
    return result


flat_list_creative = f = lambda d: 0 * d == 0 and [d] or sum(map(f, d), [])


def flat_list_speedy(array):
    import re
    return [int(i) for i in re.findall(r'[-]?\d+', str(array))]


def flat_list_3rd_party(array: list) -> list:
    """
        What flatten does, is to use recursion over the list until the list is completely flat.
          Since pandas is built on top of numpy, it means it's a fast solution
    """
    from pandas.core.common import flatten
    return list(flatten(array))


if __name__ == "__main__":
    print("Example:")
    print(list(flat_list([1, 2, 3])))
    test_list = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
    print(flat_list(test_list))
    test_items = [[[[[[[[[]]]]]]]]]
    print(flat_list(test_items))

    print("Example (clear):")
    print(list(flat_list_clear([1, 2, 3])))
    test_list = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
    print(flat_list_clear(test_list))
    test_items = [[[[[[[[[]]]]]]]]]
    print(flat_list_clear(test_items))

    print("Example (creative):")
    print(list(flat_list_creative([1, 2, 3])))
    test_list = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
    print(flat_list_creative(test_list))
    test_items = [[[[[[[[[]]]]]]]]]
    print(flat_list_creative(test_items))

    print("Example (speedy):")
    print(list(flat_list_speedy([1, 2, 3])))
    test_list = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
    print(flat_list_speedy(test_list))
    test_items = [[[[[[[[[]]]]]]]]]
    print(flat_list_speedy(test_items))

    print("Example (3rd_party):")
    print(list(flat_list_3rd_party([1, 2, 3])))
    test_list = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
    print(flat_list_3rd_party(test_list))
    test_items = [[[[[[[[[]]]]]]]]]
    print(flat_list_3rd_party(test_items))

    # These "asserts" are used for self-checking
    assert list(flat_list([1, 2, 3])) == [1, 2, 3]
    assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
    assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
        2,
        4,
        5,
        6,
        6,
        6,
        6,
        6,
        7,
    ]
    assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

    print("The mission is done! Click 'Check Solution' to earn rewards!")
