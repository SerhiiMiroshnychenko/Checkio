"""
Вам дано рядок з двома позначками (початковою і кінцевою).
Ви повинні знайти підрядок яка знаходиться між двома позначками.
Але є декілька важливих умов:
Початкова і кінцева позначка завжди різні
Якщо не має початкової позначки, тоді перший символ повинен
знаходитись на початку рядка
Якщо не має кінцевої позначки, тоді останній символ повинен
знаходитись в кінці рядка
Якщо початкова і кінцева позначки відсутні, тоді необхідно
просто повернути рядок цілком
Якщо кінцева позначка іде перед початковою повернути порожній рядок
Вхідні дані: Три аргументи. Всі стрічки. Другий і третій аргумент
- це початкова і кінцева позначки.
Вихідні дані: Стрічка.
Як це використовується: для аналізу текстів
Передумова: не може бути більше однієї початкової та однієї кінцевої позначки
"""

def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    if begin not in text and end not in text:
        return text
    return '' if (begin_index := 0 if begin not in text else text.index(begin)+len(begin)) \
                 > (end_index := len(text) if end not in text else text.index(end))\
        else text[begin_index:end_index]


def between_markers_clear(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]


def between_markers_creative(txt, begin, end):
    a, b, c = txt.find(begin), txt.find(end), len(begin)
    return [txt[a+c:b], txt[a+c:], txt[:b], txt][2*(a<0)+(b<0)]


between_markers_speedy = lambda text, begin, end:\
    text[text.index(begin)+len(begin) if begin in text else 0:
         text.index(end) if end in text else len(text)]


if __name__ == "__main__":

    print("Example:")
    for func in (between_markers, between_markers_clear, between_markers_creative, between_markers_speedy):
        print('\n', func.__name__.upper())
        print(func("What is >apple<", ">", "<"), '== apple')
        print(func("<head><title>My new site</title></head>",
                              "<title>", "</title>"), '== My new site')
        print(func("No[/b] hi", "[b]", "[/b]"), '== No')
        print(func("No [b]hi", "[b]", "[/b]"), '== hi')
        print(func("No hi", "[b]", "[/b]"), '== No hi')
        print(func("No <hi>", ">", "<"), '== ')


    assert between_markers("What is >apple<", ">", "<") == "apple"
    assert (
        between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
        == "My new site"
    )
    assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
    assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
    assert between_markers("No hi", "[b]", "[/b]") == "No hi"
    assert between_markers("No <hi>", ">", "<") == ""

    print("The mission is done! Click 'Check Solution' to earn rewards!")
