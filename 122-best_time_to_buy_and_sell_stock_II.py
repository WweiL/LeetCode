class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        profit = 0
        end = 0
        while end < n:
            while end+1 < n and prices[end] > prices[end+1]:
                end += 1
            minPrice = prices[end]
            while end+1 < n and prices[end] < prices[end+1]:
                end += 1
            profit += prices[end] - minPrice
            end += 1
        return profit
