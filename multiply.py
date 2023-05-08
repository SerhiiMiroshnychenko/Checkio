from operator import mul as mult_two_clear
import numpy as np


def mult_two(a: int, b: int) -> int:
    return a * b


mult_two_creative = int.__mul__


def mult_two_3rd_party(a, b):
    return np.product([a, b])


if __name__ == "__main__":
    print("Example")
    print(mult_two(1, 2))
    print(mult_two_clear(1, 2))
    print(mult_two_creative(1, 2))
    print(mult_two_3rd_party(1, 2))

    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0

    print("The first mission is done! Click 'Check' to earn cool rewards!")
