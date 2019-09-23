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
        
    return result

def divide(x, y):
    return bf(x, y)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
