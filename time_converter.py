"""
Ви сучасна людина, яка воліє використовувати 24-годинний формат часу.
Але у деяких регіонах використовують 12-годинний формат.
Ваше завдання - переконвертувати час з 12-годинного формату на 24-годинний,
використовуючи наступні правила:
- вихідний формат має бути 'чч:мм'
- якщо годинник менше 10 - допишіть '0' перед ним. Наприклад: '09:05'
Ви можете дізнатися більше про 12-годинний формат.
Вхідні дані: Час у 12-годинному форматі (як рядок).
Вихідні дані: Час у 24-годинному форматі (як рядок).
Приклади:
time_converter('12:30 p.m.') == '12:30'
time_converter('9:00 a.m.') == '09:00'
time_converter('11:15 p.m.') == '23:15'
Як це використовується: Для роботи з різними форматами часу.
Передумови:
'00:00' <= час <= '23:59'
"""

def time_converter(time: str) -> str:
    meaning, suffix = time.split(' ')
    hours, minutes = int(meaning.split(':')[0]), int(meaning.split(':')[1])
    hours = hours + 12 if suffix == 'p.m.' else hours
    hours = 0 if hours == 24 else hours
    hours, minutes = f'0{hours}' if len(str(hours)) < 2 else hours,\
        f'0{minutes}' if len(str(minutes)) < 2 else minutes
    return f'{hours}:{minutes}'


if __name__ == "__main__":
    print("Example:")
    print(time_converter("12:30 p.m."))
    print(time_converter("9:00 a.m."))
    print(time_converter("11:15 p.m."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    print("Coding complete? Click 'Check' to earn cool rewards!")