from test_framework import generic_test

# succint version from book
def second(L):
    it = L

    while it:
        it_next = it.next
        while it_next and it_next.data == it.data:
            it_next = it_next.next
        it.next = it_next
        it = it_next

    return L

# in first try, forgot 2 corner cases:
# at the end, slow could be None and slow.next should be None
def first(L):
    slow = fast = L

    while fast:
        if fast.data != slow.data:
            slow.next = fast
            slow = fast
        fast = fast.next
    
    if slow:
        slow.next = None

    return L

def remove_duplicates(L):
    # return first(L)
    return second(L)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
