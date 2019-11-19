from test_framework import generic_test
from list_node import ListNode


def get_len(L):
    list_len = 0

    while L:
        L = L.next
        list_len += 1

    return list_len

# from book, a cyclic solution
def second(L, k):
    if not L: return L
    tail, list_len = L, 1
    while tail.next:
        tail = tail.next
        list_len += 1
    k %= list_len
    if k == 0: return L

    # make it a cycle
    tail.next = L

    count = list_len - k
    for _ in range(count):
        tail = tail.next

    new_head = tail.next
    tail.next = None

    return new_head

# note the corner cases for L and k
def first(L, k):
    list_len = get_len(L)
    if list_len == 0: return L
    k %= list_len
    if k == 0: return L

    dummy = ListNode(0, L)
    slow = fast = dummy

    for _ in range(k):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next

    new_head = slow.next
    slow.next, fast.next = None, L

    return new_head

def cyclically_right_shift_list(L, k):
    # return first(L, k)
    return second(L, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
