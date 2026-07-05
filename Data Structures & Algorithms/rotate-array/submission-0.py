class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # handle k > n

        nums[:] = nums[::-1]        # reverse whole array
        nums[:k] = nums[:k][::-1]   # reverse first k
        nums[k:] = nums[k:][::-1]   # reverse rest