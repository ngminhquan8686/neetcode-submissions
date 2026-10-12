class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , profit = 0, 0
        for r in range(len(prices)):
            profit = max(prices[r] - prices[l], profit)

            while prices[r] - prices[l] < 0:
                l += 1
        
        return profit



        