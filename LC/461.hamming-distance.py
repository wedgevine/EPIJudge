#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (70.70%)
# Likes:    1418
# Dislikes: 136
# Total Accepted:    264.4K
# Total Submissions: 373.9K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 2^31.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0

        while z:
            count += 1
            z = z & (z - 1)

        return count
# @lc code=end

