#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_len, current, size = 0, 0, len(nums)
        current_value = float('nan')
        already_two = False

        while current < size:
            if nums[current] != current_value:
                nums[new_len] = nums[current]
                current_value = nums[current]
                new_len += 1
                already_two = False
            elif nums[current] == current_value and not already_two:
                nums[new_len] = nums[current]
                new_len += 1
                already_two = True
            current += 1

        return new_len
        
# @lc code=end

