#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (55.37%)
# Likes:    2472
# Dislikes: 90
# Total Accepted:    547.3K
# Total Submissions: 987.3K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.first(nums)
        # self.second(nums)
        self.third(nums)

    def first(self, nums):
        size = len(nums)
        current, first_zero = 0, float('inf')

        while current < size:
            if nums[current] == 0:
                first_zero = min(first_zero, current)
            else:
                if current > first_zero:
                    nums[first_zero], nums[current] = nums[current], nums[first_zero]
                    if nums[first_zero + 1] == 0:
                        first_zero += 1
                    else:
                        first_zero = float('inf')
            current += 1
    
    def second(self, nums):
        zero_start = float('inf')

        for i, n in enumerate(nums):
            if n == 0:
                zero_start = min(i, zero_start)
            else:
                if i > zero_start:
                    nums[zero_start], nums[i] = n, 0
                    zero_start = zero_start + 1 if nums[zero_start + 1] == 0 else float('inf')

    def third(self, nums):
        last_non_zero = -1

        for i, n in enumerate(nums):
            if n != 0:
                last_non_zero += 1
                nums[last_non_zero] = n

        for i in range(last_non_zero + 1, len(nums)):
            nums[i] = 0
# @lc code=end

