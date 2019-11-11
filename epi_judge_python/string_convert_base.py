from test_framework import generic_test
import functools

def char_to_int(c):
    oc = ord(c)
    if oc < 65:
        return oc - ord('0')
    else:
        return oc - ord('A') + 10
def int_to_char(i):
    if i < 10:
        return chr(ord('0') + i)
    else:
        return chr(ord('A') + (i - 10))

def first(num_as_string, b1, b2):
    num, num_as_array = 0, []
    is_negative = False

    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        is_negative = True

    for i in range(len(num_as_string)):
        num = num * b1 + char_to_int(num_as_string[i])

    while True:
        num_as_array.append(int_to_char(num % b2))
        num //= b2
        if num == 0:
            break
    
    if is_negative:
        num_as_array.append('-')

    return ''.join(reversed(num_as_array))

# use reduce
def second(num_as_string, b1, b2):
    def construct_from_base(num, base):
        return ('' if num == 0 else 
                construct_from_base(num // base, base) 
                + 
                int_to_char(num % base)) 

    num, is_negative = 0, False 

    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        is_negative = True

    num = functools.reduce(
        lambda x, c: x * b1 + char_to_int(c),
        num_as_string,
        0
    )

    return ('-' if is_negative  else '') + ('0' if num == 0 else construct_from_base(num, b2))

def convert_base(num_as_string, b1, b2):
    # return first(num_as_string, b1, b2)
    return second(num_as_string, b1, b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
