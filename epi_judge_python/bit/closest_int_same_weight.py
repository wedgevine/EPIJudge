from test_framework import generic_test

# for given x, find y != x
# which has same number of "1"s as x
# also |y-x| is as small as possible
# for simplicity x is not all "0" or "1"

def swap(x, i, j):
    return x ^ ((1 << i) | (1 << j))

def get_bit(x, i):
    return (x >> i) & 1

def first(x):
    start = 0
    end = start

    while (get_bit(x, end) == get_bit(x, start) and end < 64):
        end += 1

    if (end < 64):
        return swap(x, end, end - 1)
    else:
        raise ValueError('All bits are 0 or 1')

# using trick x & (-x) to get LSB
# find out the rightmost bit that different from the first bit
# as a result, this algo is O(1) complexity, compared with the first algo O(N)
def second(x):
    mask = 0

    first_bit = x & 1
    if first_bit:
        # XXX011..1
        mask = (x + 1) & (-(x + 1))
    else:
        # XXX100..0
        mask = x & (-x)
    
    # or just use one statement
    # mask = (x + (x & 1)) & (-(x + (x & 1)))

    # make sure x is a 64-bit integer
    mask = mask % (1 << 64)
    # compose mask using current bit and previous bit
    mask = mask + (mask >> 1)
    
    if mask:
        return x ^ mask
    else:
        raise ValueError('All bits are 0 or 1')

def closest_int_same_bit_count(x):
    # return first(x)
    return second(x)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
