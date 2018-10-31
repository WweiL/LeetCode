class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        zero_cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
            else:
                zero_cnt += 1
        for i in range(n-1, n-zero_cnt-1, -1):
            nums[i] = 0
        # pos = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         temp = nums[i]
        #         nums[i] = 0
        #         nums[pos] = temp
        #         pos+= 1
