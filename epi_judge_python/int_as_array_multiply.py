from test_framework import generic_test

def first(num1, num2):
    
    result = [0] * (len(num1) + len(num2))
    index = 0
    carry_add = 0
    carry_mul = 0
    a = 0
    m = 0
    sign = 1

    if num1[0] * num2[0] < 0:
        sign = -1
        num1[0] = abs(num1[0])
        num2[0] = abs(num2[0])

    for i in reversed(range(len(num2))):
        index = len(result) - (len(num2) - i)
        for j in reversed(range(len(num1))):
            m = num1[j] * num2[i] + carry_mul
            if m >= 10:
                m, carry_mul = m % 10, m // 10
            a = result[index] + m 
            if a >= 10:
                result[index] = a - 10
                result[index - 1] += 1
            else:
                result[index] = a
            index -= 1

    if result[0] == 0:
        result[1] = sign * result[1]
        return result[1:]
    else:
        result[0] = sign * result[0]
        return result

def multiply(num1, num2):
    return first(num1, num2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
