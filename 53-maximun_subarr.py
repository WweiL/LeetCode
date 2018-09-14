class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-2, -1, -1):
            nums[i] = max(nums[i]+nums[i+1], nums[i])
        return max(nums)
