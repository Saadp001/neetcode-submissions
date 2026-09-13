class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def solve(start, temp):
            res.append(temp[:])
              

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                                                                                    
                temp.append(nums[i])
                solve(i+1, temp) 
                temp.pop()   

        solve(0, [])
        return res



   