#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # utilze fact x ^ x = 0
        result = 0
        for n in nums:
            result ^= n
        
        return result

    def first(self, nums: List[int]) -> int:
        history = {}

        for n in nums:
            if not n in history:
                history[n] = 1
            else:
                history[n] = 0
        
        for n in history:
            if history[n] == 1:
                return n

        
# @lc code=end

