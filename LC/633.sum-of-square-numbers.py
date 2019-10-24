#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.60%)
# Likes:    385
# Dislikes: 257
# Total Accepted:    52.3K
# Total Submissions: 160.4K
# Testcase Example:  '5'
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a^2 + b^2 = c.
# 
# Example 1:
# 
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: False
# 
# 
# 
# 
#

# @lc code=start
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            s = a * a + b * b
            if c == s:
                return True
            elif c < s:
                b -= 1
            else:
                a += 1
        
        return False
        
# @lc code=end

