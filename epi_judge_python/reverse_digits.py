from test_framework import generic_test


def bf(x):
    result = 0
    sign = 1

    if x < 0:
        sign = -1
        x = -x

    while x:
        result = result * 10 + (x % 10)
        x //= 10

    return sign * result

def reverse(x):
    return bf(x)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
