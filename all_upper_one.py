"""
ALL UPPER I
Перевір, чи всі символи у даному рядку написані у верхньому регістрі.
Якщо рядок порожній або в ньому немає жодної літери, функція має повернути True.
Вхідні дані: Рядок.
Вихідні дані: Логічне (булеве) значення.
"""


def is_all_upper(text: str) -> bool:
    return next((False for char in text if char.islower()), True)


def is_all_upper_clear(text: str) -> bool:
    # your code here
    return text.upper() == text


def is_all_upper_creative(text: str) -> bool:
    text += "A"
    return text.isupper()


if __name__ == "__main__":
    words = ['Abc', 'ABC', 'Ab1', '123', '', 'АПР']
    for word in words:
        print(f'<<{word}>> is upper: {is_all_upper(word)},'
              f' {is_all_upper_clear(word)}, '
              f'{is_all_upper_creative(word)}')

    print("Example:")
    print(is_all_upper("ALL UPPER"))

    # These "asserts" are used for self-checking
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == True
    assert is_all_upper("444") == True
    assert is_all_upper("55 55 5 ") == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")
