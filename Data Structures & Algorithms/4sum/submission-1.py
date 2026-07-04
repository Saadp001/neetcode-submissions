class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n):
            j = n-i-1
            left = i+1
            right = j-1

            while left<right:
                total = nums[i]+nums[j]+nums[left]+nums[right]
                if total<target:
                    left+=1
                elif total>target:
                    right-=1

                else:
                    ans.add(tuple(sorted([nums[i],nums[j],nums[left],nums[right]])))
                    left+=1
                    right-=1

        return [list(t) for t in ans]