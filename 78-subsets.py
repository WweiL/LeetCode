class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from copy import copy
        def helper(ans, nums, tmp, i):
            if i >= len(nums):
                ans.append(tmp)
                return ans
            else:
                elem = nums[i]
                helper(ans, nums, copy(tmp), i+1)
                tmp.append(elem)
                helper(ans, nums, copy(tmp), i+1)
        ans = []
        helper(ans, nums, [], 0)
        return ans
