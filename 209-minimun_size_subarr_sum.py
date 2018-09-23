class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = 0
        min_len = float('inf')
        tmp = 0
        while end < n:
            tmp += nums[end]
            while tmp >= s:
                min_len = min(min_len, end-start+1)
                tmp -= nums[start]
                start += 1
            end += 1
        
        return min_len if min_len != float('inf') else 0
