class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)-1
        m = heights[n]
        return m*m
        