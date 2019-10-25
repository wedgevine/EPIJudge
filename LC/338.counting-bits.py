#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (65.85%)
# Likes:    1699
# Dislikes: 120
# Total Accepted:    197.3K
# Total Submissions: 299.3K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,1]
# 
# Example 2:
# 
# 
# Input: 5
# Output: [0,1,1,2,1,2]
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
# 
#

# @lc code=start

import math

class Solution:
    def countBits(self, num: int) -> List[int]:
        # return self.first(num)
        # return self.second(num)
        return self.third(num)

    # if i is even, result[i] = result[i/2]
    # if i is odd, result[i] = result[(i-1)/2] + 1
    def third(self, num):
        result = [0] * (num + 1)

        for i in range(1, num + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result

    # by hint, count by range, based on values from previous range
    def second(self, num):
        count, result = 1, [0]

        while count <= num:
            for i in range(count):
                if count + i <= num:
                    result.append(result[i] + 1)
                else:
                    break
            count *= 2            

        return result

    # add one by one, based on previous count
    def first(self, num):
        result = [0]
        i, pre_count = 1, 0

        while i <= num:
            if i & 1 == 1:
                pre_count += 1
            else:
                pre_count = pre_count - (int(math.log((i ^ (i - 1)) + 1, 2)) - 2)

            result.append(pre_count)
            i += 1

        return result
    

       
# @lc code=end

