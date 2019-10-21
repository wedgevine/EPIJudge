import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def first(pivot_index, A):
    pivot_value = A[pivot_index]
    s, e = 0, len(A) - 1
    ms, me = -1, -1

    # print('\n')
    # print(A)
    # print(len(A), pivot_index, pivot_value)

    while s <= e:
        if A[s] < pivot_value:
            if ms != -1:
                A[ms], A[s] = A[s], A[ms]
                ms += 1
                me = s
            s += 1
        elif A[s] == pivot_value:
            if ms != -1:
                me = s
            else:
                ms, me = s, s
            s += 1
        else:
            while A[e] > pivot_value and e > s:
                e -= 1
            A[s], A[e] = A[e], A[s]
            e -= 1

        # print("\n", s, e, '\n', A)

    # print("after \n")
    # print(A)

    return A

def second(pivot_index, A):
    pivot_value = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    # smaller group A[:smaller]
    # equal group A[smaller:equal]
    # unclassified group A[equal:larger]
    # larger group A[larger:]
    while equal < larger:
        if A[equal] < pivot_value:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot_value:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]  

    return A

def dutch_flag_partition(pivot_index, A):
    # first(pivot_index, A)
    second(pivot_index, A)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
