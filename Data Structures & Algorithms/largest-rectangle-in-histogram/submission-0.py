class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ht = heights
        
        maxi  = -1

        for i in range(len(ht)):
            for j in range(i, len(ht)):
                mini_ht = float('inf')
                for k in range(i, j+1):
                    
                    mini_ht = min(mini_ht, ht[k])

                area = mini_ht * (j-i+1)
                maxi = max(maxi, area)

        return maxi          