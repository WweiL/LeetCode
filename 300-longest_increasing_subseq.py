class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from bisect import bisect_left
        # O(nlogn), see note ->
        if len(nums) == 0:
            return 0
        nums = [float('inf')] + nums
        n = len(nums)
        dp = [-float('inf')] * n
        dp[1] = nums[1]
        length = 1
        for i in range(1, n):
            if nums[i] > dp[length]:
                length += 1
                dp[length] = nums[i]
            else:
                k = bisect_left(dp, nums[i], 0, length)
                dp[k] = nums[i]
        return length
    # O(n**2)
    # def lengthOfLIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     lis = [1] * n
    #     for i in range(n-2, -1, -1):
    #         possible = [lis[l] for l in range(i+1, n) if nums[l] > nums[i]]
    #         lis[i] = 1 + (0 if possible == [] else max(possible))
    #     return max(lis)
