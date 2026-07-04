class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ans = list(set(nums))
        n= len(ans) 
        k =0
        for i in range(n):
            nums[i] = ans[i]
            k+=1


        return k


