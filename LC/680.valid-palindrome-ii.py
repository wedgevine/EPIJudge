#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (35.09%)
# Likes:    985
# Dislikes: 68
# Total Accepted:    103.5K
# Total Submissions: 293.4K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        size = len(s)
        head, tail = 0, size - 1
        head_has_tried, head_tried_index = False, 0
        tail_has_tried, tail_tried_index = False, 0

        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            elif not head_has_tried:
                    head_tried_index = head
                    tail_tried_index = tail
                    head += 1
                    head_has_tried = True
            elif not tail_has_tried:
                    head = head_tried_index
                    tail = tail_tried_index
                    tail -= 1
                    tail_has_tried = True
            else:
                return False

        return True
        
# @lc code=end

