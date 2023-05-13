"""
GOES RIGHT AFTER

У даному слові потрібно перевірити, чи йде один символ відразу за іншим.
Випадки, яких слід очікувати, вирішуючи цю проблему:
одного із символів немає у даному слові - твоя функція повинна повертати False;
будь-який символ з'являється у слові більше одного разу - використовуй лише перший;
шукані символи однакові - твоя функція повинна повертати False;
умова враховує регістр, що означає, що «а» та «А» - це два різні символи.
Вхідні дані: Три аргументи. Перший - це заданий рядок, другий - символ, який повинен йти першим, а третій - символ, який повинен йти після першого.
Вихідні дані: Логічне (булеве) значення.
"""


def goes_after(word: str, first: str, second: str) -> bool:
    for index, character in enumerate(word):
        if character == second:
            return False
        if character == first:
            return index + 1 < len(word) and word[index + 1] == second
    return False


def goes_after_clear(word: str, first: str, second: str) -> bool:
    try:
        return word.index(second)-word.index(first) == 1
    except ValueError:
        return False


goes_after_creative = lambda w, f, s: w.index(f) == w.index(s)-1 if f in w and s in w else False


def goes_after_speedy(word: str, first: str, second: str) -> bool:
    i = word.find(first)
    return i >= 0 and word.find(second) == i+1


if __name__ == "__main__":
    funcs = (goes_after, goes_after_clear, goes_after_creative, goes_after_speedy)
    for f in funcs:
        print(f'Function <<{f.__name__}>>')
        print(f("world", "w", "o"))
        print(f('transport', 'r', 't'))
        print()

    # These "asserts" are used for self-checking
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("Almaz", "a", "l") == False
    assert goes_after('transport', 'r', 't') == False
    assert goes_after('almaz', 'a', 'l') == True
    assert goes_after('almaz', 'm', 'a') == False
    assert goes_after('almaz', 'r', 'l') == False
    assert goes_after('almaz', 'p', 'p') == False
    assert goes_after('almaz', 'r', 'a') == False
    assert goes_after('world', 'a', 'r') == False
    assert goes_after('amazed', 'a', 'z') == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")
