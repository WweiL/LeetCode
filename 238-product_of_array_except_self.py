class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        tmp = 1
        for i in range(n):
            ans[i] = tmp
            tmp *= nums[i]

        tmp = nums[-1]
        for i in range(n-2, -1, -1):
            ans[i] *= tmp
            tmp *= nums[i]

        return ans
