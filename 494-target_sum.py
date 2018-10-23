class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # n = len(nums)
        # sums = [[0] * (S+1) for _ in range(n+1)]
        # sums[n][0] = 1
        # for i in range(n-1, -1, -1):
        #     num = nums[i]
        #     for v in range(0, S+1):
        #         plus  = sums[i+1][v+num] if v+num <= S else 0
        #         minus = sums[i+1][v-num] if v-num >= 0 else 0
        #         print(plus, minus, i, v)
        #         sums[i][v] = plus + minus
        # return sums[0][S]
        from collections import defaultdict
        if not nums:
            return 0
        rem2cnt = defaultdict(int)
        if nums[0] == 0:
            rem2cnt[nums[0]] = 2
        else:
            rem2cnt[nums[0]] = 1
            rem2cnt[-nums[0]] = 1
        for num in nums[1:]:
            temp = defaultdict(int)
            for rem in rem2cnt.keys():
                temp[rem + num] += rem2cnt[rem]
                temp[rem - num] += rem2cnt[rem]
            rem2cnt = temp
        return rem2cnt[S]
    
        """
        # brute force, recursive DFS O(2^n)
        count = 0
        def findTargetSumWays(self, nums, S):
            if len(nums) == 0 and S == 0:
                self.count += 1
            elif len(nums) > 0:
                left = self.findTargetSumWays(nums[1:], S-nums[0])
                right = self.findTargetSumWays(nums[1:], S+nums[0])
            return self.count
        """
        """
        # recusive dfs with memoization
        def findTargetSumWays(self, nums, S):
            index = 0
            cache = {}
            return self.dfs_mem(index, nums, S, cache)

        def dfs_mem(self, index, nums, S, cache):
            if index == len(nums) and S == 0:
                return 1
            if index == len(nums) and S != 0:
                return 0
            if (index, S) in cache:
                return cache[(index, S)]
            left = self.dfs_mem(index+1, nums, S-nums[index], cache)
            right = self.dfs_mem(index+1, nums, S+nums[index], cache)
            cache[(index+1, S-nums[index])] = left
            cache[(index+1, S+nums[index])] = right
            return left+right
        """
        """
        #dp
        def findTargetSumWays(self, nums, S):
            Sum = sum(nums)
            if Sum < S or (Sum+S)%2 != 0:
                return 0
            target = int((Sum+S)/2)
            dp = [0] * (target+1)
            dp[0] = 1
            for num in nums:
                for j in reversed(range(target+1)):
                    if j-num < 0:
                        continue
                    dp[j] += dp[j-num]
                    #print("dp[",j,"]=",dp[j])
            return dp[target]
        """
