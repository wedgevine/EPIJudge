#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (32.65%)
# Likes:    755
# Dislikes: 2189
# Total Accepted:    437.3K
# Total Submissions: 1.3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        head, tail = 0, size - 1

        while head < tail:
            if not s[head].isalnum():
                head += 1
            elif not s[tail].isalnum():
                tail -= 1
            else:
                if s[head].lower() != s[tail].lower():
                    return False
                head += 1
                tail -= 1

        return True
        
        
# @lc code=end

