#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    # find the most significant bit where m and n are different
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0: 
            return 0
        if m == n:
            return m

        result = 0
        for i in reversed(range(31)):
            d = pow(2, i)
            qn = n // d
            qm = m // d
            if qn == qm:
                n %= d
                m %= d
                result = (result << 1) + qn
            else:
                result = result << (i + 1)
                break
        
        return result
    

        
# @lc code=end

