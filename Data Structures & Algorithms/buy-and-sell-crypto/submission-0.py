class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float("-inf")

        for x in range(len(prices)):
            for y in range(x, len(prices)):
                maxProfit = max(maxProfit, prices[y] - prices[x])
        
        print(maxProfit)

        return maxProfit
