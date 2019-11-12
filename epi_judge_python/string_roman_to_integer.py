from test_framework import generic_test
import functools

MAPPING = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000,
}

# from book, scan from right to left, since the string is in non-increasing order,
# if find a char in left is samller, minus its value
def second(s):
    return functools.reduce(
        lambda x, i: x + (-MAPPING[s[i]] if MAPPING[s[i]] < MAPPING[s[i + 1]] else MAPPING[s[i]]),
        reversed(range(len(s) - 1)),
        MAPPING[s[-1]]
    )

# look ahead, but not utilized string is non-increasing
def first(s):
    current, value = 0, 0

    while current < len(s):
        if current + 1 < len(s) and s[current : current + 2] in MAPPING:
            value += MAPPING[s[current : current + 2]]
            current += 2
        else:
            value += MAPPING[s[current]]
            current += 1

    return value

def roman_to_integer(s):
    # return first(s)
    return second(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
