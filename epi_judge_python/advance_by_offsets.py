from test_framework import generic_test

def first(A):

    start = 0
    while start + A[start] < len(A) - 1:
        rank = 0
        next_step = 0
        for i in range(1, A[start] + 1):
            if i + A[start + i] >= rank:
                rank = i + A[start + i]
                next_step = i
            if start + rank > len(A):
                return True
        if next_step == 0:
            return False
        start += next_step
    
    return True

def second(A):

    start, current = 0, 0
    distance = 0
    last = len(A) - 1

    while start + A[start] < last:
        limit = start + A[start]
        distance = limit
        for i in range(current, limit + 1):
            if i + A[i] >= distance:
                distance = i + A[i]
                start = i
        if distance == limit:
            return False
        current = limit + 1

    return True

# most simple solution from book
# but second algo can be modified to calculate how many steps needed exactly
# https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
# https://www.geeksforgeeks.org/minimum-steps-reach-end-array-constraints/

def third(A):
    
    the_furthest, i = 0, 0
    last = len(A) - 1

    while i <= the_furthest and the_furthest < last:
        the_furthest = max(the_furthest, i + A[i])
        i += 1

    return the_furthest >= last
    
def can_reach_end(A):
    # return first(A)
    # return second(A)
    return third(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
