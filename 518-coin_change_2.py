class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[i][amount]: at the ith coins and with amount money remaining, how many ways
        # dp[n][>0] = 0
        # dp[i][amount] = max(1+dp[i][amount-coins[i]], 1+dp[i+1][amount-coins[i]])
        # return dp[0][amount]
        # coins.sort()
        # n = len(coins)
        # dp = [[0]*(amount+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0] = 0
        # for i in range(amount+1):
        #     dp[n][i] = -float('inf')
        # for i in range(n-1, -1, -1):
        #     for am in range(1, amount+1):
        #         if coins[i] <= am:
        #             val = max(1+dp[i][am-coins[i]], 1+dp[i+1][am-coins[i]], dp[i+1][am])
        #             print(i, am, dp[i][am-coins[i]], dp[i+1][am-coins[i]], val)
        #             dp[i][am] = val# if val > 0 else 0
        # return dp[0][amount] if dp[0][amount] > 0 else 0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[amount]
