class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1 - i
        while i<j:
            total = nums[i] + nums[j]
            if total== target:
                return [i,j]
            elif total>target: 
                j-=1
            else:
                i+=1    

        return [-1,-1]        
             

            
            




