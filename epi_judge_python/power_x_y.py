from test_framework import generic_test

# if y = pow(2, N)

# O(pow(2, N))
def bf(x, y):
    result = 1
    negative = 0

    if y < 0:
        negative = 1
        y = -y

    while y > 0:
        result = result * x
        y -= 1

    if negative:
        result = 1 / result

    return result

# O(N*N)
def second(x, y):
    result = 1
    negative = 0

    if y < 0:
        negative = 1
        y = -y

    while y:
        order = 1
        running_value = x

        while y >= (order << 1):
            order <<= 1
            running_value *= running_value

        result *= running_value
        y -= order

    if negative:
        result = 1 / result

    return result

# O(N)
def third(x, y):
    result = 1

    if y < 0:
        y = -y
        x = 1 / x

    while y:
        if y & 1:
            result *= x
        x *= x
        y >>= 1

    return result

def power(x, y):
    # return bf(x, y)     # 719us/570us
    # return second(x, y)     # 15us/13us
    return third(x, y)      # 5us/5us


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
