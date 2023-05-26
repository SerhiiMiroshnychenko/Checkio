"""
Римська система числення має десяткову основу, але вона непозиційна
і не містить 0 (нуль). Римські числа утворюються шляхом
комбінації наступних семи символів:
Символ	Значення
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)
У цьому завданні, вам необхідно перетворити дане ціле число
(від 1 до 3999) в римську систему числення.
Вхідні дані: Число, як ціле число (int).
Вихідні дані: Римське число, як рядок (str).
"""

def checkio(data: int) -> str:
    result = ''
    roman_numbers = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }

    equivalent = {
        'DCCCC': 'CM',
        'CCCC': 'CD',
        'LXXXX': 'XC',
        'XXXX': 'XL',
        'VIIII': 'IX',
        'IIII': 'IV',
    }

    for number in roman_numbers:
        rest = data % number
        result += (data // number) * roman_numbers[number]
        data = rest
    for chars in equivalent:
        result = result.replace(chars, equivalent[chars])
    return result


def checkio_clear(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result


def checkio_speedy(x):
    a,r="",{}
    for i in range(3):
        p,(j,c,d)=10**i,"IVXLCDM"[2*i:][:3]
        r |= {p:j,5*p:c,4*p:j+c,9*p:j+d,10*p:d}
    for k in reversed(sorted(r)):
        a+=x//k*r[k]
        x%=k
    return a

if __name__ == '__main__':
    for func in (checkio, checkio_clear, checkio_speedy):
        print(func(6))
        print(func(76))
        print('499 => ', func(499), '<- CDXCIX')
        print(func(3888))
        print(func(9))
        print(func(90))
        print(func(900))
        print(func(4))
        print(func(40))
        print(func(400))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
