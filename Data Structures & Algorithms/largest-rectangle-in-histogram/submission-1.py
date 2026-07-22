class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ht = heights
        
        maxi  = 0

        for i in range(len(ht)):
            mini_ht = float('inf')
            for j in range(i, len(ht)):
                mini_ht = min(mini_ht, ht[j])
                area = mini_ht * (j-i+1)
                maxi = max(maxi, area)

        return maxi          