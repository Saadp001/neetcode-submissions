class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for i in range(len(nums)):
            mini = min(nums[i], mini)

        return mini    
             