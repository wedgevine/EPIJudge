#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        current1, current2 = m - 1, n - 1

        while current2 >= 0:
            if current1 >= 0:
                if nums2[current2] > nums1[current1]:
                    nums1[current1 + current2 + 1] = nums2[current2]
                    current2 -= 1
                else:
                    nums1[current1 + current2 + 1] = nums1[current1]
                    current1 -= 1
            else:
                nums1[current1 + current2 + 1] = nums2[current2]
                current2 -= 1

        return
        
# @lc code=end

