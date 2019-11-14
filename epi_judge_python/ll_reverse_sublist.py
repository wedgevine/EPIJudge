from test_framework import generic_test
from list_node import ListNode

# shorter solution from book
def second(L, start, finish):
    head = ListNode(0, L)
    pre_start = head

    for _ in range(1, start):
        pre_start = pre_start.next

    iter_node = pre_start.next
    for _ in range(finish - start):
        tmp = iter_node.next
        iter_node.next, pre_start.next, tmp.next = tmp.next, tmp, pre_start.next

    return head.next

def first(L, start, finish):
    if start < 1 or finish < 1 or start > finish:
        return L

    head = ListNode(0, L)
    pre_start_node, finish_node = head, head
    node = None
    count = 1

    while count < start:
        pre_start_node = pre_start_node.next
        count += 1
    finish_node = pre_start_node.next
    while count < finish:
        finish_node = finish_node.next
        count += 1

    # now, extract start node and insert it after finish_node
    count = start
    while count < finish:
        node = pre_start_node.next
        pre_start_node.next = node.next
        node.next = finish_node.next
        finish_node.next = node
        count += 1
        
    return head.next

def reverse_sublist(L, start, finish):
    # return first(L, start, finish)
    return second(L, start, finish)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
