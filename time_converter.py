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
    hours = hours + 12 if suffix == 'p.m.' and hours != 12 else hours
    hours = 0 if hours == 24 or (hours == 12 and suffix == 'a.m.')  else hours
    hours, minutes = f'0{hours}' if len(str(hours)) < 2 else hours,\
        f'0{minutes}' if len(str(minutes)) < 2 else minutes
    return f'{hours}:{minutes}'


def time_converter_clear(time):
    h, m = map(int, time[:-5].split(':'))
    return f"{h % 12 + 12 * ('p' in time):02d}:{m:02d}"


def time_converter_explain(time):
    # h, m = map(int, time[:-5].split(':'))
    splited_time = time[:-5].split(':') # splited_time == "12:30".split(':') == ["12", "30"]
    h = int(splited_time[0]) # h = int("12")
    m = int(splited_time[1]) # h = int("34")

    # return f"{h % 12 + 12 * ('p' in time):02d}:{m:02d}"
    # 1. hour = h % 12 + 12 * ('p' in time)
    hour = h
    if hour == 12: # h % 12 part
        hour = 0 # this means conversion from "12:30 p.m." to "00:30 p.m."

    hour += 12 if 'p' in time else 0
    return "{:02d}:{:02d}".format(hour, m)


from time import strptime as p, strftime as f

time_converter_creative = lambda t: f("%H:%M", p(t.replace('.', ''), "%I:%M %p"))


def time_converter_speedy(t):
    import time
    return time.strftime('%H:%M', time.strptime(t.replace('.', ''), '%I:%M %p'))



def time_converter_3rd(tim):
    import time
    tim = tim.replace(' ','').replace('.', '')
    times = time.strptime(tim.upper(), '%I:%M%p')
    return time.strftime('%H:%M', times)




if __name__ == "__main__":
    print("Example:")
    for func in (time_converter,
                 time_converter_clear,
                 time_converter_explain,
                 time_converter_speedy,
                 time_converter_creative,
                 time_converter_3rd):
        print(f'\nFunction {func.__name__.upper()}:')
        print(func("12:30 p.m."))
        print(func("9:00 a.m."))
        print(func("11:15 p.m."))
        print(func("12:00 a.m."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    assert time_converter("12:00 a.m.") == "00:00"

    print("Coding complete? Click 'Check' to earn cool rewards!")