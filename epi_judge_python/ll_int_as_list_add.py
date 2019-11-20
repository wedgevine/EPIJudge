from test_framework import generic_test
from list_node import ListNode

# the most important point in linked list is assigning to iter.next
# and iter = iter.next, by doing this, list can be changed iteratively
def first(L1, L2):

    sum_head = ListNode(0)
    sum_iter = sum_head
    carry, s = 0, 0
    
    while carry or L1 or L2:
        s = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        sum_iter.next = L1 or L2
        if not sum_iter.next: sum_iter.next = ListNode(0)
        sum_iter.next.data = s % 10
        carry = s // 10
        sum_iter = sum_iter.next
        if L1: L1 = L1.next
        if L2: L2 = L2.next

    return sum_head.next

def add_two_numbers(L1, L2):
    return first(L1, L2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
