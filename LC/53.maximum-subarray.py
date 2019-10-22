#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sofar = float('-inf')
        current, current_sum = 0, 0
        size = len(nums)

        while current < size:
            current_sum += nums[current]
            if current_sum > max_sofar:
                max_sofar = current_sum
            if current_sum < 0:
                current_sum = 0
            current += 1

        return max_sofar

# @lc code=end

