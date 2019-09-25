import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def bf(A):
    start = 0
    end = len(A) - 1

    while start < end:
        if A[start] % 2 == 1:
            if A[end] % 2 == 0:
                # swap(A, start, end)
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            else:
                end -= 1
        else:
            start += 1
    
    return A

def second(A):
    next_even = 0
    next_odd = len(A) - 1

    while next_even < next_odd:
        if A[next_even] %2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A            

def even_odd(A):
    return bf(A)
    # return second(A)


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure("Elements mismatch")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_array.py",
                                       'even_odd_array.tsv', even_odd_wrapper))
