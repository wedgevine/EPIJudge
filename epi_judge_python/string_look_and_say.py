from test_framework import generic_test
import itertools

# pythonic, use the power of itertools.groupby()
def third(n):
    s = '1'

    for _ in range(n - 1):
        s = ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s)
        )
    
    return s

# from book, more succinct
def second(n):
    def get_next(s):
        result, current = [], 0

        while current < len(s):
            count = 1
            # look ahead?
            while current + 1 < len(s) and s[current] == s[current + 1]:
                count += 1
                current += 1
            result.append(str(count) + s[current])
            current += 1
        
        return ''.join(result)
    
    s = '1'
    for _ in range(1, n):
        s = get_next(s)

    return s

def first(n):
    sn = '1'
    loop = n
    result = ['1']
    pre_d, count = '', 0

    while loop > 1:
        result = []
        pre_d, count = sn[0], 1
        for d in sn[1:]:
            if d != pre_d:
                result.append(str(count))
                result.append(pre_d)
                pre_d, count = d, 1
            else:
                count += 1
        # add the last digit
        result.append(str(count))
        result.append(pre_d)

        loop -= 1
        sn = result
    
    return ''.join(result)


def look_and_say(n):
    # return first(n)
    # return second(n)
    return third(n)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
