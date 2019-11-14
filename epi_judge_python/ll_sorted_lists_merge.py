from test_framework import generic_test
from list_node import ListNode

# from book, more elegent, using dummy head
def second(L1, L2):
    head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    
    tail.next = L1 or L2

    return head.next


def first(L1, L2):
    merge_head, merge_current = None, None

    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if L1.data < L2.data:
        merge_head = merge_current = L1
        L1 = L1.next
    else:
        merge_head = merge_current = L2
        L2 = L2.next

    while L1 is not None and L2 is not None:
        if L1.data < L2.data:
            merge_current.next = L1
            L1 = L1.next
        else:
            merge_current.next = L2
            L2 = L2.next
        merge_current = merge_current.next

    if L1 is not None:
        merge_current.next = L1
    if L2 is not None:
        merge_current.next = L2
    
    return merge_head


def merge_two_sorted_lists(L1, L2):
    # return first(L1, L2)
    return second(L1, L2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
