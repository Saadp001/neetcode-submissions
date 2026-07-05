class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxi = 1
        for i in range(n):
            for j in range(i+1,n):
                dis = j-i
                mini = min(heights[i], heights[j])
                total = dis*mini

                maxi = max(total, maxi)

        return maxi