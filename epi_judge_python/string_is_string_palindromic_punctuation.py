from test_framework import generic_test


def first(s):
    size = len(s)
    head, tail = 0, size - 1

    while head < tail:
        if not s[head].isalnum():
            head += 1
        elif not s[tail].isalnum():
            tail -= 1
        else:
            if s[head].upper() == s[tail].upper():
                head += 1
                tail -= 1
            else:
                return False

    return True

def is_palindrome(s):
    return first(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
