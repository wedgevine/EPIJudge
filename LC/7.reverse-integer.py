#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        limit = pow(2, 31)
        if  (-1) * limit <= x <= limit - 1:
            sign = 1 if x >= 0 else -1 
            x = x * sign
            result = 0

            while x > 0:
                result = result * 10 + (x % 10)
                x = x // 10

            result *= sign
            if (-1) * limit <= result <= limit - 1:
                return result
            else:
                return 0
        else:
            return 0
        
# @lc code=end

