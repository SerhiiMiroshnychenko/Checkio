"""
Відсортуй даний список так, щоб його елементи стали згруповані
та ці групи йшли в порядку спадання частоти, тобто кількості
появи елемента в послідовності. Якщо два елементи мають однакову
частоту, їх групи повинні йти в порядку першої появи елемента в початковому списку.
Вхідні дані: Список.
Вихідні дані: Список або інший Ітерований об'єкт (кортеж, ітератор, генератор).
Де це використовується: Для аналізу даних за допомогою математичної статистики
та математичного аналізу, а також для пошуку тенденцій і прогнозування майбутніх
змін (систем, явищ тощо).
Передумова: елементи можуть бути цілими числами або рядками.
"""

from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    items_frequency= {}
    for item in items:
        if item not in items_frequency:
            items_frequency[item] = items.count(item)
    frequency_of_items = sorted(list(items_frequency.values()))[::-1]
    sorted_by_frequency_items = []
    add_frequencies = []
    for frequency in frequency_of_items:
        for key_, value_ in items_frequency.items():
            if value_ == frequency:
                add_frequency = [key_] * frequency
                if add_frequency not in add_frequencies:
                    add_frequencies.append(add_frequency)
                    sorted_by_frequency_items += add_frequency
    return sorted_by_frequency_items


def frequency_sort_clear(items: list[str | int]) -> Iterable[str | int]:
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))


frequency_sort_creative = lambda a: sorted(a, key=lambda x: (-a.count(x), a.index(x)))


def frequency_sort_speedy(items):
    from collections import Counter
    groups = Counter(items)
    sort = sorted(groups.items(), key=lambda e: e[1], reverse=True)
    for key, value in sort:
        yield from [key]*value


def frequency_sort_3rd(items):
    import pandas as pd
    if len(items) <= 2: return items  # return the simple cases
    # create a dataframe from items and the frequencies of each item
    df = pd.DataFrame(zip(items, [items.count(x) for x in items]))
    # sort descending by frequencies
    df.sort_values(by=1, ascending=False, inplace=True)
    # group by frequency but do not sort
    df = df.groupby([0], sort=False)[1].count()
    # create a list of each unique entry the number of times it occurs in items
    return [x for x in df.index for _ in range(items.count(x))]


if __name__ == "__main__":
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort_clear([4, 6, 2, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort_creative(["bob", "bob", "carl", "alex", "bob"]))
    print(list(frequency_sort_speedy([4, 6, 2, 2, 6, 4, 4, 4])))
    print(frequency_sort_3rd([4, 6, 2, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort([17, 99, 42]))
    print(frequency_sort([]))
    print(frequency_sort([1]))

    print("Example:")
    print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

    # These "asserts" are used for self-checking
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
        "bob",
        "bob",
        "bob",
        "carl",
        "alex",
    ]
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert not list(frequency_sort([]))
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([6, 3])) == [6, 3]
    assert list(frequency_sort([1, 1, 1, 1])) == [1, 1, 1, 1]
    assert list(frequency_sort([1, 2, 2, 1])) == [1, 1, 2, 2]

    print("The mission is done! Click 'Check Solution' to earn rewards!")

