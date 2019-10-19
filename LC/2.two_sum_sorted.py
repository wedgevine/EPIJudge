# Success
# Details 
# Runtime: 76 ms, faster than 63.01% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.1 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        
        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start + 1, end + 1]
            if s < target:
                start += 1
            if s > target:
                end -= 1
                
        return []
        