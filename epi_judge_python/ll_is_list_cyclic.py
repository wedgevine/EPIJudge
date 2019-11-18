import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def get_cycle_length(head):
    try:
        slow = head.next
        fast = slow.next

        while slow is not fast:
            slow = slow.next
            fast = fast.next.next

        step = 1
        slow = slow.next
        fast = fast.next.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
            step += 1

        return step
    except AttributeError:
        return 0

def first(head):
    c = get_cycle_length(head)

    if c == 0:
        return None

    slow = fast = head
    for _ in range(c):
        fast = fast.next

    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow

def second(head):
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

def has_cycle(head):
    return first(head)
    # return second(head)


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", 'is_list_cyclic.tsv', has_cycle_wrapper))
