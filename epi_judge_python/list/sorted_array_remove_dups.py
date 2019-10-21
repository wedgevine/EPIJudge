import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def first(A):
    
    if not A:
        return 0

    current, to_check = 0, 1
    
    while to_check < len(A):
        if A[to_check] != A[current]:
            current += 1
            A[current] = A[to_check]
        to_check += 1
    
    return current + 1

# book solution, faster
def second(A):

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[i] != A[write_index - 1]:
            A[write_index] = A[i]
            write_index += 1

    return write_index            

# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    # return first(A)
    return second(A)


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
