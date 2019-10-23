#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (72.83%)
# Likes:    589
# Dislikes: 62
# Total Accepted:    135.9K
# Total Submissions: 186.5K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        size = len(A)
        next_even, next_odd = 0, size - 1

        while next_even < next_odd:
            if A[next_even] % 2 == 0:
                next_even += 1
            else:
                A[next_even], A[next_odd] = A[next_odd], A[next_even]
                next_odd -= 1
        
        return A
        
# @lc code=end

