#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_len, checked_len, size = 0, 1, len(nums)

        while checked_len < size:
            if nums[checked_len] == nums[new_len]:
                checked_len += 1
            else:
                new_len += 1
                nums[new_len] = nums[checked_len]

        return new_len + 1
        
# @lc code=end

