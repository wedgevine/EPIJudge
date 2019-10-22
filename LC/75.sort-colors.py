#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        after_red, current, before_blue = 0, 0, size - 1

        while current <= before_blue:
            color = nums[current]
            if color == 2:
                nums[current], nums[before_blue] = nums[before_blue], nums[current]
                before_blue -= 1
            else:
                if color == 0:
                    nums[current], nums[after_red] = nums[after_red], nums[current]
                    after_red += 1
                current += 1

        return
            
            
        
# @lc code=end

