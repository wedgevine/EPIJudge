#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        origin_x = x
        while x > 0:
            reversed_x = reversed_x * 10 + (x % 10)
            x //= 10

        return (origin_x == reversed_x)
        
# @lc code=end

