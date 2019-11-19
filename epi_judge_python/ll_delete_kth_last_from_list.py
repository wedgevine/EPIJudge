from test_framework import generic_test
from list_node import ListNode


def first(L, k):
    dummy = ListNode(0, L)
    slow, fast = dummy, L

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next 


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    return first(L, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
