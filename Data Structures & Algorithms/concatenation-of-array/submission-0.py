class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in nums:
            ans.append(nums[i])

        return ans    
            


        