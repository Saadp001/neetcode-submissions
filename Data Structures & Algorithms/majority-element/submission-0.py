class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            cnt = 0
            maxi = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    cnt +=1
                if cnt > n/2:
                    return nums[i]     
        #     maxi = max(cnt, maxi)

        # return maxi    

        