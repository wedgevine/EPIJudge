from test_framework import generic_test

def swap_bit(x, i, j):
    if ((x >> i & 1) != (x >> j & 1)):
        x ^= (1 << i) | (1 << j)

    return x

def get_reverse_bf(x):
    for i in range(32):
        x = swap_bit(x, i, 63-i)

    return x

def get_reverse(x, length):
    for i in range(length >> 1):
        x = swap_bit(x, i, length - 1 - i)

    return x

# cache lookup table and divide and conqure method
reverse_list = [get_reverse(k, 8) for k in range(1 << 8)]
reverse16_list = [get_reverse(k, 16) for k in range(1 << 16)]

def get_reverse_by_lookup(x):
    result = 0

    for i in range(8):
        result <<= 8
        result += reverse_list[x & 0xFF]
        x >>= 8

    return result

def get_reverse16_by_lookup(x):
    result = 0

    for i in range(4):
        result <<= 16
        result += reverse16_list[x & 0xFFFF]
        x >>= 16

    return result
def reverse_bits(x):
    # return get_reverse_bf(x)
    return get_reverse_by_lookup(x)
    # return get_reverse16_by_lookup(x)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
