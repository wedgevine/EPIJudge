from test_framework import generic_test

def first_try(x, i, j):
    vi = (x >> i) & 1
    vj = (x >> j) & 1
    mask = pow(2, 64) - 1
    to_or = 1
    to_and = 1
    
    if (vi != vj):
        if vi:
            to_or = 1 << j
            to_and = (1 << i) ^ mask 
        else :
            to_or = 1 << i
            to_and = (1 << j) ^ mask
            
        x = (x | to_or) & to_and

    return x

def second_try(x, i, j):
    vi = (x >> i) & 1
    vj = (x >> j) & 1

    if (vi != vj):
        x ^= (1 << j) | (1 << i)

    return x

def swap_bits(x, i, j):
    # return first_try(x, i, j)
    return second_try(x, i, j)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
