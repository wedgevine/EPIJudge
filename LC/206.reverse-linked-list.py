#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (57.36%)
# Likes:    3050
# Dislikes: 74
# Total Accepted:    739.1K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # iterative solution
    def first(self, head):
        dummy = ListNode(0)
        dummy.next = head
        next_node = dummy.next

        while next_node and next_node.next:
            tmp = next_node.next
            dummy.next, tmp.next, next_node.next = tmp, dummy.next, tmp.next

        return dummy.next

    # recursive solution
    def rr(self, head, last):
        if head:
            next_node = head.next
            head.next = last
            return self.rr(next_node, head)
        else:
            return last

    def second(self, head):
        return self.rr(head, None)

    def third(self, head):
        if not head: return head

        pre_node, next_node = head, head.next

        while next_node:
            tmp = next_node.next
            next_node.next = pre_node
            pre_node = next_node
            next_node = tmp

        return pre_node

    # from LC, change pointer direction from start to end
    def forth(self, head):
        pre_node, current_node = None, head

        while current_node:
            # difficult to understand
            # pre_node, current_node.next, current_node = current_node, pre_node, current_node.next
            tmp = current_node.next
            current_node.next = pre_node
            pre_node, current_node = current_node, tmp
        
        return pre_node

    # recursive from LC, the key is changing pointer direction
    def fifth(self, head):
        if not head or not head.next: return head
        new_head = self.fifth(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        # return self.first(head)
        # return self.second(head)
        # return self.third(head)
        # return self.forth(head)
        return self.fifth(head)
        
# @lc code=end

