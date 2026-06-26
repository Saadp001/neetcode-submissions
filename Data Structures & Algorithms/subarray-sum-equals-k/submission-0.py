class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        sum = 0
        for i in range(n):
            for j in range(i, n):
                for l in range(i, j+1):
                    sum += nums[l]
                if sum == k:   # the sum should be after all l elements end that is subarray
                    cnt +=1
                       
                sum = 0

        return cnt        