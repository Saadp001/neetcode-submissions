class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)

        for i in range(n):
            left = i+1
            right = n-1
            while left<right:
                if nums[i]+nums[left]+nums[right]<0:
                    left+=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    ans.add(tuple(sorted([nums[i],nums[left],nums[right]]))) 
                    left +=1
                    right -=1       

        return [list(t) for t in ans]               
            


        