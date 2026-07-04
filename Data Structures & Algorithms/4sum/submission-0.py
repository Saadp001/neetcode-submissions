class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        total = nums[i]+nums[j]+nums[k]+nums[l]

                        if total == target:
                            ans.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
        
        return [list(t) for t in ans]