#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        score = 0
        candidate = None

        for i in nums:
            if score == 0:
                candidate = i
            score += (1 if candidate == i else -1)
        
        return candidate

    def first(self, nums: List[int]) -> int:
        stat = {}
        size = len(nums)
        if size == 1:
            return nums[0]

        for num in nums:
            if num in stat:
                stat[num] += 1
                if stat[num] >= size / 2:
                    return num
            else:
                stat[num] = 1        

# @lc code=end

