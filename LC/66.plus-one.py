#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        carryon = 1
        for i in reversed(range(size)):
            sum = carryon + digits[i]
            digits[i] = sum % 10
            carryon = sum // 10
            if not carryon:
                break

        if carryon:
            return [carryon] + digits[:]
        else:
            return digits
        
# @lc code=end

