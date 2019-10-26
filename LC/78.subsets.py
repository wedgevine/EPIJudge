#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (55.64%)
# Likes:    2470
# Dislikes: 60
# Total Accepted:    433.7K
# Total Submissions: 776.4K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.first(nums)
        return self.second(nums)

    # elegent solution from LC
    def second(self, nums):
        result = [[]]

        for n in nums:
            result += [r + [n] for r in result]
        
        return result

    def first(self, nums):
        result = [[]]

        while nums:
            n = nums.pop()
            new_result = []
            for r in result:
                rc = list(r)
                rc.append(n)
                new_result.append(rc)
            result = result + new_result

        return result
        
# @lc code=end

