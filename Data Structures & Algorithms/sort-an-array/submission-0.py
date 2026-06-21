class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            minIdx = i
            for j in range(i+1, n):
                if nums[j] < nums[minIdx]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums