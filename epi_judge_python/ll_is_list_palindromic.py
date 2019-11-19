from test_framework import generic_test
from list_node import ListNode

def get_reverse(L):
    pre_node = None
    current = L
    while current:
        tmp = current.next
        current.next = pre_node
        pre_node = current
        current = tmp
    return pre_node

def first(L):
    if not L: return True

    slow, fast = L, L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    start1 = L
    start2 = get_reverse(slow)
    while start2 and start2.data == start1.data:
        start1 = start1.next
        start2 = start2.next
    return True if not start2 else False


def is_linked_list_a_palindrome(L):
    return first(L)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
