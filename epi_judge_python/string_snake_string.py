from test_framework import generic_test

# pythonic solution using slice
def second(s):
    return s[1::4] + s[0::2] + s[3::4]


# first, let's try multiple passes
def first(s):
    size, result = len(s), []
    
    index, step = 1, 4
    while index < size:
        result.append(s[index])
        index += step
    
    index, step = 0, 2
    while index < size:
        result.append(s[index])
        index += step

    index, step = 3, 4
    while index < size:
        result.append(s[index])
        index += step

    return ''.join(result)


def snake_string(s):
    # return first(s)
    return second(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
