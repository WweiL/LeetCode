class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums == []:
            return 0
        n = len(nums)
        ans, p_sum = 0, 0
        sum2pos = {0: -1}
        for i in range(n):
            p_sum += nums[i]
            # keep track of the earliest appearance of prefix sum
            if p_sum not in sum2pos:
                sum2pos[p_sum] = i
            if p_sum-k in sum2pos:
                ans = max(ans, i - sum2pos[p_sum-k])
        return ans
        # TLE!
        # if nums == []:
        #     return 0
        # elif len(nums) == 1:
        #     if nums[0] == k:
        #         return 1
        #     else:
        #         return 0
        # else:
        #     maxLength = 0
        #     for i, v in enumerate(nums):
        #         subsum = 0
        #         j = i
        #         while j < len(nums):
        #             subsum += nums[j]
        #             if subsum == k:
        #                 print(i, j, v, nums[j])
        #                 maxLength = max(maxLength, j-i+1)
        #             j += 1
        #     return maxLength
