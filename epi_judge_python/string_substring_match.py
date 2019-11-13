from test_framework import generic_test
import functools

def first(t, s):
    size_t, size_s = len(t), len(s)
    start_t = 0
    current_t, current_s = 0, 0
    
    while start_t <= size_t - size_s:
        current_t = start_t
        current_s = 0
        while current_s < size_s and t[current_t] == s[current_s]:
            current_t += 1
            current_s += 1
        if current_s == size_s:
            return start_t
        else:
            start_t += 1

    return -1

# from book, the so-called rabin-karp algo, depending on a hash function
def second(t, s):
    if len(t) < len(s):
        return -1

    BASE = 26
    t_hash = functools.reduce(
        lambda h, c: h * BASE + ord(c),
        t[:len(s)],
        0
    )
    s_hash = functools.reduce(
        lambda h, c: h * BASE + ord(c),
        s,
        0
    )
    power_s = BASE ** max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])
        print(t_hash)

    if t_hash == s_hash and t[len(t) - len(s):len(t)] == s:
        return len(t) - len(s)
    
    return -1


def rabin_karp(t, s):
    # return first(t, s)
    return second(t, s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
