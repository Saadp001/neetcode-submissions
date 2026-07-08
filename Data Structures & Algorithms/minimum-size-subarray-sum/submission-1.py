class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        mini = float('inf')

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    mini = min(mini, j-i+1)

        return mini if mini != float('inf') else 0    

