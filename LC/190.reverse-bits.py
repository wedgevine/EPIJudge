class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return self.second(n)
        
    def bf(self, n):
        r = 0
        for i in range(32):
            r = (r << 1) + (n & 0x1)
            n = n >> 1
        return r
        
    def second(self, n):
        n = (n << 16) | (n >> 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n
        