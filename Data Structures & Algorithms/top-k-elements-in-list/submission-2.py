from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n = len(nums)
        last = slast = n-1
        
        # Added -1 step so the loop actually runs backwards
        for i in range(len(nums)-1, -1, -1):
            if nums[last] != nums[i]:
                slast = nums[i]
                # Wrapped in brackets to return a List[int]
                return [nums[last], slast]

        return [nums[last]]
