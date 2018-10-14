class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        left = 0
        right = 1
        res = 2 if nums[right] > nums[left] else 1
        while right < len(nums):
            if nums[right-1] < nums[right]:
                res = max(res, right - left + 1)
            else:
                left = right
            right += 1
        return res
