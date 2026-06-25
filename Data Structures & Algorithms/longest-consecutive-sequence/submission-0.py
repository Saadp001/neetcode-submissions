class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # list(set(nums)).sort() — .sort() sorts in place and returns None. So ans = None
        ans = list(set(nums))
        ans.sort()
        
        cnt = 1
        maxi = 0

        for i in range(len(ans)-1):
            if ans[i] + 1 == ans[i+1]:
                cnt += 1
                maxi = max(cnt, maxi)
            else:
                cnt = 1

        return maxi            

        
