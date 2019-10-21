from test_framework import generic_test

def first(A):
    carry = 1
    current = len(A) - 1

    while current >= 0:
        A[current], carry = (A[current] + carry) % 10, (A[current] + carry) // 10
        current -= 1

    if carry:
        A.insert(0, 1)
        # A = [carry] + A
        # A[0] = 1
        # A.append(0)

    # about insert vs append, insert always need to copy existing elements
    # while for append, sometimes no need to copy, sometimes need to
    # so it looks append is faster than insert
    # amortizely, append is O(1), while insert is O(N-i) complexity
    # but for the above case, looks there is no difference, maybe because 
    # just one element added?
    # https://stackoverflow.com/questions/7776938/python-insert-vs-append

    return A

def second(A):
    carry = 1

    for i in reversed(range(len(A))):
        A[i] += carry
        if A[i] == 10:
            A[i] = 0
            carry = 1
        else:
            carry = 0

    if carry == 1:
        A[0] = 1
        A.append(0) 
    
    return A

# this is the fastest, why?
# no carry variable, no extra computation for it
def third(A):

    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] < 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
      
    return A

def plus_one(A):
    # return first(A)
    # return second(A)
    return third(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
