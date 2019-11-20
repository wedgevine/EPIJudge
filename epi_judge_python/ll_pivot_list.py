import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from list_node import ListNode

def first(l, x):
    front_head, middle_head, rear_head = ListNode(0), ListNode(0), ListNode(0)
    front_tail, middle_tail, rear_tail = front_head, middle_head, rear_head

    while l:
        if l.data < x:
            front_tail.next = l
            front_tail = front_tail.next
        elif l.data == x:
            middle_tail.next = l
            middle_tail = middle_tail.next
        else:
            rear_tail.next = l
            rear_tail = rear_tail.next
        l = l.next
    rear_tail.next = None
    middle_tail.next = rear_head.next
    front_tail.next = middle_head.next
    # if middle_head.next:
    #     front_tail.next = middle_head.next
    #     front_tail = middle_tail
    # if rear_head.next:
    #     front_tail.next = rear_head.next
    #     front_tail = rear_tail
    # front_tail.next = None 

    return front_head.next

def list_pivoting(l, x):
    return first(l, x)


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
