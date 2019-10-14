from test_framework import generic_test

# the key insight is increase the perm as little as possible
# meaning try to keep elements from left unchanged as much as possible
# meaning find the right most element which is less than an element from
# its right
# meaning if we travel from the right, whenever we saw a value descrease,
# we know we can do a swap of elements to find the next perm
def first(perm):

    size = len(perm)
    current = size - 1
    current_max = float('-inf')

    while current >= 0:
        if current_max <= perm[current]:
            current_max = perm[current]
            current -= 1
        else:
            new_perm = [0]
            not_swapped = True
            for i in reversed(range(current + 1, size)):
                if perm[i] > perm[current] and not_swapped:
                    new_perm[0] = perm[i]
                    new_perm.append(perm[current])
                    not_swapped = False
                else:
                    new_perm.append(perm[i])
            break

    if current < 0:
        return []
    else:
        return perm[:current] + new_perm 

# from the last element, thinking about an ascnding list, until encountered
# a descending element, this is the element we can change to get the next p
# this time, trying to find an algo with constant extra space
def second(perm):

    size = len(perm)
    current = size - 2

    while current >= 0:
        if perm[current] >= perm[current + 1]:
            current -= 1
        # found the descending element, current
        else:
            # find the smallest element which larger than current
            # and swap these 2 elements
            i = 1
            while size - i > current:
                if perm[size - i] <= perm[current]:
                    i += 1
                else:
                    perm[current], perm[size - i] = perm[size - i], perm[current]
                    break
            # reverse all elements after current
            head = current + 1
            tail = size - 1
            while head < tail:
                perm[head], perm[tail] = perm[tail], perm[head]
                head += 1
                tail -= 1
            break

    if current < 0:
        return []
    else:
        return perm

def next_permutation(perm):
    return first(perm)
    # return second(perm)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
