class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy = prices[0]

        for x in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[x] - buy)

            if prices[x] < buy:
                buy = prices[x]        

        return maxProfit
