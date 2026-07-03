class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = 0
        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]  
                maxi = max(maxi, profit)

        return maxi

        