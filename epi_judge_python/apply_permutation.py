from test_framework import generic_test


def first(perm, A):

    size = len(A)
    B = [0] * size

    for i in range(size):
        B[perm[i]] = A[i]

    A[:] = B    

    return

# unlike first, try to in-place permutation, in constant memory space
# thinking there are multiple cyclic permutations, each is a closed circle
# each element in the circle takes position of its next element, the last
# element takes position of first element
# the algo is find all such circles, for each circle, re-position elements
# one by one, thus, only constant extra spaces are needed
def second(perm, A):

    size = len(A)
    start, current, finished = 0, 0, 0
    
    while finished < size:
        while perm[start] == -1:
            start += 1
        current = start
        next_value = A[current]
        while perm[current] != -1:
            next_index = perm[current]
            A[next_index], next_value = next_value, A[next_index]
            finished += 1
            perm[current] = -1        
            current = next_index

    return 

def apply_permutation(perm, A):
    # first(perm, A)
    second(perm, A)
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
