class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                if i != n-1:
                    nums.pop(i)
                    nums[i+1] = nums[i]
                else:
                    nums.pop(i)    
            
        return len(nums)