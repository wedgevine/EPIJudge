from test_framework import generic_test
from list_node import ListNode

# from book, a two lists solution
# be careful with what next pointing
# seperate the variables with the objects they pointing
def second(L):
    if not L: return L

    even_head, odd_head = ListNode(0), ListNode(0)
    tail, turn = [even_head, odd_head], 0

    while L:
        tail[turn].next = L
        tail[turn] = tail[turn].next
        L = L.next
        turn ^= 1
    tail[1].next = None
    tail[0].next = odd_head.next

    return even_head.next

def first(L):
    if not L: return L

    even_tail, odd_tail = L, L.next
    current, current_parity = L.next, 1

    while current:
        if (current_parity % 2) == 0:
            odd_tail.next = current.next
            odd_tail = odd_tail.next
            current.next = even_tail.next
            even_tail.next = current
            even_tail = current
            current = odd_tail
        else:
            current = current.next
        current_parity += 1

    return L

def even_odd_merge(L):
    # return first(L)
    return second(L)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
