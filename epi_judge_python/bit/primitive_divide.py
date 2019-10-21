from test_framework import generic_test

def bf(x, y):
    result = 0

    while x >= y:
        result += 1
        x -= y
    
    return result

def second(x, y):
    result = 0

    while x >= y:
        running_y = y
        order = 0
        while x >= running_y:
            x -= running_y
            result += (1 << order)
            running_y <<= 1
            order += 1
    
    return result

def third(x, y):
    result = 0
    order = 0

    while x >= y:
        y <<= 1
        order += 1

    while order >= 0:
        if x >= y:
            result += (1 << order)
            x -= y
        y >>= 1
        order -= 1

    return result

def divide(x, y):
    # return bf(x, y)
    # return second(x, y)
    return third(x, y)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
