class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        s = 0
        mini = float('inf')
        while r<len(nums):     
            if s < target:
                s+=nums[r]
                r+=1
            
            while s >= target:
                mini = min(mini, r - l)
                s -= nums[l]
                l += 1

        return mini if mini != float('inf') else 0

                
        