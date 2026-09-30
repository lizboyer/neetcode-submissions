class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = 100
        max_diff = 0
        i = 0
        j = len(prices) -1
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                max_price = 0
            if prices[i] > max_price:
                max_price = prices[i]
            max_diff = max(max_diff, max_price - min_price)
        return (max_diff)