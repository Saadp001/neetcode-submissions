class Solution:
    def solve(self,nums, i,temp):
        if i >= len(nums):
            self.res.append(temp[:])
            return 

        temp.append(nums[i])
        self.solve(nums, i+1, temp)
        temp.pop()
        self.solve(nums, i+1, temp)
    


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        temp = []        

        self.solve(nums,0,temp)

        return self.res
        