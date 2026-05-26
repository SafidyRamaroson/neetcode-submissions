class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                buyPrice = prices[i]
                sellPrice = prices[j]
                maxProfit = max(sellPrice - buyPrice, maxProfit)
        return maxProfit
        