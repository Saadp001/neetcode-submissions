class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        mini = float('inf')

        for i in range(n):
            total = 0
            for j in range(i,n):
                total+=nums[j]
                if total >= target:
                    mini = min(mini, j-i+1)
                    break

        return mini if mini != float('inf') else 0    

