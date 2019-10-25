#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (62.76%)
# Likes:    601
# Dislikes: 76
# Total Accepted:    116.9K
# Total Submissions: 186.1K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
# 
# Note:
# 
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# 
# 
# 
# Example 1:
# 
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# 
# 
# 
# Example 2:
# 
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
# 
# 
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        # return self.first(num)
        return self.second(num)

    def second(self, num):
        mask = 1

        while mask <= num:
            mask <<= 1            

        return (mask - 1) ^ num

    def first(self, num):
        c, order = 0, 0

        while num:
            c = ((1 ^ (num & 1)) << order) | c
            order += 1
            num >>= 1

        return c
        
# @lc code=end

