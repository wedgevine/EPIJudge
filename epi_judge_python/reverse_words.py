import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# exception message: can only concatenate str (not "bytearray") to str
def first(s):
    size = len(s)
    r = ''
    word_start = word_end = size - 1

    while word_start >= 0:
        if s[word_start] != ' ':
            word_start -= 1
        else:
            r += (s[word_start + 1 : word_end + 1])
            r += ' '
            word_start -= 1
            word_end = word_start
    
    r += s[:word_end + 1]
    s[:] = r

# for bytes and bytearray, char is encoded as ascii, whitespace is 32
def second(s):
    s.reverse()
    size = len(s)
    word_start, word_end = 0, 0
    head = tail = 0

    while word_end < size:
        if s[word_end] != 32:
            word_end += 1
        else:
            head, tail = word_start, word_end - 1
            while head < tail:
                s[head], s[tail] = s[tail], s[head]
                head += 1
                tail -= 1
            word_end += 1
            word_start = word_end

    head, tail = word_start, word_end - 1
    while head < tail:
        s[head], s[tail] = s[tail], s[head]
        head += 1
        tail -= 1

# use find method
def third(s):
    s.reverse()

    start = end = 0
    while end >= 0:
        end = s.find(b' ', start)
        if end < 0:
            break
        head, tail = start, end - 1
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
        start = end + 1

    head, tail = start, len(s) - 1
    while head < tail:
        s[head], s[tail] = s[tail], s[head]
        head += 1
        tail -= 1
    

# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # first(s)
    # second(s)
    third(s)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
