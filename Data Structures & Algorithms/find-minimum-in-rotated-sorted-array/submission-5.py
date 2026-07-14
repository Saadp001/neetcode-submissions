class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]
            
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]