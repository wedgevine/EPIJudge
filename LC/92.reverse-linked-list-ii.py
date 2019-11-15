#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (36.28%)
# Likes:    1579
# Dislikes: 109
# Total Accepted:    225.1K
# Total Submissions: 616.3K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def first(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        pre_start = dummy

        for _ in range(m - 1):
            pre_start = pre_start.next

        next_node = pre_start.next
        for _ in range(m, n):
            tmp = next_node.next
            next_node.next = tmp.next
            pre_start.next, tmp.next = tmp, pre_start.next

        return dummy.next
        
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        return self.first(head, m, n)
# @lc code=end

