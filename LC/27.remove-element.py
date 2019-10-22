#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        head, tail = 0, size - 1

        while head <= tail:
            if nums[head] == val:
                if nums[tail] != val:
                    nums[head], nums[tail] = nums[tail], nums[head]
                    head += 1
                    tail -= 1
                else:
                    tail -= 1
            else:
                head += 1
        
        return head

# @lc code=end

