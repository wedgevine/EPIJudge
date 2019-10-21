from test_framework import generic_test

def get_reverse(x):
    result = 0

    while x:
        result = result * 10 + x % 10
        x //= 10

    return result

def bf(x):
    if x < 0:
        return False

    return x == get_reverse(x) 

def is_palindrome_number(x):
    return bf(x)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
