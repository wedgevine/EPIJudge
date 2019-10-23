# used as a sample question in 
# How to: Work at Google — Example Coding/Engineering Interview
# the last question, what if the list is huge which can't put in memory
# the guy asked the right question, can the comp list put in memory?
# if yes, the input list can be chunked into smaller part
# either processed one by one or in parallel, for each chunk, do the same

# in the following 4 solutions, the 4th is brute force, the other 3 are the
# same, single pass hash

class Solution:
    # Success
    # Details 
    # Runtime: 56 ms, faster than 88.21% of Python3 online submissions for Two Sum.
    # Memory Usage: 15.6 MB, less than 5.11% of Python3 online submissions for Two Sum.
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        result = []
        candidate = {}
        
        for i, num in enumerate(nums):
            pair = target - num
            if pair in candidate:
                result = [candidate[pair], i]
            candidate[num] = i
            
        return result

    # Success
    # Details 
    # Runtime: 56 ms, faster than 88.21% of Python3 online submissions for Two Sum.
    # Memory Usage: 15.1 MB, less than 5.11% of Python3 online submissions for Two Sum.
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        candidate = {}
        
        for i, num in enumerate(nums):
            pair = target - num
            if pair in candidate:
                return [candidate[pair], i]
            candidate[num] = i
            
        return []
        
    # Success
    # Details 
    # Runtime: 60 ms, faster than 70.25% of Python3 online submissions for Two Sum.
    # Memory Usage: 15.3 MB, less than 5.11% of Python3 online submissions for Two Sum.    
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        comp = {}
         
        for i, num in enumerate(nums):
            if num in comp:
                return [comp[num], i]
            comp[target - num] = i
        
        return []

    # Success
    # Details 
    # Runtime: 5228 ms, faster than 20.64% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.9 MB, less than 10.00% of Python3 online submissions for Two Sum.
    def twoSum4(self, nums: List[int], target: int) -> List[int]:

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    # return [i, j]
                    return [i, i + 1 + j]


        return []