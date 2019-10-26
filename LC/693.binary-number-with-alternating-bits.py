#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (58.38%)
# Likes:    332
# Dislikes: 74
# Total Accepted:    48.4K
# Total Submissions: 82.9K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# 
# 
# 
# Example 2:
# 
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# 
# 
# 
# Example 3:
# 
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# 
# 
# 
# Example 4:
# 
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
# 
# 
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # return self.first(n)
        # return self.second(n)
        return self.thrid(n)

    # if true, n must be in format:
    # 1010..10 or
    # 1010..101

    def thrid(self, n):
        return n & (n >> 1) == 0 and n & (n >> 2) == (n >> 2)

    def second(self, n):
        m = (n ^ (n >> 1)) + 1
        # if true, m must be power of 2
        return m & (m - 1) == 0

    def first(self, n):
        parity = n & 1

        while n:
            n >>= 1
            if parity == n & 1:
                return False
            parity = n & 1

        return True
        
# @lc code=end

