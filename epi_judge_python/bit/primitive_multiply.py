from test_framework import generic_test

def addition(x, y):
    result = 0
    current_sum = 1
    a, b, c, s = 0, 0, 0, 0

    while x | y | c:
        a = x & 1
        b = y & 1

        # s = a ^ b ^ c
        
        if (a & b & c):
            s = 1
            c = 1
        elif ((a | b | c) and not(a ^ b ^ c)):
            s = 0
            c = 1
        elif (a | b | c and a ^ b ^ c):
            s = 1
            c = 0
        else:
            s = 0
            c = 0
        
        if s:
            result = result | current_sum

        x >>= 1
        y >>= 1
        current_sum <<= 1

    return result

def multiply(x, y):
    result = 0

    while y != 0:
        if y & 1:
            result  = addition(result, x)
        x <<= 1
        y >>= 1

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
