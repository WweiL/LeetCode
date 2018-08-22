class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from copy import copy, deepcopy
        def p(nums, l, ans, i):
            nums.remove(i)
            l.append(i)
            if not nums:
                ans.append(l)
            else:
                for j in nums:
                    p(copy(nums), copy(l), ans, j)
        
        ans = []
        nums = set(nums)
        for i in nums:
            p(copy(nums), [], ans, i)

        return ans
            
