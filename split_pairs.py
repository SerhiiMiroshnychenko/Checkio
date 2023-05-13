"""
SPLIT PAIRS

Розбий рядок на пари символів.
Якщо рядок містить непарну кількість символів,
тоді відсутній другий символ останньої пари повинен
бути замінений на символ підкреслювання ('_').

Вхідні дані: Рядок.
Вихідні дані: Список або інший ітеративний об'єкт з рядків.
"""

from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    new_text = f'{text}_' if len(text) % 2 != 0 else text
    return [f'{new_text[ind]}{new_text[ind + 1]}' for ind in range(0, len(new_text)-1, 2)]


def split_pairs_clear(a):
    return [ch1+ch2 for ch1, ch2 in zip(a[::2], f'{a[1::2]}_')]


if __name__ == "__main__":

    print("Example:")

    print(list(split_pairs("abcd")))
    print(list(split_pairs("abc")))

    print(list(split_pairs_clear("abcd")))
    print(list(split_pairs_clear("abc")))

    assert list(split_pairs("abcd")) == ["ab", "cd"]
    assert list(split_pairs("abc")) == ["ab", "c_"]
    assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
    assert list(split_pairs("a")) == ["a_"]
    assert not list(split_pairs(""))

    print("The mission is done! Click 'Check Solution' to earn rewards!")
