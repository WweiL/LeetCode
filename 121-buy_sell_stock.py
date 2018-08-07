class Solution:
    # Greedy
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                maxProfit = max(maxProfit, p-minPrice)
        return maxProfit
        
      # DP
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) <= 1:
#             return 0
        
#         dp = [0] * len(prices)
#         dp[-1] = 0
#         for i in range(len(prices)-2, -1, -1):
#             val = prices[i+1] - prices[i]
#             print(val)
#             dp[i] =  val + dp[i+1] if dp[i+1] > 0 else val
            
#         return max(dp)
