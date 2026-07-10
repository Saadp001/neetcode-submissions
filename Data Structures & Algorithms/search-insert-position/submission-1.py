class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target > nums[n-1]:
            return n
        mini = float('inf')
        for i in range(n):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                mini = min(nums[i], mini)    

        for i in range(n):
            if nums[i] == mini:
                return i      