class Solution:
    # timeout
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        current, size = 0, len(nums) - 1
        
        nums.sort()
        while current < size - 1:
            current_value = nums[current]
            if current_value > 0:
                break
            
            current_complement = (-1) * current_value
            start_value = float('nan')
            start, end = current + 1, size
            while start < end:
                s = nums[start] + nums[end]
                if s == current_complement:
                    if start_value != nums[start]:
                        result.append([current_value, nums[start], nums[end]])
                        start_value = nums[start]
                    start += 1
                    end -= 1
                if s < current_complement:
                    start += 1
                if s > current_complement:
                    end -= 1
                    
            while current < size - 1 and nums[current + 1] == current_value:
                current += 1
        
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        current, size = 0, len(nums) - 1
        
        while current < size - 1:
            current_value = nums[current]
            current_complement = (-1) * current_value
            current_candidate = {}

            for num in nums[current + 1:]:
                to_pair = current_complement - num
                if to_pair in current_candidate:
                     

            start_value = float('nan')
            start, end = current + 1, size
            while start < end:
                s = nums[start] + nums[end]
                if s == current_complement:
                    if start_value != nums[start]:
                        result.append([current_value, nums[start], nums[end]])
                        start_value = nums[start]
                    start += 1
                    end -= 1
                if s < current_complement:
                    start += 1
                if s > current_complement:
                    end -= 1
                    
            while current < size - 1 and nums[current + 1] == current_value:
                current += 1
        
        return result