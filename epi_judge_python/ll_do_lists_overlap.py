import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_cyclic_node(head):
    def cycle_len(end):
        start = end
        step = 0

        while True:
            start = start.next
            step += 1
            if start is end:
                return step

    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            cl = cycle_len(slow)
            slow = fast = head
            for _ in range(cl):
                fast = fast.next
            while True:
                if slow is fast:
                    return slow
                slow = slow.next
                fast = fast.next

    return None

def get_terminated_overlap(l0, l1):
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
    l0_cnode = get_cyclic_node(l0)
    l1_cnode = get_cyclic_node(l1)

    # print('\n', l0_cnode, l1_cnode)

    if not l0_cnode and not l1_cnode:
        return get_terminated_overlap(l0, l1)
    elif l0_cnode and l1_cnode:
        l1_slow, l1_fast = l1_cnode.next, l1_cnode.next.next
        while l1_slow is not l1_fast and l1_slow is not l0_cnode:
            l1_slow = l1_slow.next
            l1_fast = l1_fast.next.next
        if l1_slow is l0_cnode:
            return l0_cnode
        else:
            return None
    else:
        return None

# first is not right, for both list sharing the same cycle,
# the first shared node could be in the stem or in the cycle
def second(l0, l1):
    def get_distance(a, b):
        d = 0
        while a is not b:
            a = a.next
            d += 1
        return d

    l0_cnode = get_cyclic_node(l0)
    l1_cnode = get_cyclic_node(l1)

    if not l0_cnode and not l1_cnode:
        return get_terminated_overlap(l0, l1)
    elif l0_cnode and l1_cnode:

        l1_slow, l1_fast = l1_cnode.next, l1_cnode.next.next
        while l1_slow is not l0_cnode and l1_slow is not l1_fast:
            l1_slow, l1_fast = l1_slow.next, l1_fast.next.next
        if l1_slow is not l0_cnode:
            return None
        
        d0 = get_distance(l0, l0_cnode)
        d1 = get_distance(l1, l1_cnode)
        if d0 > d1:
            l0, l1 = l1, l0
            l0_cnode, l1_cnode = l1_cnode, l0_cnode
        for _ in range(abs(d0 - d1)):
            l1 = l1.next
        while l0 is not l1 and l0 is not l0_cnode and l1 is not l1_cnode:
            l0, l1 = l0.next, l1.next
        
        return l0 if l0 is l1 else l0_cnode
        
    else:
        return None

def overlapping_lists(l0, l1):
    # return first(l0, l1)
    return second(l0, l1)


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
