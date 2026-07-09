class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            maxi = nums[i]
            for j in range(i+1, len(nums)):
                maxi = max(nums[i], nums[j], nums[j+1])
                ans.append(maxi)
                break
        return ans        