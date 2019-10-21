from test_framework import generic_test

def first(num1, num2):
    
    # a simple fact is product of m digits x n digits 
    # will be m + n or m + n - 1 digits
    # pre-assign a list so that don't have to insert/append element one by one
    
    result = [0] * (len(num1) + len(num2))
    index = 0
    sign = 1

    if num1[0] * num2[0] == 0:
        return [0]

    sign = (num1[0] * num2[0]) // (abs(num1[0] * abs(num2[0])))
    num1[0] = abs(num1[0])  
    num2[0] = abs(num2[0])

    for i in reversed(range(len(num2))):
        index = len(result) - (len(num2) - i)
        for j in reversed(range(len(num1))):
            result[index] += num1[j] * num2[i]
            if result[index] >= 10:
                result[index - 1] += result[index] // 10
                result[index] = result[index] % 10
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
