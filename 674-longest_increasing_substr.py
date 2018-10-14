class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        left = 0
        right = 1
        res = 2 if nums[right] > nums[left] else 1
        while right < n:
            if nums[right-1] < nums[right]:
                res = max(res, right - left + 1)
            else:
                left = right
            right += 1
        return res
