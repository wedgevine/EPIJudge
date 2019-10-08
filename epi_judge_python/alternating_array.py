import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook

def book(A):

    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)

    return

def second(A):

    is_bigger = 1
    current, last = 0, len(A) - 1

    while current < last:
        if is_bigger * (A[current + 1] - A[current]) < 0:
            A[current], A[current + 1] = A[current + 1], A[current]
        is_bigger *= -1
        current += 1

    return

def first(A):

    is_asd = True
    start, last = 0, len(A) - 1

    while start < last:
        if is_asd:
            if A[start] > A[start + 1]:
                A[start], A[start + 1] = A[start + 1], A[start]
        else:
            if A[start] < A[start + 1]:
                A[start], A[start + 1] = A[start + 1], A[start]
        is_asd = not is_asd
        start += 1

    return 
    
def rearrange(A):
    # first(A)    
    # second(A)
    book(A)
    return


@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i - 1, i),
                            '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i, i + 1),
                                '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i - 1, i),
                                '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] <= A[{}]'.format(i, i + 1),
                                '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("alternating_array.py",
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
