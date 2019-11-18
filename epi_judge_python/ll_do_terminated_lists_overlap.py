import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# from book, better pragramming
def second(l0, l1):
    def get_len(l):
        len_l = 0
        while l:
            l = l.next
            len_l += 1
        return len_l

    len0, len1 = get_len(l0), get_len(l1)
    # always let l1 longer than l0
    if len0 > len1:
        l0, l1 = l1, l0
    for _ in range(abs(len0 - len1)):
        l1 = l1.next
    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    return l0

def first(l0, l1):

    list0, list1 = l0, l1
    len0 = len1 = 0

    while list0 and list0.next:
        list0 = list0.next
        len0 += 1

    while list1 and list1.next:
        list1 = list1.next
        len1 += 1

    if list0 is list1:
        list0, list1 = l0, l1

        if len0 > len1:
            while len0 > len1:
                list0 = list0.next
                len0 -= 1
        elif len1 > len0:
            while len1 > len0:
                list1 = list1.next
                len1 -= 1

        while list0 is not list1:
            list0 = list0.next
            list1 = list1.next
        
        return list0
    else:
        return None


def overlapping_no_cycle_lists(l0, l1):
    # return first(l0, l1)
    return second(l0, l1)


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
