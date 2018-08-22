class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = slow = 0
        while fast < len(nums):
            if fast > 0 and nums[fast] == nums[fast-1]:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1; slow += 1
        return slow
