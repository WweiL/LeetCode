class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from bisect import bisect_left
        # dp[i]: the last element in nums with LIS length i
        n = len(nums)
        dp = [float('inf')] * n
        length = 0
        for i in nums:
            pos = bisect_left(dp, i)
            if pos == length:
                length += 1
            dp[pos] = i
        return length

    # # O(n**2)
    # # def lengthOfLIS(self, nums):
    # #     """
    # #     :type nums: List[int]
    # #     :rtype: int
    # #     """
    # #     if not nums:
    # #         return 0
    # #     n = len(nums)
    # #     lis = [1] * n
    # #     for i in range(n-2, -1, -1):
    # #         possible = [lis[l] for l in range(i+1, n) if nums[l] > nums[i]]
    # #         lis[i] = 1 + (0 if possible == [] else max(possible))
    # #     return max(lis)
