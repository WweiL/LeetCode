class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        best_solution = []
        if len(nums) < 3:
            return []
        prefix_sum = [nums[0]] * size
        for i in range(1, size):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        dp = [[0]*(size+1) for _ in range(4)]
        sol = [[[]]*(size+1) for _ in range(4)]
        max_sum = 0
        for level in range(1, 4):
            for i in range(size - k*level, -1, -1):
                dp[level][i] = dp[level][i+1]
                sol[level][i] = sol[level][i+1]
                
                sum_k = prefix_sum[i+k-1] - (0 if i == 0 else prefix_sum[i-1])
                if dp[level-1][i+k] + sum_k >= dp[level][i]:
                    dp[level][i] = dp[level-1][i+k] + sum_k
                    sol[level][i] = [i] + sol[level-1][i+k]
                
                if level == 3 and dp[level][i] >= max_sum:
                    max_sum = dp[level][i]
                    best_solution = sol[level][i]
        return best_solution
    
    
