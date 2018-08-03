class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = 0
                nums[pos] = temp
                pos += 1
