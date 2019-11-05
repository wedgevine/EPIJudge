from test_framework import generic_test
from test_framework.test_failure import TestFailure


def i2s_first(x):
    if x == 0:
        return '0'

    a, is_negative = [], False

    if x < 0:
        is_negative = True
        x = -x

    while x:
        # str() function is not allowed
        # a.append(str(x % 10))
        a.append(chr(ord('0') + (x % 10)))
        x //= 10
    
    if is_negative:
        a.append('-')

    return ''.join(reversed(a))

def s2i_first(s):
    i, sign = 0, 1

    if s[0] == '-':
        sign = -1
        s = s[1:]
    
    for c in range(len(s)):
        # since int() function is not allowed
        # i = i * 10 + int(s[c])
        i = i * 10 + (ord(s[c]) - ord('0'))

    return i * sign


def int_to_string(x):
    return i2s_first(x)


def string_to_int(s):
    return s2i_first(s)


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
